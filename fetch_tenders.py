import requests, json, time

def normalize_notices(notices):
    res = []
    for notice in notices:
        tmp = {}
        tmp["publication_number"] = notice["publication-number"]
        tmp["title_en"] = notice["notice-title"].get("eng")
        tmp["publication_date"] = notice["publication-date"]
        res.append(tmp)
    return res

url = "https://api.ted.europa.eu/v3/notices/search"

payload = {
    "query": "buyer-country=FRA AND publication-date>=20260101",
    "fields": ["publication-number", "notice-title", "publication-date"],
    "page": 1,
    "limit": 250
}

all_notices = []

for page in range(1, 5):
    payload["page"] = page

    time.sleep(5)
    response = requests.post(url, json=payload, timeout=30)
    if response.status_code == 429:
        print(
            "Retry-After",
            response.headers.get("Retry-After", "not provided")
        )
    response.raise_for_status()

    data = response.json()
    page_notices = data["notices"]

    all_notices.extend(page_notices)

    print("Page:", page)
    print("Returned notices:", len(page_notices))
    print("Search timed out:", data["timedOut"])

print("Total collected:", len(all_notices))

records = normalize_notices(all_notices)

with open("normalized_tenders.json", "w", encoding="utf-8") as file:
    json.dump(records, file, indent=2, ensure_ascii=False)

for record in records[:3]:
    print(
        record["publication_number"],
        "|",
        record["publication_date"],
        "|",
        record["title_en"]
    )

print("Normalized records:", len(records))

if records:
    print("First normalized record:", records[0])