import json

def tenderpilot(tenders, country):
    res = []
    for i in tenders:
        if i["country"] == country:
            print(i["title"])
            res.append(i)
    return res

if __name__ == "__main__":
    with open("tenders.json", "r", encoding="utf-8") as file:
        tenders = json.load(file)
    # tenderpilot(tenders, "France")
    morocco_tenders = tenderpilot(tenders, "Morocco")
    with open("morocco_tenders.json", "w", encoding="utf-8") as file:
        json.dump(morocco_tenders, file, indent=2)
