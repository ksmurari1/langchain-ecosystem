from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore


# 1. DATA INGESTION
# Create a small text file first:
# sample_rag.txt

loader = TextLoader("sample_rag.txt")
documents = loader.load()

print("\n=== 1. DOCUMENT ===")
print(documents[0].page_content)
print("Metadata:", documents[0].metadata)


# 2. TEXT SPLITTER
splitter = RecursiveCharacterTextSplitter(
    chunk_size=60,
    chunk_overlap=10
)

chunks = splitter.split_documents(documents)

print("\n=== 2. CHUNKS ===")
print("Total chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i + 1}:")
    print(chunk.page_content)


# 3. EMBEDDINGS
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

print("\n=== 3. EMBEDDINGS ===")

for i, chunk in enumerate(chunks):
    vector = embeddings.embed_query(chunk.page_content)

    print(f"Chunk {i + 1} vector size:", len(vector))
    print("First 5 values:", vector[:5])


# 4. VECTOR STORE
vector_store = InMemoryVectorStore(
    embedding=embeddings
)

vector_store.add_documents(chunks)

print("\n=== 4. VECTOR STORE ===")
print("Chunks successfully stored as vectors.")


# 5. SEARCH
query = "How can I build an AI application?"

results = vector_store.similarity_search(
    query,
    k=2
)

print("\n=== 5. SEARCH RESULTS ===")

for i, result in enumerate(results):
    print(f"\nResult {i + 1}:")
    print(result.page_content)