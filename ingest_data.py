from config import es, INDEX_NAME
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-mpnet-base-v2")

docs = [
    "Elasticsearch supports vector search using dense vectors.",
    "RAG improves LLM accuracy by grounding responses.",
    "Hybrid search combines BM25 and vector similarity.",
    "HNSW indexing improves ANN performance.",
    "Quantization reduces memory usage in vector databases."
]

for i, doc in enumerate(docs):
    embedding = model.encode(doc).tolist()

    es.index(
        index=INDEX_NAME,
        id=i,
        document={
            "content": doc,
            "embedding": embedding
        }
    )

print("Documents indexed successfully.")
