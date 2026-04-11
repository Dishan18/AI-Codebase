import os
from utils.file_reader import read_file
from utils.chunker import chunk_text, chunk_code

def process_repo(repo_path, file_list):
    all_chunks = []
    file_chunk_count = {}

    for relative_path in file_list:
        full_path = os.path.join(repo_path, relative_path)

        content = read_file(full_path)
        if not content:
            continue
        path_upper = relative_path.upper()
        if "README" in path_upper:
            content = content[:300]
        elif "DOC" in path_upper:
            content = content[:500]

        if relative_path.lower().endswith((".html", ".js", ".ts", ".jsx", ".tsx", ".py")):
            chunks = chunk_code(content)
        else:
            chunks = chunk_text(content)

        if relative_path not in file_chunk_count:
            file_chunk_count[relative_path] = 0

        for chunk in chunks:
            if file_chunk_count[relative_path] >= 5:
                break  
            all_chunks.append({
                "content": chunk,
                "file_path": relative_path
            })
            file_chunk_count[relative_path] += 1
    return all_chunks