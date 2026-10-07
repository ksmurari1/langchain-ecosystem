from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

texts = [
    "Dogs are friendly animals.",
    "Puppies are young dogs.",
    "Cars are useful for transportation."
]

vectors = [embeddings.embed_query(text) for text in texts]

# The example demonstrates that semantically related text
# tends to have a higher cosine similarity.
from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity([vectors[0]], [vectors[1]])[0][0]
print("Dogs vs Puppies similarity:", round(float(similarity), 2))
