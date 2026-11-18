def split_text(text, chunk_size, overlap=0):
    if chunk_size <= 0 or overlap < 0 or overlap >= chunk_size:
        raise ValueError("Use a positive chunk size and a smaller, nonnegative overlap.")

    chunks = []
    step = chunk_size - overlap

    for start in range(0, len(text), step):
        chunk = text[start:start + chunk_size]
        chunks.append(chunk)

        if start + chunk_size >= len(text):
            break

    return chunks


if __name__ == "__main__":
    result = split_text("ABCDEFGHIJ", 4, 1)
    print(result)