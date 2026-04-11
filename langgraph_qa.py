import os
from dotenv import load_dotenv
from typing import Annotated, TypedDict
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

load_dotenv()

class State(TypedDict):
    messages: Annotated[list, add_messages]

class LangGraphQA:
    def __init__(self, model_name=os.getenv("OPENAI_MODEL_NAME")):
        self.llm = ChatOpenAI(
            model=model_name,
            temperature=0,
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_API_BASE")
        )
        
        self.graph = self._build_graph()
    
    def _chatbot(self, state: State):
        response = self.llm.invoke(state["messages"])
        return {"messages": [response]}
    
    def _build_graph(self):
        graph_builder = StateGraph(State)
        graph_builder.add_node("chatbot", self._chatbot)
        graph_builder.add_edge(START, "chatbot")
        graph_builder.add_edge("chatbot", END)
        return graph_builder.compile()
    
    def ask(self, question: str, history: list = None) -> tuple[str, list]:
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
