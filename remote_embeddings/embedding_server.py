from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

MODEL_NAME = "intfloat/multilingual-e5-small"

app = FastAPI()
model = SentenceTransformer(MODEL_NAME, device="cpu")

class EmbeddingRequest(BaseModel):
    texts: list[str]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/embed")
def embed(body: EmbeddingRequest):
    embeddings = model.encode(
        body.texts,
        normalize_embeddings=True
    )

    return {
        "model": MODEL_NAME,
        "embeddings": embeddings.tolist()
    }
