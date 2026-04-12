import os
from dotenv import load_dotenv
from typing import Annotated, TypedDict
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

load_dotenv()

class State(TypedDict):
    """
    状态类型定义
    使用 TypedDict 定义图中流转的状态结构
    add_messages 是一个 reducer 函数，用于合并消息列表
    """
    messages: Annotated[list, add_messages]

class LangGraphQA:
    """
    基于 LangGraph 的问答系统
    使用状态图 (StateGraph) 实现带历史记录的多轮对话
    """
    
    def __init__(self, model_name=os.getenv("OPENAI_MODEL_NAME")):
        """
        初始化问答系统并构建状态图
        
        Args:
            model_name: 使用的模型名称，从环境变量读取
        """
        self.llm = ChatOpenAI(
            model=model_name,
            temperature=0,
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_API_BASE")
        )
        
        self.graph = self._build_graph()
    
    def _chatbot(self, state: State):
        """
        聊天机器人节点函数
        接收当前状态，调用 LLM 生成回复，返回更新后的状态
        
        Args:
            state: 当前状态，包含消息历史
            
        Returns:
            包含新 AI 消息的状态更新
        """
        response = self.llm.invoke(state["messages"])
        return {"messages": [response]}
    
    def _build_graph(self):
        """
        构建 LangGraph 状态图
        
        图结构:
        START -> chatbot -> END
        
        Returns:
            编译后的状态图
        """
        graph_builder = StateGraph(State)
        graph_builder.add_node("chatbot", self._chatbot)
        graph_builder.add_edge(START, "chatbot")
        graph_builder.add_edge("chatbot", END)
        return graph_builder.compile()
    
    def ask(self, question: str, history: list = None) -> tuple[str, list]:
        """
        发送问题并获取回答，同时维护对话历史
        
        Args:
            question: 用户的问题
            history: 历史消息列表，默认为 None（空历史）
            
        Returns:
            (回答文本, 更新后的历史消息列表)
        """
        if history is None:
            history = []
        
        messages = history + [HumanMessage(content=question)]
        result = self.graph.invoke({"messages": messages})
        ai_message = result["messages"][-1]
        
        updated_history = messages + [ai_message]
        return ai_message.content, updated_history

if __name__ == "__main__":
    qa = LangGraphQA()
    history = []
    
    print("=== LangGraph 问答系统 (带历史记录) ===")
    print("输入 'quit' 退出，'clear' 清空历史")
    print("-" * 40)
    
    while True:
        question = input("\n请输入问题: ")
        
        if question.lower() in ["quit", "exit", "退出"]:
            break
        if question.lower() in ["clear", "清空"]:
            history = []
            print("历史记录已清空")
            continue
        
        answer, history = qa.ask(question, history)
        print(f"\n回答: {answer}")
