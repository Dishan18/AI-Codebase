from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm

def generate_embeddings(chunks):
    texts = [chunk["content"] for chunk in chunks]
    embeddings = model.encode(texts)
    embeddings = np.array([normalize(e) for e in embeddings]).astype("float32")
    return embeddings

def embed_query(query: str):
    embedding = model.encode([query])[0]
    embedding = normalize(embedding)
    return np.array([embedding]).astype("float32")