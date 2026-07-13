import sqlite3

conn = sqlite3.connect("db/test.db")

with open("db/schema_production.sql", "r", encoding="utf-8") as f:
    conn.executescript(f.read())

print("=" * 60)
print("Production Schema Created Successfully")
print("=" * 60)

cursor = conn.cursor()

cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table'
ORDER BY name;
""")

for table in cursor.fetchall():
    print(table[0])

conn.close()