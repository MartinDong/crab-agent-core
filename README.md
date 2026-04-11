# 问答系统演示

基于 LangChain 和 LangGraph 的精简版问答系统

## 安装依赖

```bash
pip install -r requirements.txt
```

## 配置

复制 `.env.example` 为 `.env` 并填入你的 OpenAI API 配置：

```bash
cp .env.example .env
```

编辑 `.env` 文件：

```
OPENAI_API_KEY=你的API密钥
OPENAI_API_BASE=https://api.openai.com/v1
```

## 运行

### LangChain 版本

简单的问答系统，无历史记录：

```bash
python langchain_qa.py
```

### LangGraph 版本

带对话历史记录的问答系统：

```bash
python langgraph_qa.py
```

## 文件说明

- `langchain_qa.py` - LangChain 版本（链式调用）
- `langgraph_qa.py` - LangGraph 版本（状态图 + 历史记录）
- `requirements.txt` - 项目依赖
