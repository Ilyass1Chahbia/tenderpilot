import requests

url = "https://api.ted.europa.eu/v3/notices/search"

payload = {
    "query": "buyer-country=FRA",
    "fields": ["publication-number", "notice-title"],
    "page": 1,
    "limit": 5
}

response = requests.post(url, json=payload, timeout=30)

print("HTTP status:", response.status_code)
response.raise_for_status()

data = response.json()

print("Response type:", type(data))
print("Response keys:", data.keys())

notices = data["notices"]

print("Search timed out:", data["timedOut"])
print("Notices type:", type(notices))
print("Returned notices:", len(notices))

for notice in notices:
    print(notice["publication-number"], " | " , notice["notice-title"]["eng"])

print("Total matches:", data["totalNoticeCount"])