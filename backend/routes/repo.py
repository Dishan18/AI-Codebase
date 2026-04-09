from fastapi import APIRouter
from pydantic import BaseModel

from services.repo_service import clone_repo
from utils.file_filter import get_valid_files
from services.processing_service import process_repo


from services.processing_service import process_repo
from services.embedding_service import generate_embeddings
from services.vector_store import create_faiss_index
from services.store import store

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

    # store in memory
    store["index"] = index
    store["chunks"] = chunks

    return {
        "repo_name": repo_name,
        "total_files": len(files),
        "total_chunks": len(chunks),
        "embedding_dim": embeddings.shape[1],
        "status": "ready for querying"
    }