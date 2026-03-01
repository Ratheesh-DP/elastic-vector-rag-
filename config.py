from elasticsearch import Elasticsearch
import os
from dotenv import load_dotenv

load_dotenv()

ELASTIC_URL = "http://localhost:9200"
INDEX_NAME = "rag-index"

es = Elasticsearch(ELASTIC_URL)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
