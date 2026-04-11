from services.llm_service import generate_answer

def debug(query, context_chunks, history):
    prompt = f"""
You are a senior engineer debugging code.

Analyze the issue and provide:
1. Possible cause
2. Suggested fix
3. Explanation

Use only the given context.

Issue:
{query}
"""

    return {
        "answer": generate_answer(prompt, context_chunks, history),
        "results": context_chunks[:3]
    }