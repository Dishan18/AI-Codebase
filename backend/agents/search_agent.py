def code_search(query, context_chunks):
    results = []
    q = query.lower()

    for c in context_chunks:
        content = c["content"]
        if q in content.lower():
            results.append({
                "file_path": c["file_path"],
                "snippet": content.strip()[:300]
            })

    return results[:5]