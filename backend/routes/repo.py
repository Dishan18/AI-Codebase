from fastapi import APIRouter
from pydantic import BaseModel

from services.repo_service import clone_repo
from utils.file_filter import get_valid_files
from services.processing_service import process_repo
router = APIRouter()

class RepoRequest(BaseModel):
    repo_url: str

@router.post("/ingest-repo")
def ingest_repo(req: RepoRequest):
    repo_name, repo_path = clone_repo(req.repo_url)

    files = get_valid_files(repo_path)

    chunks = process_repo(repo_path, files)

    return {
        "repo_name": repo_name,
        "total_files": len(files),
        "total_chunks": len(chunks),
        "sample_chunks": chunks[:5]
    }