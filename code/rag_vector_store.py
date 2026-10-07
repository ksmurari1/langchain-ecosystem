from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

loader = TextLoader("../data/sample_rag.txt")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=60,
    chunk_overlap=10
)
chunks = splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vector_store = InMemoryVectorStore(embedding=embeddings)
vector_store.add_documents(chunks)

query = "How can LangChain help build AI applications?"
results = vector_store.similarity_search(query, k=2)

print("Documents:", len(documents))
print("Chunks:", len(chunks))

print("\nTop results:")
for i, result in enumerate(results, start=1):
    print(f"{i}. {result.page_content}")
