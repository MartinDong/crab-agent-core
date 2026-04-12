"""
LangGraph 核心设计演示 - 智能任务助手（交互式版本）

这个文件展示了 LangGraph 的三个核心设计：
1. 显式的状态管理 - 使用复杂的 TypedDict 结构
2. Checkpointing - 支持检查点保存和恢复
3. 循环和条件路由 - ReAct 模式的循环执行 + 条件分支

与自动演示版本的区别：
- 交互式输入，用户可以自由提问
- 包含 resume_from_checkpoint() 方法展示检查点恢复功能

作者: Crab Agent Core Team
日期: 2026-04-12
"""

import os
import sys
import json
from typing import Annotated, TypedDict, Literal
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph.message import add_messages

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from skills import WeatherSkill
from color_utils import (
    Color,
    colored,
    print_colored,
    print_info,
    print_success,
    print_warning,
    print_error,
    print_header,
    print_section
)

load_dotenv()


class AgentState(TypedDict):
    """
    【LangGraph 核心设计 1：显式的状态管理】
    
    使用 TypedDict 定义复杂的状态结构，集中管理 Agent 的所有信息。
    
    字段说明：
    - messages: 消息历史记录，使用 Annotated 配合 add_messages 实现消息列表的合并
    - task_description: 用户输入的任务描述
    - task_status: 当前任务状态（pending/thinking/acting/reflecting/completed/failed）
    - thought_steps: 所有思考步骤的记录
    - actions_taken: 已执行的行动列表
    - observations: 观察结果（行动的输出）
    - max_iterations: 最大迭代次数限制
    - current_iteration: 当前迭代次数
    - final_answer: 最终答案
    """
    messages: Annotated[list, add_messages]
    task_description: str
    task_status: Literal["pending", "thinking", "acting", "reflecting", "completed", "failed"]
    thought_steps: list[str]
    actions_taken: list[dict]
    observations: list[str]
    max_iterations: int
    current_iteration: int
    final_answer: str


