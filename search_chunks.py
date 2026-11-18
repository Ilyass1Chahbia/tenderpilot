import json

def search_chunks(chunks, query):
    matches = []

    for chunk in chunks:
        if query.lower() in chunk["text"].lower():
            matches.append(chunk)

    return matches

with open(
    "documents/2026-OJS214-00763826-en.chunks.json",
    "r",
    encoding="utf-8"
) as file:
    chunks = json.load(file)

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