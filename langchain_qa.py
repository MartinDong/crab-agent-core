import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

class LangChainQA:
    def __init__(self, model_name=os.getenv("OPENAI_MODEL_NAME")):
        self.llm = ChatOpenAI(
            model=model_name,
            temperature=0,
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_API_BASE")
        )
        
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "你是一个智能问答助手，请用简洁明了的方式回答用户的问题。"),
            ("human", "{question}")
        ])
        
        self.chain = self.prompt | self.llm | StrOutputParser()
    
    def ask(self, question: str) -> str:
        return self.chain.invoke({"question": question})

if __name__ == "__main__":
    qa = LangChainQA()
    
    print("=== LangChain 问答系统 ===")
    print("输入 'quit' 退出")
    print("-" * 30)
    
    while True:
        question = input("\n请输入问题: ")
        if question.lower() in ["quit", "exit", "退出"]:
            break
        answer = qa.ask(question)
        print(f"\n回答: {answer}")
