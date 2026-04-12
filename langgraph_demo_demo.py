import os
import json
from typing import Annotated, TypedDict, Literal
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph.message import add_messages

load_dotenv()

class AgentState(TypedDict):
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
    def __init__(self, model_name=os.getenv("OPENAI_MODEL_NAME")):
        self.llm = ChatOpenAI(
            model=model_name,
            temperature=0.7,
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_API_BASE")
        )
        
        self.checkpointer = MemorySaver()
        self.graph = self._build_graph()
    
    def _think_node(self, state: AgentState):
        state["task_status"] = "thinking"
        state["current_iteration"] += 1
        
        print(f"\n{'─'*80}")
        print(f"迭代 {state['current_iteration']} - 思考阶段".center(80))
        print(f"{'─'*80}")
        
        system_prompt = """你是一个智能任务助手。你的任务是分析用户的问题，思考如何解决，并决定下一步行动。

请按照以下格式输出你的思考（JSON格式）：
{
    "thought": "你的思考过程",
    "action": "下一步行动类型，可选值：search | calculate | complete | fail",
    "action_input": "行动的具体输入内容"
}

行动说明：
- search: 搜索信息
- calculate: 计算
- complete: 任务完成，输出最终答案
- fail: 任务失败
"""
        
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
        elif action == "complete":
            observation = f"[完成] 任务已完成：{action_input}"
        elif action == "fail":
            observation = f"[失败] 任务失败：{action_input}"
        
        print(f"观察结果: {observation}")
        
        state["observations"].append(observation)
        return state
    
    def _reflect_node(self, state: AgentState):
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
        elif current_iter >= max_iter:
            state["final_answer"] = f"已达到最大迭代次数 {max_iter}，任务未完成。"
            state["task_status"] = "failed"
            print(f"⚠ 已达到最大迭代次数 {max_iter}")
        else:
            print("→ 继续下一轮迭代...")
        
        return state
    
    def _router(self, state: AgentState) -> Literal["think", "end"]:
        if state["task_status"] in ["completed", "failed"]:
            return "end"
        else:
            return "think"
    
    def _build_graph(self):
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
        if i < len(result['observations']):
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
    print("[演示 2] 搜索任务：了解 LangGraph 的核心概念".center(80))
    print("="*80)
    result2 = assistant.run_task("搜索 LangGraph 的核心概念", max_iterations=5, thread_id="task_search")
    print("\n" + "="*80)
    print("演示 2 执行完毕".center(80))
    print("="*80)
    print(f"\n任务描述: {result2['task_description']}")
    print(f"任务状态: {result2['task_status']}")
    print(f"迭代次数: {result2['current_iteration']}/{result2['max_iterations']}")
    print(f"\n最终答案: {result2['final_answer']}")
