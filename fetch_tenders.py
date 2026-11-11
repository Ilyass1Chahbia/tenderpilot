import requests, json, time
from datetime import date, timedelta

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

start_date = date.today() - timedelta(days=7)
start_date_next = start_date.strftime("%Y%m%d")

print("Collecting since: ", start_date)

payload = {
    "query": "buyer-country=FRA AND publication-date>=" + start_date_next,
    "fields": ["publication-number", "notice-title", "publication-date"],
    "page": 1,
    "limit": 250
}

all_notices = []
page = 1

while True:
    payload["page"] = page
    time.sleep(5)

    response = requests.post(url, json=payload, timeout=30)

    if response.status_code == 429:
        print(
            "Retry-After:",
            response.headers.get("Retry-After", "not provided")
        )

    response.raise_for_status()
    data = response.json()

    if data["timedOut"]:
        raise RuntimeError("TED search timed out; collection stopped.")

    page_notices = data["notices"]
    all_notices.extend(page_notices)

    print("Page:", page)
    print("Returned notices:", len(page_notices))

    if len(page_notices) < payload["limit"]:
        break

    page += 1
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