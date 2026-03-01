from config import es, INDEX_NAME, OPENAI_API_KEY
from sentence_transformers import SentenceTransformer
from openai import OpenAI

client = OpenAI(api_key=OPENAI_API_KEY)
model = SentenceTransformer("all-mpnet-base-v2")

def retrieve(query):
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

    docs = [hit["_source"]["content"] for hit in response["hits"]["hits"]]
    return "\n".join(docs)

def generate_answer(query):
    context = retrieve(query)

    prompt = f"""
    Answer using only the context below.

    Context:
    {context}

    Question:
    {query}
    """

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return completion.choices[0].message.content


if __name__ == "__main__":
    user_query = "What are benefits of hybrid search?"
    answer = generate_answer(user_query)
    print("\nGenerated Answer:\n")
    print(answer)
