import requests

url = "http://100.90.217.38:8765/embed"

payload = {
    "texts": ["query: Who is the buyer?"]
}

response = requests.post(url, json=payload, timeout=10)

print("HTTP status:", response.status_code)
response.raise_for_status()

data = response.json()
embeddings = data["embeddings"]
print("Model:", data["model"])
print("Embeddings returned:", len(embeddings))
print("Numbers in first embedding:", len(embeddings[0]))