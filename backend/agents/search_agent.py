def code_search(query, context_chunks):
    results = []
    q = query.lower()

    for c in context_chunks:
        content = c["content"]
        if q in content.lower():
            results.append({
                "file_path": c["file_path"],
                "content": content.strip()[:800]
            })

    return {
        "answer": None,
        "results": results[:5]
    }