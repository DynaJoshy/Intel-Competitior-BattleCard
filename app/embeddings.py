import chromadb
from chromadb.config import Settings
from openai import OpenAI
from datetime import datetime
from .config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

chroma = chromadb.Client(
    Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory="./vectorstore"
    )
)

collection = chroma.get_or_create_collection("deal_chunks")


def embed(texts: list[str]) -> list[list[float]]:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )
    return [e.embedding for e in response.data]


def index_chunks(deal_id: str, chunks: list[str]):
    vectors = embed(chunks)

    timestamp = datetime.utcnow().isoformat()

    ids = [f"{deal_id}-{i}" for i in range(len(chunks))]

    metadatas = [
        {
            "deal_id": deal_id,
            "chunk_index": i,
            "created_at": timestamp
        }
        for i in range(len(chunks))
    ]

    collection.add(
        documents=chunks,
        embeddings=vectors,
        ids=ids,
        metadatas=metadatas
    )

    return ids


def retrieve(query: str, k: int = 8):
    q_emb = embed([query])[0]

    results = collection.query(
        query_embeddings=[q_emb],
        n_results=k,
        include=["documents", "metadatas", "ids"]
    )

    return list(
        zip(
            results["ids"],
            results["documents"],
            results["metadatas"]
        )
    )
