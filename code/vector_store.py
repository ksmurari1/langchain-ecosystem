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

results = vector_store.similarity_search(
    "How can I build an AI application?",
    k=2
)

for result in results:
    print(result.page_content)