class SmartTaskAssistant:
    """
    智能任务助手类 - 完整体现 LangGraph 三个核心设计
    
    设计特点：
    1. 显式的状态管理：使用 TypedDict 定义复杂 State 结构
    2. Checkpointing：使用 MemorySaver 支持检查点
    3. 循环和条件路由：ReAct 模式的循环执行 + 条件分支
    
    工作流程（ReAct 模式）：
        think（思考） -> act（行动） -> reflect（反思）
            ^                          ↓
            └────────── 循环 ────────────┘
    """
    
    def __init__(self, model_name=os.getenv("OPENAI_MODEL_NAME")):
        """
        初始化智能任务助手
        
        参数：
            model_name: 使用的 LLM 模型名称，默认从 .env 的 OPENAI_MODEL_NAME 读取
        """
        self.llm = ChatOpenAI(
            model=model_name,
            temperature=0.0,
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_API_BASE")
        )
        
        self.weather_skill = WeatherSkill()
        
        self.checkpointer = MemorySaver()
        
        self.graph = self._build_graph()
    
    def _think_node(self, state: AgentState):
        """
        【思考节点】
        分析任务，决定下一步行动。
        
        这个节点体现了：
        - 使用 LLM 进行推理
        - 读取当前状态，决定下一步
        - 更新状态
        
        参数：
            state: 当前 Agent 状态
            
        返回：
            更新后的 Agent 状态
        """
        state["task_status"] = "thinking"
        state["current_iteration"] += 1
        
        print_section(f"迭代 {state['current_iteration']} - 思考阶段")
        
        system_prompt = """你是一个智能任务助手。你的任务是分析用户的问题，思考如何解决，并决定下一步行动。

请按照以下格式输出你的思考（JSON格式）：
{
    "thought": "你的思考过程",
    "action": "下一步行动类型，可选值：search | calculate | weather | complete | fail",
    "action_input": "行动的具体输入内容"
}

行动说明：
- search: 搜索信息
- calculate: 计算（格式：数学表达式，如 2+3*4）
- weather: 查询天气（格式：城市名，如 "北京"。用户问"明天""后天""预报"时，也只填城市名，工具会自动处理）
- complete: 任务完成，输出最终答案
- fail: 任务失败

注意：
1. 如果用户问的是天气相关问题，请直接使用 weather 行动
2. weather 的 action_input 只填纯净的城市名即可（如"邢台"，不要包含"明天""预报"等词）
3. 如果用户问"邢台明天天气"，action_input 应该是"邢台"，不是"邢台明天"
4. 获得天气数据后，使用 complete 行动总结天气信息给用户"""
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"任务描述：{state['task_description']}")
        ]
        
        if state["thought_steps"]:
            messages.append(AIMessage(content=f"之前的思考：{json.dumps(state['thought_steps'], ensure_ascii=False)}"))
        if state["actions_taken"]:
            messages.append(AIMessage(content=f"已执行的行动：{json.dumps(state['actions_taken'], ensure_ascii=False)}"))
        if state["observations"]:
            messages.append(AIMessage(content=f"观察结果：{json.dumps(state['observations'], ensure_ascii=False)}"))
        
        print_info("正在思考...")
        response = self.llm.invoke(messages)
        
        try:
            result = json.loads(response.content)
            thought = result.get("thought", "")
            action = result.get("action", "complete")
            action_input = result.get("action_input", "")
        except:
            thought = "无法解析思考结果"
            action = "complete"
            action_input = "抱歉，我无法完成这个任务"
        
        print_colored(f"思考结果: {thought}", Color.BRIGHT_CYAN)
        print_colored(f"决定行动: {action} - {action_input}", Color.BRIGHT_YELLOW)
        
        state["thought_steps"].append(thought)
        state["actions_taken"].append({
            "action": action,
            "input": action_input,
            "iteration": state["current_iteration"]
        })
        
        return state
    
    def _act_node(self, state: AgentState):
        """
        【行动节点】
        执行具体的操作（模拟工具调用）。
        
        这个节点体现了：
        - 工具集成（WeatherSkill）
        - 多种行动类型支持
        
        参数：
            state: 当前 Agent 状态
            
        返回：
            更新后的 Agent 状态
        """
        state["task_status"] = "acting"
        
        last_action = state["actions_taken"][-1]
        action = last_action["action"]
        action_input = last_action["input"]
        
        print_section(f"迭代 {state['current_iteration']} - 行动阶段")
        print_colored(f"执行行动: {action}", Color.BRIGHT_GREEN)
        
        observation = ""
        
        if action == "search":
            observation = f"[搜索结果] 关于 '{action_input}' 的信息：这是一个模拟的搜索结果，实际应用中会调用真实的搜索工具。"
        elif action == "calculate":
            try:
                result = eval(action_input)
                observation = f"[计算结果] {action_input} = {result}"
            except:
                observation = f"[计算错误] 无法计算: {action_input}"
        elif action == "weather":
            observation = self.weather_skill.execute(action_input)
        elif action == "complete":
            observation = f"[完成] 任务已完成：{action_input}"
        elif action == "fail":
            observation = f"[失败] 任务失败：{action_input}"
        
        print_colored(f"观察结果: {observation}", Color.BRIGHT_BLUE)
        
        state["observations"].append(observation)
        return state
    
    def _reflect_node(self, state: AgentState):
        """
        【反思节点】
        评估当前进展，决定是否继续循环。
        
        参数：
            state: 当前 Agent 状态
            
        返回：
            更新后的 Agent 状态
        """
        state["task_status"] = "reflecting"
        
        print_section(f"迭代 {state['current_iteration']} - 反思阶段")
        
        last_action = state["actions_taken"][-1]["action"]
        current_iter = state["current_iteration"]
        max_iter = state["max_iterations"]
        
        if last_action == "complete":
            state["final_answer"] = state["actions_taken"][-1]["input"]
            state["task_status"] = "completed"
            print_success("✓ 任务完成！")
        elif last_action == "fail":
            state["final_answer"] = state["actions_taken"][-1]["input"]
            state["task_status"] = "failed"
            print_error("✗ 任务失败")
        elif current_iter >= max_iter:
            state["final_answer"] = f"已达到最大迭代次数 {max_iter}，任务未完成。"
            state["task_status"] = "failed"
            print_warning(f"⚠ 已达到最大迭代次数 {max_iter}")
        else:
            print_info("→ 继续下一轮迭代...")
        
        return state
    
    def _router(self, state: AgentState) -> Literal["think", "end"]:
        """
        【LangGraph 核心设计 3：条件路由】
        根据当前状态决定下一步走向（继续思考或结束）。
        
        参数：
            state: 当前 Agent 状态
            
        返回：
            下一步节点名称："think" 或 "end"
        """
        if state["task_status"] in ["completed", "failed"]:
            return "end"
        else:
            return "think"
    
    def _build_graph(self):
        """
        构建 LangGraph 状态图
        
        图形结构：
            START -> think -> act -> reflect
                                    ↓
                              (条件路由)
                              ↙       ↘
                           think      END
        """
        graph_builder = StateGraph(AgentState)
        
        graph_builder.add_node("think", self._think_node)
        graph_builder.add_node("act", self._act_node)
        graph_builder.add_node("reflect", self._reflect_node)
        
        graph_builder.add_edge(START, "think")
        graph_builder.add_edge("think", "act")
        graph_builder.add_edge("act", "reflect")
        
        graph_builder.add_conditional_edges(
            "reflect",
            self._router,
            {
                "think": "think",
                "end": END
            }
        )
        
        return graph_builder.compile(checkpointer=self.checkpointer)
    
    def run_task(self, task_description: str, max_iterations: int = 5, thread_id: str = "default"):
        """
        执行任务
        
        参数：
            task_description: 任务描述
            max_iterations: 最大迭代次数
            thread_id: 线程 ID（用于 Checkpointing，每个任务一个独立 ID）
            
        返回：
            最终的 Agent 状态
        """
        initial_state: AgentState = {
            "messages": [],
            "task_description": task_description,
            "task_status": "pending",
            "thought_steps": [],
            "actions_taken": [],
            "observations": [],
            "max_iterations": max_iterations,
            "current_iteration": 0,
            "final_answer": ""
        }
        
        config = {"configurable": {"thread_id": thread_id}}
        
        result = self.graph.invoke(initial_state, config)
        return result
    
    def resume_from_checkpoint(self, thread_id: str = "default"):
        """
        【Checkpointing 演示】
        从检查点恢复执行。
        
        这个方法展示了 LangGraph 的第二个核心设计：Checkpointing。
        可以从之前中断的地方继续执行任务。
        
        参数：
            thread_id: 线程 ID，与 run_task() 中使用的一致
            
        返回：
            最终的 Agent 状态（如果有检查点），否则 None
        """
        config = {"configurable": {"thread_id": thread_id}}
        
        state = self.graph.get_state(config)
        
        if state.values:
            result = self.graph.invoke(None, config)
            return result
        
        return None


