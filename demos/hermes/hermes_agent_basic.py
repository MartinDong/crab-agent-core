import os
import sys
from dotenv import load_dotenv

# 确保能加载项目根目录的 .env
# 文件路径: e:\AiAgent\crab-agent-core\demos\hermes\hermes_agent_basic.py
# 需要两次 dirname() 才能到达项目根目录 e:\AiAgent\crab-agent-core
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(dotenv_path=os.path.join(PROJECT_ROOT, ".env"))

# 将项目根目录和 demos 目录添加到 sys.path 以支持正确的模块导入
sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "demos"))

# 确保 hermes-agent 已安装
# pip install git+https://github.com/NousResearch/hermes-agent.git
try:
    from run_agent import AIAgent
except ImportError:
    print("错误: 未找到 hermes-agent 包。")
    print("请先安装: pip install git+https://github.com/NousResearch/hermes-agent.git")
    sys.exit(1)

from qianfan.config import LLMConfig


class HermesBasicAgent:
    """
    基于 Hermes AIAgent 的简单问答助手
    使用 chat() 方法快速获取文本回复
    配置来源: E:\\AiAgent\\crab-agent-core\\.env
    """

    def __init__(self, model=None, api_key=None, base_url=None):
        """
        初始化 Hermes Agent

        Args:
            model: 模型名称，默认从 .env 的 OPENAI_MODEL_NAME 读取
            api_key: API 密钥，默认从 .env 的 OPENAI_API_KEY 或 QIANFAN_API_KEY 读取
            base_url: API 基础地址，默认从 .env 读取
        """
        # 优先使用显式传入的参数，否则从 .env 读取
        cfg = LLMConfig.get_active_config()
        self.model = model or cfg["model"]
        self.api_key = api_key or cfg["api_key"]
        self.base_url = base_url or cfg["base_url"]
        self.provider = cfg["provider"]

        # 调试：打印实际使用的配置信息
        preview = self.api_key[:16] + "..." if len(self.api_key) > 20 else self.api_key
        print(f"[Config] provider={self.provider}, model={self.model}")
        print(f"[Config] base_url={self.base_url}")
        print(f"[Config] api_key={preview}")

        self.agent = AIAgent(
            model=self.model,
            api_key=self.api_key,
            base_url=self.base_url,
            quiet_mode=True,          # 禁用 CLI 输出，避免污染应用输出
            skip_memory=True,         # 禁用持久化记忆，适合简单问答场景
            skip_context_files=True,  # 不加载 AGENTS.md 文件
        )

    def ask(self, question: str) -> str:
        """
        发送问题并获取回复

        Args:
            question: 用户问题

        Returns:
            模型的文本回复
        """
        return self.agent.chat(question)


if __name__ == "__main__":
    print("=== Hermes Agent 基础问答系统 ===")
    print("使用 chat() 方法快速获取回复")
    print("输入 'quit' 退出")
    print("-" * 40)

    try:
        agent = HermesBasicAgent()
    except ValueError as e:
        print(f"初始化失败: {e}")
        sys.exit(1)

    while True:
        question = input("\n请输入问题: ").strip()
        if question.lower() in ["quit", "exit", "退出", "q"]:
            break
        if not question:
            continue

        print("\n[思考中...]")
        try:
            answer = agent.ask(question)
            print(f"回答: {answer}")
        except Exception as e:
            print(f"调用失败: {e}")
