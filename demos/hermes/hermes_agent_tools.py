import os
import sys
import concurrent.futures
from dotenv import load_dotenv

# 确保能加载项目根目录的 .env
# 文件路径: e:\AiAgent\crab-agent-core\demos\hermes\hermes_agent_tools.py
# 需要两次 dirname() 才能到达项目根目录 e:\AiAgent\crab-agent-core
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(dotenv_path=os.path.join(PROJECT_ROOT, ".env"))

# 将项目根目录和 demos 目录添加到 sys.path 以支持正确的模块导入
sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "demos"))

# 确保 hermes-agent 已安装
try:
    from run_agent import AIAgent
except ImportError:
    print("错误: 未找到 hermes-agent 包。")
    print("请先安装: pip install git+https://github.com/NousResearch/hermes-agent.git")
    sys.exit(1)

from qianfan.config import LLMConfig


def _get_agent_config(model=None, api_key=None, base_url=None):
    """封装配置读取逻辑，优先使用显式传入的参数"""
    cfg = LLMConfig.get_active_config()
    return {
        "model": model or cfg["model"],
        "api_key": api_key or cfg["api_key"],
        "base_url": base_url or cfg["base_url"],
        "provider": cfg["provider"],
    }


class HermesWebAgent:
    """
    仅启用 web 工具的 Hermes Agent
    配置来源: E:\\AiAgent\\crab-agent-core\\.env
    适合用于研究、搜索、浏览网页等场景
    """

    def __init__(self, model=None, api_key=None, base_url=None):
        cfg = _get_agent_config(model, api_key, base_url)
        self.model = cfg["model"]
        self.api_key = cfg["api_key"]
        self.base_url = cfg["base_url"]
        self.provider = cfg["provider"]

        self.agent = AIAgent(
            model=self.model,
            api_key=self.api_key,
            base_url=self.base_url,
            quiet_mode=True,
            enabled_toolsets=["web"],  # 仅启用 web 工具
            skip_memory=True,
            skip_context_files=True,
        )

    def research(self, query: str) -> str:
        """执行网络研究并返回结果"""
        return self.agent.chat(query)


class HermesSafeAgent:
    """
    禁用终端和浏览器的安全 Agent
    配置来源: E:\\AiAgent\\crab-agent-core\\.env
    适合共享环境或对外暴露的接口
    """

    def __init__(self, model=None, api_key=None, base_url=None):
        cfg = _get_agent_config(model, api_key, base_url)
        self.model = cfg["model"]
        self.api_key = cfg["api_key"]
        self.base_url = cfg["base_url"]
        self.provider = cfg["provider"]

        self.agent = AIAgent(
            model=self.model,
            api_key=self.api_key,
            base_url=self.base_url,
            quiet_mode=True,
            disabled_toolsets=["terminal", "browser"],  # 禁用高危工具
            skip_memory=True,
            skip_context_files=True,
        )

    def ask(self, question: str) -> str:
        """安全问答，不会执行本地命令或打开浏览器"""
        return self.agent.chat(question)


class HermesBatchProcessor:
    """
    Hermes 批量处理助手
    配置来源: E:\\AiAgent\\crab-agent-core\\.env
    使用线程池并发处理多个任务，每个任务独立的 AIAgent 实例
    """

    def __init__(self, model=None, api_key=None, base_url=None, max_workers=3):
        cfg = _get_agent_config(model, api_key, base_url)
        self.model = cfg["model"]
        self.api_key = cfg["api_key"]
        self.base_url = cfg["base_url"]
        self.provider = cfg["provider"]
        self.max_workers = max_workers

    def _process_single(self, prompt: str) -> dict:
        """单个任务处理（每个线程独立实例）"""
        agent = AIAgent(
            model=self.model,
            api_key=self.api_key,
            base_url=self.base_url,
            quiet_mode=True,
            skip_memory=True,
            skip_context_files=True,
        )
        try:
            response = agent.chat(prompt)
            return {"prompt": prompt, "status": "success", "response": response}
        except Exception as e:
            return {"prompt": prompt, "status": "error", "error": str(e)}

    def run(self, prompts: list[str]) -> list[dict]:
        """
        批量运行多个提示词

        Args:
            prompts: 提示词列表

        Returns:
            结果字典列表
        """
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            results = list(executor.map(self._process_single, prompts))
        return results


if __name__ == "__main__":
    print("=== Hermes Agent 工具集配置示例 ===")
    print("配置来源: E:\\AiAgent\\crab-agent-core\\.env")
    print("本演示展示如何配置不同的工具集和批量处理")
    print("-" * 50)

    try:
        # 先打印当前使用的服务配置
        print("\n[当前配置]")
        LLMConfig.print_config()

        # 1. 演示仅启用 web 工具的 Agent
        print("\n[1] Web 研究 Agent (仅启用 web 工具集)")
        web_agent = HermesWebAgent()
        query = "搜索 Python 3.13 的主要新特性并简要总结"
        print(f"用户: {query}")
        result = web_agent.research(query)
        print(f"Agent: {result[:300]}...")

        # 2. 演示安全 Agent
        print("\n[2] 安全 Agent (禁用 terminal 和 browser)")
        safe_agent = HermesSafeAgent()
        safe_result = safe_agent.ask("解释什么是快速排序算法")
        print(f"Agent: {safe_result[:300]}...")

        # 3. 演示批量处理
        print("\n[3] 批量处理 (并行处理多个提示词)")
        batch = HermesBatchProcessor(max_workers=2)
        prompts = [
            "用一句话解释递归",
            "用一句话解释哈希表",
            "用一句话解释动态规划",
        ]
        print(f"批量任务: {prompts}")
        batch_results = batch.run(prompts)
        for r in batch_results:
            status = "成功" if r["status"] == "success" else "失败"
            snippet = r.get("response", r.get("error", ""))[:100]
            print(f"  - [{status}] {r['prompt']}: {snippet}...")

    except ValueError as e:
        print(f"初始化失败: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"运行出错: {e}")
