import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"


def generate_answer(query, context_chunks, history=[]):
    history_text = "\n\n".join(
        [f"Q: {h['query']}\nA: {h['answer']}" for h in history]
    )

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

Conversation history:
{history_text}

Context:
{context}

Question:
{query}

Answer:
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=30
        )

        response.raise_for_status()
        data = response.json()

        return data.get("response", "No response from model")

    except requests.exceptions.RequestException:
        return "LLM request failed (Ollama not running or network issue)"
    except ValueError:
        return "Invalid response from LLM"