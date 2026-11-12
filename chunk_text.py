
def split_text(text, chunk_size):
    chunks = []

    for start in range(0, len(text), chunk_size):
        chunk = text[start:start + chunk_size]
        chunks.append(chunk)
    return chunks

if __name__ == "__main__":
    result = split_text("ABCDEFGHIJ", 4)
    print(result)