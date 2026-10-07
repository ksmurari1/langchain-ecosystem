from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

text = "I love programming in Python."

vector = embeddings.embed_query(text)

print("Vector size:", len(vector))
print("First 5 values:", vector[:5])