from fastapi import APIRouter
from pydantic import BaseModel

from services.repo_service import clone_repo
from utils.file_filter import get_valid_files
from services.processing_service import process_repo
from services.embedding_service import embed_query, generate_embeddings
from services.vector_store import search_index, create_faiss_index
from services.store import store
from pydantic import BaseModel
from services.llm_service import generate_answer

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

    return {
        "repo_name": repo_name,
        "total_files": len(files),
        "total_chunks": len(chunks),
        "embedding_dim": embeddings.shape[1],
        "status": "ready for querying"
    }

from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str
    top_k: int = 3


@router.post("/query-repo")
def query_repo(req: QueryRequest):
    if store["index"] is None or store["chunks"] is None:
        return {"error": "No repository indexed yet"}
    query_embedding = embed_query(req.query)
    indices = search_index(store["index"], query_embedding, req.top_k)
    results = []
    for i in indices[0]:
        if i == -1:
            continue
        chunk = store["chunks"][i]

        results.append({
            "content": chunk["content"][:500],
            "file_path": chunk["file_path"]
        })
    results = results[:3]
    answer = generate_answer(req.query, results)
    return {
        "query": req.query,
        "answer": answer,
        "sources": results
    }