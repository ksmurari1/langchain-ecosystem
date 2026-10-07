from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

text = "I love programming in Python."
vector = embeddings.embed_query(text)

print("Vector size:", len(vector))
print("First 5 values:", vector[:5])
