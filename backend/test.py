from services.embedding_service import generate_embeddings, embed_query
from services.vector_store import create_faiss_index, search_index

chunks = [
    {"content": "login user with password", "file_path": "auth.py"},
    {"content": "render homepage UI", "file_path": "ui.js"},
    {"content": "authenticate user credentials", "file_path": "auth.py"}
]
embeddings = generate_embeddings(chunks)

index = create_faiss_index(embeddings)

query = "user authentication"
query_emb = embed_query(query)

indices = search_index(index, query_emb, k=2)

print(indices)