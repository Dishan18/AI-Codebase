import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"


def generate_answer(query, context_chunks):
    context = "\n\n".join(
        [f"File: {c['file_path']}\nCode:\n{c['content']}" for c in context_chunks]
    )

    prompt = f"""
You are a senior software engineer.

Your task:
- Explain clearly what the code does
- Mention key components and logic
- Be concise but accurate

Rules:
- Use ONLY the provided context
- If unsure, say "Not enough information"

Context:
{context}

Question:
{query}

Answer:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]