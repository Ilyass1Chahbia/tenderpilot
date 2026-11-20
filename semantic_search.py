import json
import requests

def similarity(first, second):
    if len(first) != len(second):
        raise ValueError("Embeddings must have the same length.")

    score = 0

    for position in range(len(first)):
        score += first[position] * second[position]

    return score


def get_score(result):
    return result["score"]

with open("documents/semantic_index.json", "r", encoding="utf-8") as file:
    index_data = json.load(file)

question = input("Question: ").strip()

if not question:
    raise SystemExit("Please enter a question.")

response = requests.post(
    "http://100.90.217.38:8765/embed",
    json={"texts": ["query: " + question]},
    timeout=60
)
response.raise_for_status()

data = response.json()

if data["model"] != index_data["model"]:
    raise ValueError("The question and document embeddings must use the same model.")

question_embedding = data["embeddings"][0]

print("Stored chunks:", len(index_data["chunks"]))
print("Question embeddings received:", len(data["embeddings"]))
print("Numbers in question embedding:", len(question_embedding))

selected_source = "2026-OJS214-00763826-en.pdf"

results = []

for chunk in index_data["chunks"]:
    if chunk["source_file"] != selected_source:
        continue

    result = chunk.copy()
    result["score"] = similarity(
        question_embedding,
        chunk["embedding"]
    )
    results.append(result)

print("Chunks searched:", len(results))

top_results = sorted(results, key=get_score, reverse=True)[:3]

for result in top_results:
    print(
        result["source_file"],
        "| Page:", result["page_number"],
        "| Chunk:", result["chunk_number"]
    )
    print("Similarity:", result["score"])
    print(result["text"])
    print()