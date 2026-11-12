import json
from chunk_text import split_text

with open(
    "documents/2026-OJS214-00763826-en.pages.json",
    "r",
    encoding="utf-8"
) as file:
    pages = json.load(file)

page = pages[0]
chunks = split_text(page["text"], 500)

records = []

for page in pages:
    chunks = split_text(page["text"], 500)

    for chunk_number, chunk in enumerate(chunks, start=1):
        records.append({
            "source_file": page["source_file"],
            "page_number": page["page_number"],
            "chunk_number": chunk_number,
            "text": chunk
        })

with open(
    "documents/2026-OJS214-00763826-en.chunks.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(records, file, indent=2, ensure_ascii=False)

print("Pages processed:", len(pages))
print("Chunks saved:", len(records))