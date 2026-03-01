from config import es, INDEX_NAME

mapping = {
    "mappings": {
        "properties": {
            "content": {"type": "text"},
            "embedding": {
                "type": "dense_vector",
                "dims": 768,
                "index": True,
                "similarity": "cosine"
            }
        }
    }
}

if es.indices.exists(index=INDEX_NAME):
    es.indices.delete(index=INDEX_NAME)

es.indices.create(index=INDEX_NAME, body=mapping)

print("Index created successfully.")
