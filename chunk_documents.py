import json
from pathlib import Path
from chunk_text import split_text

for pdf_path in Path("documents").glob("*.pdf"):
    pages_path = pdf_path.with_suffix(".pages.json")

    with open(pages_path, "r", encoding="utf-8") as file:
        pages = json.load(file)

    records = []

    for page in pages:
        chunks = split_text(page["text"], 500, 100)

        for chunk_number, chunk in enumerate(chunks, start=1):
            records.append({
                "source_file": page["source_file"],
                "page_number": page["page_number"],
                "chunk_number": chunk_number,
                "text": chunk
            })

    output_path = pdf_path.with_suffix(".chunks.json")

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=2, ensure_ascii=False)

    print(
        "Saved:", output_path.name,
        "| Pages:", len(pages),
        "| Chunks:", len(records)
    )