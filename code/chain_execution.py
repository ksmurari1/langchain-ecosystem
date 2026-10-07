from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

texts = [
    "LangChain helps build AI applications.",
    "Python is a popular programming language.",
    "Dogs are friendly animals.",
    "Cars are useful for transportation."
]

vector_store = InMemoryVectorStore(embedding=embeddings)
vector_store.add_texts(texts)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)

prompt = ChatPromptTemplate.from_template("""
Answer the question using only the context provided.

Context:
{context}

Question:
{question}
""")

llm = ChatOpenAI(model="gpt-4o-mini")
chain = prompt | llm

question = "How can I build an AI application?"
documents = retriever.invoke(question)

context = "\n".join(
    document.page_content for document in documents
)

response = chain.invoke({
    "context": context,
    "question": question
})

print("Question:", question)
print("\nAnswer:", response.content)
