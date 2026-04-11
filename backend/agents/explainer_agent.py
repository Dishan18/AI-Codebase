from services.llm_service import generate_answer

def explain(query, context_chunks, history):
    prompt = f"""
You are a senior software engineer.

Explain the code clearly and concisely.

Focus on:
- what the code does
- key logic
- important components

Use only the provided context.

Question:
{query}
"""

    return {
        "answer": generate_answer(prompt, context_chunks, history),
        "results": context_chunks[:3]
    }