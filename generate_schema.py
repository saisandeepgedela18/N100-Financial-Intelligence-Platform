import pandas as pd
from pathlib import Path

RAW_DATA = Path("data/raw")
OUTPUT = Path("db/schema_generated.sql")

special_files = [
    "financial_ratios",
    "market_cap",
    "peer_groups",
    "sectors",
    "stock_prices"
]

tables = []

for file in RAW_DATA.glob("*.xlsx"):

    table_name = file.stem.lower()

    print(f"Processing {table_name}...")

    if table_name in special_files:
        df = pd.read_excel(file)
    else:
        df = pd.read_excel(file, header=1)

    sql = []
    sql.append(f"\n-- {table_name.upper()}")
    sql.append(f"CREATE TABLE IF NOT EXISTS {table_name} (")

    cols = []

    for col in df.columns:

        col = (
            str(col)
            .strip()
            .replace(" ", "_")
            .replace("%", "pct")
            .replace("/", "_")
            .replace("-", "_")
            .replace("(", "")
            .replace(")", "")
            .replace(".", "")
            .lower()
        )

        if col == "id":
            cols.append("    id TEXT PRIMARY KEY")

        elif "year" in col:
            cols.append(f"    {col} TEXT")

        elif "date" in col:
            cols.append(f"    {col} TEXT")

        else:
            cols.append(f"    {col} TEXT")

    sql.append(",\n".join(cols))
    sql.append(");")

    tables.append("\n".join(sql))

OUTPUT.write_text("\n\n".join(tables), encoding="utf-8")

print("\nSchema Generated Successfully!")
print(f"Saved to : {OUTPUT}")