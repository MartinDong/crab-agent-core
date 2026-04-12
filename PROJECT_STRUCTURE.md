
# 项目结构说明

## 目录结构

```
crab-agent-core/
├── .trae/                    # Trae IDE 配置目录
│   └── skills/               # Trae IDE Skill 配置
│       └── weather-skill/    # 天气查询 Skill
│           └── SKILL.md
├── demos/                    # 演示文件目录
│   ├── langchain_qa.py       # LangChain 问答示例
│   ├── langgraph_qa.py       # LangGraph 问答示例
│   ├── langgraph_core_demo.py  # LangGraph 核心设计交互式演示
│   └── langgraph_demo_demo.py # LangGraph 核心设计自动演示
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
```

