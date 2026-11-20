import json
from pathlib import Path
import requests

chunks = []

for pdf_path in Path("documents").glob("*.pdf"):
    chunks_path = pdf_path.with_suffix(".chunks.json")

    with open(chunks_path, "r", encoding="utf-8") as file:
        chunks.extend(json.load(file))

texts = []

for chunk in chunks:
    texts.append("passage: " + chunk["text"])
response = requests.post(
    "http://100.90.217.38:8765/embed",
    json={"texts": texts},
    timeout=120
    )
response.raise_for_status()

data = response.json()
embeddings = data["embeddings"]

print("Chunks sent:", len(chunks))
print("Embeddings received:", len(embeddings))
print("Number per embedding:", len(embeddings[0]))

if len(embeddings) != len(chunks):
    raise ValueError("The number of embeddings must match the number of chunks.")

for position, chunk in enumerate(chunks):
    chunk["embedding"] = embeddings[position]

index_data = {
    "model": data["model"],
    "normalized": True,
    "chunks": chunks
}

with open(
    "documents/semantic_index.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(index_data, file, indent=2, ensure_ascii=False)

print("Index saved:", len(chunks), "chunks")