from langchain_huggingface import HuggingFaceEmbeddings
import numpy as np

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

text1 = "I like dogs"
text2 = "I love puppies"
text3 = "The car is fast"

v1 = embeddings.embed_query(text1)
v2 = embeddings.embed_query(text2)
v3 = embeddings.embed_query(text3)


def similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )


print("Dogs vs Puppies:", round(similarity(v1, v2), 2))
print("Dogs vs Car:", round(similarity(v1, v3), 2))
print("Puppies vs Car:", round(similarity(v2, v3), 2))