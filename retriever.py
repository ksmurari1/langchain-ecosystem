from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings


# 1. Create embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


# 2. Sample documents
texts = [
    "LangChain helps build AI applications.",
    "Python is a popular programming language.",
    "Dogs are friendly animals.",
    "Cars are useful for transportation."
]


# 3. Create Vector Store
vector_store = InMemoryVectorStore(
    embedding=embeddings
)


# 4. Add documents to Vector Store
vector_store.add_texts(texts)


# 5. Create Retriever from Vector Store
retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)


# 6. Ask Retriever for relevant documents
query = "How can I build an AI application?"

results = retriever.invoke(query)


# 7. Display retrieved documents
print("Query:", query)
print("\nRetrieved Documents:")

for i, result in enumerate(results):
    print(f"\nResult {i + 1}:")
    print(result.page_content)