import json
from pathlib import Path

def search_chunks(chunks, query):
    matches = []

    for chunk in chunks:
        if query.lower() in chunk["text"].lower():
            matches.append(chunk)

    return matches

chunks = []

for pdf_path in Path("documents").glob("*.pdf"):
    chunks_path = pdf_path.with_suffix(".chunks.json")

    with open(chunks_path, "r", encoding="utf-8") as file:
        document_chunks = json.load(file)

    chunks.extend(document_chunks)

print("Chunks loaded:", len(chunks))

query = input("Search for: ").strip()

if not query:
    print("Please enter some text to search for.")
else:
    results = search_chunks(chunks, query)

    print("Matches found:", len(results))

    if not results:
        print("No matching passages found.")

    for result in results:
        print(
            result["source_file"],
            "| Page:", result["page_number"],
            "| Chunk:", result["chunk_number"]
        )