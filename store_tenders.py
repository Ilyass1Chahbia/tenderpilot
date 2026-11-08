import json, os
from datetime import date

import psycopg
from dotenv import load_dotenv

load_dotenv()

with open("normalized_tenders.json", "r", encoding="utf-8") as file:
    records = json.load(file)

with psycopg.connect(
    host="127.0.0.1",
    port=5434,
    dbname="tenderpilot",
    user="tenderpilot",
    password=os.environ["POSTGRES_PASSWORD"],
    connect_timeout=5
) as conn:
    with conn.cursor() as cur:
        for records in records:
            publication_date = date.fromisoformat(
                records["publication_date"][:10]
            )

            cur.execute(
                """
                INSERT INTO tenders (
                    publication_number,
                    title_en,
                    publication_date
                )
                VALUES (%s, %s, %s)
                ON CONFLICT (publication_number) DO NOTHING;
                """,
                (
                    records["publication_number"],
                    records["title_en"],
                    publication_date
                )
            )

        cur.execute("SELECT COUNT(*) FROM tenders;")
        total = cur.fetchone()[0]

print("Rows stored:", total)