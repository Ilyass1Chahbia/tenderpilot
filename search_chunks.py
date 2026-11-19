import json
from pathlib import Path

def get_score(result):
    return result["score"]

def search_chunks(chunks, query):
    matches = []

    for chunk in chunks:
        score = chunk["text"].lower().count(query.lower())

        if score > 0:
            result = chunk.copy()
            result["score"] = score
            matches.append(result)

    return sorted(matches, key=get_score, reverse=True)

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

    top_results = results[:3]
    print("Showing:", len(top_results))
    for result in top_results:
        text = result["text"]
        score = result["score"]
        position = text.lower().find(query.lower())
        preview = text[position:position + 160]

        print(
            result["source_file"],
            "| Page:", result["page_number"],
            "| Chunk:", result["chunk_number"],
            "| Score:", score
        )
        print("Preview:", preview)
        print()