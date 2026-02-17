import json
import sqlite3

JSON_PATH = "quotes.json"
DB_PATH = "quotes.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS quotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quote TEXT NOT NULL,
    author TEXT,
    category TEXT NOT NULL
)
""")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

inserted = 0

for item in data:
    quote = item.get("Quote")
    author = item.get("Author")
    category = item.get("Category")

    if not quote or not category:
        continue

    cursor.execute(
        "INSERT INTO quotes (quote, author, category) VALUES (?, ?, ?)",
        (
            quote.strip(),
            (author or "Unknown").strip(),
            category.strip().lower()
        )
    )
    inserted += 1

conn.commit()
conn.close()

print(f"Imported {inserted} quotes successfully.")