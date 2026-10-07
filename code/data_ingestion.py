from langchain_community.document_loaders import TextLoader

loader = TextLoader("../data/sample.txt")
documents = loader.load()

print("Documents:", len(documents))
print("Content:", documents[0].page_content)
print("Metadata:", documents[0].metadata)
