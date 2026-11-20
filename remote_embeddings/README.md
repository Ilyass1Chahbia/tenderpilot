# Remote embedding service

Run on the remote Linux machine, from this folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu
python -m uvicorn embedding_server:app --host 100.90.217.38 --port 8765
```

The CPU package index is needed for the recorded PyTorch CPU build.
The model downloads on first startup.
The local TenderPilot client connects through Tailscale.

Endpoints:
- GET /health
- POST /embed, with JSON such as:
  {"texts": ["query: Who is the buyer?"]}