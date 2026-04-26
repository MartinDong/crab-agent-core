# 问答系统演示

基于 LangChain、LangGraph 和 Hermes Agent 的精简版问答系统

## 安装依赖

```bash
pip install -r requirements.txt
```

## 配置

复制 `.env.example` 为 `.env` 并填入你的 LLM API 配置：

```bash
cp .env.example .env
```

编辑 `.env` 文件，支持两种配置方式：

**方式一：OpenAI 兼容 API**
```
OPENAI_API_KEY=sk-xxx
OPENAI_API_BASE=https://api.openai.com/v1
OPENAI_MODEL_NAME=deepseek-v3.1-250821
```

**方式二：百度千帆**
```
QIANFAN_API_KEY=bce-v3/...
QIANFAN_API_BASE=https://qianfan.baidubce.com
OPENAI_MODEL_NAME=deepseek-v3.1-250821
```

> 注：所有 Hermes Agent 示例都通过 `demos/config.py` 统一读取 `.env` 中的配置，无需在代码中手动传入。

## 运行

### LangChain 版本

简单的问答系统，无历史记录：

```bash
python demos/langchain_qa.py
```

### LangGraph 版本

带对话历史记录的问答系统：

```bash
python demos/langgraph_qa.py
```

### Hermes Agent 版本

基于 Hermes Python 库的 Agent 应用，支持工具调用、多轮对话和批量处理：

```bash
# 检查当前配置（会打印使用的服务商和模型）
python demos/config.py

# 基础问答（简单 chat 方法）
python demos/hermes_agent_basic.py

# 多轮对话（完整对话控制）
python demos/hermes_agent_conversation.py

# 工具集配置与批量处理
python demos/hermes_agent_tools.py

# FastAPI 服务（需先安装 fastapi）
pip install fastapi uvicorn
uvicorn demos.hermes_agent_api:app --reload
```

## 文件说明

- `demos/config.py` - 统一配置管理（读取 `.env`中的 LLM 服务配置）
- `demos/langchain_qa.py` - LangChain 版本（链式调用）
- `demos/langgraph_qa.py` - LangGraph 版本（状态图 + 历史记录）
- `demos/hermes_agent_basic.py` - Hermes Agent 基础问答
- `demos/hermes_agent_conversation.py` - Hermes Agent 多轮对话
- `demos/hermes_agent_tools.py` - Hermes Agent 工具集与批量处理
- `demos/hermes_agent_api.py` - Hermes Agent FastAPI 集成
- `requirements.txt` - 项目依赖
