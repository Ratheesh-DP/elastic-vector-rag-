# elastic-vector-rag-
# Vectorized Thinking: Production RAG with Elasticsearch

This project demonstrates how to build a production-ready Retrieval-Augmented Generation (RAG) pipeline using Elasticsearch as a vector database.

## Features
- Dense vector indexing
- kNN semantic search
- Hybrid search (BM25 + vector)
- RAG pipeline integration
- Production-ready architecture

## Architecture

User Query → Embedding Model → Elasticsearch kNN → Top-K Docs → LLM → Response

## Setup

1. Install dependencies:
pip install -r requirements.txt

2. Start Elasticsearch locally (Docker recommended)

3. Create index:
python create_index.py

4. Ingest data:
python ingest_data.py

5. Run search:
python search.py

6. Run RAG pipeline:
python rag_pipeline.py
