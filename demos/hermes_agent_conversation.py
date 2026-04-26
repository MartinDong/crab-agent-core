import os
import sys
from dotenv import load_dotenv

# 确保能加载项目根目录的 .env
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(dotenv_path=os.path.join(PROJECT_ROOT, ".env"))

# 确保 hermes-agent 已安装
try:
    from run_agent import AIAgent
except ImportError:
    print("错误: 未找到 hermes-agent 包。")
    print("请先安装: pip install git+https://github.com/NousResearch/hermes-agent.git")
    sys.exit(1)

from config import LLMConfig


class HermesConversationAgent:
    """
    基于 Hermes AIAgent 的多轮对话系统
    使用 run_conversation() 完全控制对话流程
    支持历史记忆、自定义系统提示词、轨迹保存
    配置来源: E:\\AiAgent\\crab-agent-core\\.env
    """

    def __init__(
        self,
        model=None,
        api_key=None,
        base_url=None,
        save_trajectories=False,
        ephemeral_system_prompt=None,
    ):
        """
        初始化对话 Agent

        Args:
            model: 模型名称，默认从 .env 读取
            api_key: API 密钥，默认从 .env 读取
            base_url: API 基础地址，默认从 .env 读取
            save_trajectories: 是否保存对话轨迹到 JSONL
            ephemeral_system_prompt: 自定义系统提示词（不会被写入轨迹）
        """
        cfg = LLMConfig.get_active_config()
        self.model = model or cfg["model"]
        self.api_key = api_key or cfg["api_key"]
        self.base_url = base_url or cfg["base_url"]
        self.provider = cfg["provider"]

        self.agent = AIAgent(
            model=self.model,
            api_key=self.api_key,
            base_url=self.base_url,
            quiet_mode=True,
            save_trajectories=save_trajectories,
            ephemeral_system_prompt=ephemeral_system_prompt,
            skip_context_files=True,
        )
        self.history = []
        self.turn_count = 0

    def chat(self, message: str, system_message: str = None, task_id: str = None) -> dict:
        """
        发送消息并获取完整对话结果

        Args:
            message: 用户消息
            system_message: 临时覆盖系统提示词
            task_id: 任务 ID，用于 VM 隔离

        Returns:
            包含 final_response、messages 等的字典
        """
        result = self.agent.run_conversation(
            user_message=message,
            system_message=system_message,
            conversation_history=self.history if self.history else None,
            task_id=task_id or f"conv-{self.turn_count}",
        )
        self.turn_count += 1

        # 更新历史记录（run_conversation 内部会复制，不会突变原始列表）
        self.history = result.get("messages", [])
        return result

    def get_history_summary(self) -> str:
        """获取当前对话历史的简要摘要"""
        roles = []
        for msg in self.history:
            role = msg.get("role", "unknown")
            roles.append(role)
        return f"总消息数: {len(self.history)} | 角色流转: {' -> '.join(roles[-6:])}"

    def clear_history(self):
        """清空对话历史"""
        self.history = []
        print("对话历史已清空")

    def save_history_to_file(self, filepath: str):
        """将对话历史保存为 JSON 文件"""
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.history, f, ensure_ascii=False, indent=2)
        print(f"历史已保存到: {filepath}")


if __name__ == "__main__":
    print("=== Hermes Agent 多轮对话系统 ===")
    print("使用 run_conversation() 完全控制对话流程")
    print("命令: 'quit'=退出 | 'clear'=清空历史 | 'save'=保存历史 | 'info'=查看状态")
    print("-" * 50)

    try:
        # 示例：使用自定义系统提示词构建专属助手
        agent = HermesConversationAgent(
            save_trajectories=False,  # 设为 True 可保存到 trajectory_samples.jsonl
            ephemeral_system_prompt="你是一个精通 Python 的技术顾问，回答简洁且注重实践。",
        )
    except ValueError as e:
        print(f"初始化失败: {e}")
        sys.exit(1)

    while True:
        user_input = input("\n你: ").strip()
        if not user_input:
            continue

        cmd = user_input.lower()
        if cmd in ["quit", "exit", "q", "退出"]:
            break
        if cmd in ["clear", "清空"]:
            agent.clear_history()
            continue
        if cmd in ["save", "保存"]:
            agent.save_history_to_file("conversation_history.json")
            continue
        if cmd in ["info", "状态"]:
            print(f"[{agent.get_history_summary()}]")
            continue

        print("助手: [思考中...]")
        try:
            result = agent.chat(user_input)
            print(f"助手: {result['final_response']}")
            print(f"[{agent.get_history_summary()}]")
        except Exception as e:
            print(f"调用失败: {e}")
