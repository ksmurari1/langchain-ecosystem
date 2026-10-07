from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings

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

query = "How can I build an AI application?"
results = retriever.invoke(query)

print("Query:", query)
print("\nRetrieved Documents:")

for i, result in enumerate(results, start=1):
    print(f"\nResult {i}:")
    print(result.page_content)
