from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

prompts = [
    "Explain LangChain in simple terms.",
    "What is a Retriever in LangChain?",
    "Why is LangSmith useful?"
]

for p in prompts:
    response = llm.invoke(p)

    print("\nPrompt:", p)
    print("Answer:", response.content)
