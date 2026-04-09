from sentence_transformers import SentenceTransformer

# load model once (important for performance)
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(chunks):
    texts = [chunk["content"] for chunk in chunks]

    embeddings = model.encode(texts)

    return embeddings


def embed_query(query: str):
    return model.encode([query])