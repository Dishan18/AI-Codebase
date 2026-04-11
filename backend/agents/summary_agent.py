from services.llm_service import generate_answer

def summarize(query, context_chunks, history):
    prompt = f"""
You are a senior engineer.

Provide a high-level summary of the repository/code.

Include:
- purpose of the project
- main components
- how pieces fit together

Use only the provided context.

Question:
{query}
"""
    return generate_answer(prompt, context_chunks, history)