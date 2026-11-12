import json
from pypdf import PdfReader
from pathlib import Path


def extract_pages(pdf_path):
    pages = []

    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)

        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text()

            pages.append({
                "source_file": Path(pdf_path).name,
                "page_number": page_number,
                "text": text
            })

    return pages

if __name__ == "__main__":
    pages = extract_pages("documents/2026-OJS220-00789482-en.pdf")

    with open("documents/789482-2026.pages.json", "w", encoding="utf-8") as file:
        json.dump(pages, file, indent=2, ensure_ascii=False)

    print("Pages saved:", len(pages))

    if pages:
        print("First page preview:", pages[0]["text"][:300])