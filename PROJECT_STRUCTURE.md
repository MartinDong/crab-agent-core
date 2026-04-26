
# 项目结构说明

## 目录结构

```
crab-agent-core/
├── .trae/                    # Trae IDE 配置目录
│   └── skills/               # Trae IDE Skill 配置
│       └── weather-skill/    # 天气查询 Skill
│           └── SKILL.md
├── demos/                    # 演示文件目录
│   ├── config.py                 # 统一配置管理（读取 .env 中的 LLM 服务配置）
│   ├── langchain_qa.py           # LangChain 问答示例
│   ├── langgraph_qa.py           # LangGraph 问答示例
│   ├── langgraph_core_demo.py    # LangGraph 核心设计交互式演示
│   ├── langgraph_demo_demo.py    # LangGraph 核心设计自动演示
│   ├── hermes_agent_basic.py      # Hermes Agent 基础 chat 用法
│   ├── hermes_agent_conversation.py # Hermes Agent 多轮对话与完整控制
│   ├── hermes_agent_tools.py      # Hermes Agent 工具集配置与批量处理
│   └── hermes_agent_api.py        # Hermes Agent FastAPI 服务集成示例
├── skills/                   # 可复用 Skill 模块
│   ├── __init__.py
│   └── weather.py            # 天气查询 Skill
├── tests/                    # 测试文件目录
│   └── test_skill.py         # Skill 测试脚本
├── .env.example              # 环境变量示例
├── .gitignore
├── README.md                 # 项目说明
├── PROJECT_STRUCTURE.md      # 本文件 - 项目结构说明
└── requirements.txt          # 项目依赖
```

## 目录说明

### `.trae/`
- **用途**: Trae IDE 的配置目录
- **规范**: 存放 Trae IDE 相关的 Skill 配置

### `demos/`
- **用途**: 存放所有演示和示例代码
- **规范**: 
  - 所有以 `_demo.py` 或 `_qa.py` 结尾的文件
  - 按功能分类存放
  - 命名清晰，明确展示功能

**Hermes Agent 示例** (`hermes_agent_*.py`)
- `hermes_agent_basic.py` - 基础使用，展示 `chat()` 方法快速获取回复
- `hermes_agent_conversation.py` - 多轮对话，展示 `run_conversation()` 、历史记忆、轨迹保存
- `hermes_agent_tools.py` - 工具集配置（enabled_toolsets / disabled_toolsets）与批量处理
- `hermes_agent_api.py` - FastAPI 集成示例，展示如何在 Web 服务中嵌入 Hermes

### `skills/`
- **用途**: 可复用的 Skill 模块
- **规范**:
  - 每个 Skill 一个模块文件或子目录
  - 提供统一的 `execute()` 接口
  - 在 `__init__.py` 中导出
  - 参考 `WeatherSkill` 的实现模式

### `tests/`
- **用途**: 测试脚本和单元测试
- **规范**:
  - 测试文件以 `test_` 开头
  - 可以快速验证功能是否正常

## 文件迁移规则

1. **演示文件** → `demos/`
   - `langchain_qa.py`
   - `langgraph_qa.py`
   - `langgraph_core_demo.py`
   - `langgraph_demo_demo.py`

2. **测试文件** → `tests/`
   - `test_skill.py`

3. **Skill 模块** → `skills/`（已在正确位置）
   - `__init__.py`
   - `weather.py`

## 引用路径更新

由于文件位置变更，需要更新相关引用：
- 从 `demos/` 导入 `skills` 时路径不变（Python 包搜索机制）
- 运行 demo 时从 `demos/` 目录执行

## 运行方式

```bash
# 运行演示
python demos/langgraph_demo_demo.py

# 运行交互式演示
python demos/langgraph_core_demo.py

# 运行测试
python tests/test_skill.py

# Hermes Agent 示例
python demos/hermes_agent_basic.py         # 基础问答
python demos/hermes_agent_conversation.py   # 多轮对话
python demos/hermes_agent_tools.py          # 工具集与批量处理

# Hermes Agent API 服务（需先安装 fastapi）
pip install fastapi uvicorn
uvicorn demos.hermes_agent_api:app --reload
```

