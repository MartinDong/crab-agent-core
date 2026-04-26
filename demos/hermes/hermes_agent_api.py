import os
import sys
from dotenv import load_dotenv

# 确保能加载项目根目录的 .env
# 文件路径: e:\AiAgent\crab-agent-core\demos\hermes\hermes_agent_api.py
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

# FastAPI 为可选依赖，本文件主要用于展示代码结构
try:
    from fastapi import FastAPI
    from pydantic import BaseModel
    FASTAPI_AVAILABLE = True
except ImportError:
    FASTAPI_AVAILABLE = False
    print("提示: 安装 fastapi 和 uvicorn 后可运行本服务")
    print("  pip install fastapi uvicorn")


def _get_chat_request_defaults():
    """获取 ChatRequest 的默认模型配置"""
    try:
        cfg = LLMConfig.get_active_config()
        return cfg["model"]
    except ValueError:
        return "deepseek-v3.1-250821"


_DEFAULT_MODEL = _get_chat_request_defaults()


class ChatRequest(BaseModel):
    """聊天请求模型"""
    message: str
    model: str = _DEFAULT_MODEL


class HermesAPI:
    """
    基于 Hermes AIAgent 的 API 服务封装
    每次请求创建新的 Agent 实例，确保线程安全
    配置来源: E:\\AiAgent\\crab-agent-core\\.env
    """

    def __init__(self):
        cfg = LLMConfig.get_active_config()
        self.api_key = cfg["api_key"]
        self.base_url = cfg["base_url"]
        self.default_model = cfg["model"]
        self.provider = cfg["provider"]

    def chat(self, message: str, model: str = None) -> dict:
        """
        处理单次聊天请求

        Args:
            message: 用户消息
            model: 模型名称，默认使用 .env 中的模型

        Returns:
            包含 response 的字典
        """
        agent = AIAgent(
            model=model or self.default_model,
            api_key=self.api_key,
            base_url=self.base_url,
            quiet_mode=True,
            skip_memory=True,         # API 服务建议禁用持久记忆
            skip_context_files=True,  # 禁用 AGENTS.md 加载
            disabled_toolsets=["terminal"],  # API 环境禁用终端
        )
        response = agent.chat(message)
        return {"response": response}


def create_app() -> "FastAPI":
    """创建 FastAPI 应用实例"""
    if not FASTAPI_AVAILABLE:
        raise RuntimeError("FastAPI 未安装，请执行: pip install fastapi uvicorn")

    app = FastAPI(title="Hermes Agent API", version="1.0.0")
    service = HermesAPI()

    @app.post("/chat")
    async def chat_endpoint(request: ChatRequest):
        """聊天端点 - 接收消息并返回 AI 回复"""
        result = service.chat(request.message, request.model)
        return result

    @app.get("/health")
    async def health_check():
        """健康检查端点"""
        return {"status": "ok", "provider": service.provider}

    return app


if __name__ == "__main__":
    print("=== Hermes Agent FastAPI 服务示例 ===")
    print("配置来源: E:\\AiAgent\\crab-agent-core\\.env")
    print("运行方式: uvicorn demos.hermes_agent_api:app --reload")
    print("请求示例:")
    print('  curl -X POST http://localhost:8000/chat \\')
    print('    -H "Content-Type: application/json" \\')
    print('    -d \'{"message": "介绍一下自己"}\'')
    print("-" * 50)

    try:
        service = HermesAPI()
        print(f"\n[当前配置] 提供商: {service.provider} | 模型: {service.default_model}")
    except ValueError as e:
        print(e)
        sys.exit(1)

    if FASTAPI_AVAILABLE:
        import uvicorn
        app = create_app()
        print("正在启动服务...")
        uvicorn.run(app, host="0.0.0.0", port=8000)
    else:
        print("\nFastAPI 未安装，以下是模拟演示:")
        demo_msg = "用三句话介绍你自己"
        print(f"\n用户: {demo_msg}")
        try:
            result = service.chat(demo_msg)
            print(f"服务响应: {result}")
        except Exception as e:
            print(f"调用失败: {e}")
