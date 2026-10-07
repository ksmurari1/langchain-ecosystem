from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


# ============================================================
# 1. EMBEDDINGS
# ============================================================

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


# ============================================================
# 2. VECTOR STORE
# ============================================================

texts = [
    "LangChain helps build AI applications.",
    "Python is a popular programming language.",
    "Dogs are friendly animals.",
    "Cars are useful for transportation."
]

vector_store = InMemoryVectorStore(
    embedding=embeddings
)

vector_store.add_texts(texts)


# ============================================================
# 3. RETRIEVER
# ============================================================

retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)


# ============================================================
# 4. PROMPT
# ============================================================

prompt = ChatPromptTemplate.from_template(
    """
Answer the question using only the context provided.

Context:
{context}

Question:
{question}
"""
)


# ============================================================
# 5. LLM
# ============================================================

llm = ChatOpenAI(
    model="gpt-4o-mini"
)


# ============================================================
# 6. CHAIN
# ============================================================

# This creates the Chain:
# Prompt → LLM

chain = prompt | llm


# ============================================================
# 7. USER QUESTION
# ============================================================

question = "How can I build an AI application?"


# ============================================================
# 8. RETRIEVER EXECUTION
# ============================================================

documents = retriever.invoke(question)

context = "\n".join(
    document.page_content
    for document in documents
)


# ============================================================
# 9. CHAIN EXECUTION
# ============================================================

response = chain.invoke({
    "context": context,
    "question": question
})


# ============================================================
# 10. OUTPUT
# ============================================================

print("\n==============================")
print("QUESTION")
print("==============================")
print(question)

print("\n==============================")
print("RETRIEVED CONTEXT")
print("==============================")
print(context)

print("\n==============================")
print("FINAL ANSWER")
print("==============================")
print(response.content)