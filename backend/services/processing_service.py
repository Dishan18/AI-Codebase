import os
from utils.file_reader import read_file
from utils.chunker import chunk_text

def process_repo(repo_path, file_list):
    all_chunks = []

    for relative_path in file_list:
        full_path = os.path.join(repo_path, relative_path)

        content = read_file(full_path)
        if not content:
            continue

        chunks = chunk_text(content)

        for chunk in chunks:
            all_chunks.append({
                "content": chunk,
                "file_path": relative_path
            })
        
    return all_chunks