from fastapi import APIRouter
from pydantic import BaseModel

from services.repo_service import clone_repo
from utils.file_filter import get_valid_files
from services.processing_service import process_repo
from services.embedding_service import embed_query, generate_embeddings
from services.vector_store import search_index, create_faiss_index
from services.store import store

from agents.router_agent import route_query

router = APIRouter()

class RepoRequest(BaseModel):
    repo_url: str


@router.post("/ingest-repo")
def ingest_repo(req: RepoRequest):
    repo_name, repo_path = clone_repo(req.repo_url)
    files = get_valid_files(repo_path)
    chunks = process_repo(repo_path, files)
    embeddings = generate_embeddings(chunks)
    index = create_faiss_index(embeddings)

    store["index"] = index
    store["chunks"] = chunks
    store["history"] = []

    return {
        "repo_name": repo_name,
        "total_files": len(files),
        "total_chunks": len(chunks),
        "embedding_dim": embeddings.shape[1],
        "status": "ready for querying"
    }


class QueryRequest(BaseModel):
    query: str
    top_k: int = 3


@router.post("/query-repo")
def query_repo(req: QueryRequest):
    if store["index"] is None or store["chunks"] is None:
        return {"error": "No repository indexed yet"}

    query_embedding = embed_query(req.query)
    indices = search_index(store["index"], query_embedding, max(req.top_k, 15))

    seen = set()
    results = []
    for i in indices[0]:
        if i == -1: continue
        chunk = store["chunks"][i]
        if chunk["file_path"] in seen: continue
        seen.add(chunk["file_path"])
        results.append({"content": chunk["content"][:500], "file_path": chunk["file_path"]})
        if len(results) == 3: break

    history = store["history"][-3:]
    agent_response = route_query(req.query, results, history)
    answer_text = agent_response.get("answer")
    
    store["history"].append({"query": req.query, "answer": answer_text})
    store["history"] = store["history"][-3:]

    return {
        "query": req.query,
        "answer": answer_text,
        "results": agent_response.get("results", []),
        "sources": results
    }