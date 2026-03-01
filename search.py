from config import es, INDEX_NAME
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-mpnet-base-v2")

query = "How does hybrid search work?"
query_vector = model.encode(query).tolist()

response = es.search(
    index=INDEX_NAME,
    knn={
        "field": "embedding",
        "query_vector": query_vector,
        "k": 3,
        "num_candidates": 50
    }
)

print("Top Results:")
for hit in response["hits"]["hits"]:
    print(hit["_source"]["content"])
