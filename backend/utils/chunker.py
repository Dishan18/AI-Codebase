def chunk_text(text, chunk_size=1000, overlap=100):
    chunks = []
    
    paragraphs = text.split("\n\n")
    current_chunk = ""

    for para in paragraphs:
        if len(current_chunk) + len(para) < chunk_size:
            current_chunk += para + "\n\n"
        else:
            if current_chunk.strip():
                chunks.append(current_chunk.strip())

            current_chunk = current_chunk[-overlap:] + para + "\n\n"

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks

def chunk_code(text, chunk_size=60, overlap=10):
    lines = text.split("\n")
    chunks = []

    for i in range(0, len(lines), chunk_size - overlap):
        chunk = "\n".join(lines[i:i+chunk_size])
        if chunk.strip():
            chunks.append(chunk)

    return chunks