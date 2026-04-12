
"""
LangGraph 核心设计演示 - 智能任务助手（自动演示版本）

这个文件展示了 LangGraph 的三个核心设计：
1. 显式的状态管理 - 使用复杂的 TypedDict 结构
2. Checkpointing - 支持检查点保存和恢复
3. 循环和条件路由 - ReAct 模式的循环执行 + 条件分支

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
    
    工作流程（ReAct 模式）：
        think（思考） -&gt; act（行动） -&gt; reflect（反思）
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
            temperature=0.7,
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
        
        print(f"\n{'─'*80}")
        print(f"迭代 {state['current_iteration']} - 思考阶段".center(80))
        print(f"{'─'*80}")
        
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
- weather: 查询天气（格式：城市名，如 北京）
- complete: 任务完成，输出最终答案
- fail: 任务失败

注意：如果用户问的是天气相关问题，请直接使用 weather 行动。"""
        
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
        
        print("正在思考...")
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
        
        print(f"思考结果: {thought}")
        print(f"决定行动: {action} - {action_input}")
        
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
        
        print(f"\n{'─'*80}")
        print(f"迭代 {state['current_iteration']} - 行动阶段".center(80))
        print(f"{'─'*80}")
        print(f"执行行动: {action}")
        
        observation = ""
        
        if action == "search":
            observation = f"[搜索结果] 关于 '{action_input}' 的信息：LangGraph 是 LangChain 的一个扩展库，用于构建具有状态管理和循环能力的 Agent 应用。它的三个核心设计是：显式的状态管理、Checkpointing 机制、原生的循环和条件路由支持。"
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
        
        print(f"观察结果: {observation}")
        
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
        
        print(f"\n{'─'*80}")
        print(f"迭代 {state['current_iteration']} - 反思阶段".center(80))
        print(f"{'─'*80}")
        
        last_action = state["actions_taken"][-1]["action"]
        current_iter = state["current_iteration"]
        max_iter = state["max_iterations"]
        
        if last_action == "complete":
            state["final_answer"] = state["actions_taken"][-1]["input"]
            state["task_status"] = "completed"
            print("✓ 任务完成！")
        elif last_action == "fail":
            state["final_answer"] = state["actions_taken"][-1]["input"]
            state["task_status"] = "failed"
            print("✗ 任务失败")
        elif current_iter &gt;= max_iter:
            state["final_answer"] = f"已达到最大迭代次数 {max_iter}，任务未完成。"
            state["task_status"] = "failed"
            print(f"⚠ 已达到最大迭代次数 {max_iter}")
        else:
            print("→ 继续下一轮迭代...")
        
        return state
    
    def _router(self, state: AgentState) -&gt; Literal["think", "end"]:
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
            START -&gt; think -&gt; act -&gt; reflect
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


def print_state_summary(result):
    """
    打印状态摘要（最终结果展示）
    
    参数：
        result: 最终的 Agent 状态
    """
    print("\n" + "="*80)
    print("状态摘要".center(80))
    print("="*80)
    print(f"任务描述: {result['task_description']}")
    print(f"任务状态: {result['task_status']}")
    print(f"迭代次数: {result['current_iteration']}/{result['max_iterations']}")
    print(f"\n最终答案: {result['final_answer']}")
    print("\n" + "="*80)
    print("详细执行过程".center(80))
    print("="*80)
    
    for i in range(len(result['thought_steps'])):
        print(f"\n{'─'*80}")
        print(f"迭代 {i+1}".center(80))
        print(f"{'─'*80}")
        print(f"思考: {result['thought_steps'][i]}")
        print(f"行动: {json.dumps(result['actions_taken'][i], ensure_ascii=False, indent=2)}")
        if i &lt; len(result['observations']):
            print(f"观察: {result['observations'][i]}")


if __name__ == "__main__":
    assistant = SmartTaskAssistant()
    
    print("="*80)
    print("LangGraph 核心设计 Demo - 智能任务助手".center(80))
    print("="*80)
    print("\n这个 Demo 体现了 LangGraph 的三个核心设计：")
    print("1. 显式的状态管理 - 使用复杂的 TypedDict 结构")
    print("2. Checkpointing - 支持检查点保存和恢复")
    print("3. 循环和条件路由 - ReAct 模式的循环执行 + 条件分支")
    print("="*80)
    
    print("\n" + "="*80)
    print("[演示 1] 计算任务：2+3*4".center(80))
    print("="*80)
    result1 = assistant.run_task("计算 2+3*4", max_iterations=5, thread_id="task_calc")
    print("\n" + "="*80)
    print("演示 1 执行完毕".center(80))
    print("="*80)
    print(f"\n任务描述: {result1['task_description']}")
    print(f"任务状态: {result1['task_status']}")
    print(f"迭代次数: {result1['current_iteration']}/{result1['max_iterations']}")
    print(f"\n最终答案: {result1['final_answer']}")
    
    print("\n\n" + "="*80)
    print("[演示 2] 天气查询：北京的天气".center(80))
    print("="*80)
    result2 = assistant.run_task("查询北京的天气", max_iterations=5, thread_id="task_weather")
    print("\n" + "="*80)
    print("演示 2 执行完毕".center(80))
    print("="*80)
    print(f"\n任务描述: {result2['task_description']}")
    print(f"任务状态: {result2['task_status']}")
    print(f"迭代次数: {result2['current_iteration']}/{result2['max_iterations']}")
    print(f"\n最终答案: {result2['final_answer']}")
    
    print("\n\n" + "="*80)
    print("[演示 3] 搜索任务：了解 LangGraph 的核心概念".center(80))
    print("="*80)
    result3 = assistant.run_task("搜索 LangGraph 的核心概念", max_iterations=5, thread_id="task_search")
    print("\n" + "="*80)
    print("演示 3 执行完毕".center(80))
    print("="*80)
    print(f"\n任务描述: {result3['task_description']}")
    print(f"任务状态: {result3['task_status']}")
    print(f"迭代次数: {result3['current_iteration']}/{result3['max_iterations']}")
    print(f"\n最终答案: {result3['final_answer']}")

