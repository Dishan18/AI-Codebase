import os
import shutil
from git import Repo

BASE_DIR = "repos"

def clone_repo(repo_url: str):
    print(f"Cloning repo: {repo_url}")

    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

    repo_name = repo_url.rstrip("/").split("/")[-1]
    clone_path = os.path.join(BASE_DIR, repo_name)

    if os.path.exists(clone_path):
        shutil.rmtree(clone_path)

    try:
        Repo.clone_from(repo_url, clone_path, depth=1, single_branch=True)
        print("Clone completed")
    except Exception as e:
        print("Error:", e)
        raise Exception("Invalid or inaccessible repository")

    return repo_name, clone_path