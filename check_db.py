import os

import psycopg
from dotenv import load_dotenv

load_dotenv()

with psycopg.connect(
    host="127.0.0.1",
    port=5434,
    dbname="tenderpilot",
    user="tenderpilot",
    password=os.environ["POSTGRES_PASSWORD"],
    connect_timeout=5
) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT current_database(), current_user;")
        result = cur.fetchone()
        print("Connected to database and user:", result)