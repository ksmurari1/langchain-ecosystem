# Data Ingestion

## Definition

**Data Ingestion is the process of bringing external data into LangChain so it can be processed by the rest of the application.**

A document loader reads a source and converts it into LangChain `Document` objects.

```text
Data Source
   ↓
Document Loader
   ↓
LangChain Document
   ↓
Text Splitter
```

## What is a `Document`?

A LangChain `Document` mainly contains:

- `page_content` — the actual text
- `metadata` — information about the source

Example:

```python
from langchain_community.document_loaders import TextLoader

loader = TextLoader("sample.txt")
documents = loader.load()

print(documents[0].page_content)
print(documents[0].metadata)
```

Typical metadata:

```text
{'source': 'sample.txt'}
```

## Why ingest data if we do not answer a question immediately?

Because ingestion is a **preparation step**. The loaded document can later be:

```text
Document
   ↓
Text Splitter
   ↓
Chunks
   ↓
Embeddings
   ↓
Vector Store
   ↓
Retriever
```

## Example

A company knowledge-base chatbot might ingest:

- HR policies
- product manuals
- support documents
- technical guides

The application first prepares this knowledge. Retrieval happens later when a user asks a question.

## Repository

See `data_ingestion.py`.

