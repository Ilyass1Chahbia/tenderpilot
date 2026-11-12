import json
from pathlib import Path
from read_notice import extract_pages

for pdf_path in Path("documents").glob("*.pdf"):
    pages = extract_pages(pdf_path)

    output_path = pdf_path.with_suffix(".pages.json")

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(pages, file, indent=2, ensure_ascii=False)

    print("Saved:", output_path.name, "| Pages:", len(pages))