def print_state_summary(result):
    """
    打印状态摘要（最终结果展示）
    
    参数：
        result: 最终的 Agent 状态
    """
    print_header("状态摘要")
    print_colored(f"任务描述: {result['task_description']}", Color.WHITE)
    print_colored(f"任务状态: {result['task_status']}", Color.BRIGHT_MAGENTA)
    print_colored(f"迭代次数: {result['current_iteration']}/{result['max_iterations']}", Color.BRIGHT_CYAN)
    print_colored(f"\n最终答案: {result['final_answer']}", Color.BOLD + Color.BRIGHT_GREEN)
    print_header("详细执行过程", char="-")
    
    for i in range(len(result['thought_steps'])):
        print_section(f"迭代 {i+1}")
        print_colored(f"思考: {result['thought_steps'][i]}", Color.BRIGHT_CYAN)
        print_colored(f"行动: {json.dumps(result['actions_taken'][i], ensure_ascii=False)}", Color.BRIGHT_YELLOW)
        if i < len(result['observations']):
            print_colored(f"观察: {result['observations'][i]}", Color.BRIGHT_BLUE)


if __name__ == "__main__":
    assistant = SmartTaskAssistant()
    
    print_header("LangGraph 核心设计 Demo - 智能任务助手")
    print_colored("\n这个 Demo 体现了 LangGraph 的三个核心设计：", Color.WHITE)
    print_colored("1. 显式的状态管理 - 使用复杂的 TypedDict 结构", Color.CYAN)
    print_colored("2. Checkpointing - 支持检查点保存和恢复", Color.CYAN)
    print_colored("3. 循环和条件路由 - ReAct 模式的循环执行 + 条件分支", Color.CYAN)
    
    task = input(colored("\n请输入你的任务（例如：计算 2+3*4，或者 搜索 LangGraph 的核心概念）: ", Color.BOLD + Color.YELLOW))
    
    print_header(f"开始执行任务: {task}")
    
    result = assistant.run_task(task, max_iterations=5, thread_id="task_001")
    
    print_header("任务执行完毕")
    print_colored(f"\n任务描述: {result['task_description']}", Color.WHITE)
    print_colored(f"任务状态: {result['task_status']}", Color.BRIGHT_MAGENTA)
    print_colored(f"迭代次数: {result['current_iteration']}/{result['max_iterations']}", Color.BRIGHT_CYAN)
    print_colored(f"\n最终答案: {result['final_answer']}", Color.BOLD + Color.BRIGHT_GREEN)
