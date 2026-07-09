"""
database.py

N100 Financial Intelligence Platform
Sprint 1 - SQLite Database Manager
"""

import sqlite3
from pathlib import Path

import pandas as pd


class DatabaseManager:

    def __init__(self):

        self.database_path = Path("db") / "nifty100.db"
        self.schema_path = Path("db") / "schema.sql"

    def create_database(self):

        conn = sqlite3.connect(self.database_path)

        conn.execute("PRAGMA foreign_keys = ON")

        with open(self.schema_path, "r", encoding="utf-8") as f:

            conn.executescript(f.read())

        conn.commit()
        conn.close()

        print("=" * 70)
        print("SQLite Database Created Successfully")
        print("=" * 70)

    def load_data(self, dataframes):

        print("\n" + "=" * 70)
        print("Loading Data into SQLite")
        print("=" * 70)

        conn = sqlite3.connect(self.database_path)

        audit = []

        for table_name, df in dataframes.items():

            try:

                # Write dataframe to SQLite
                df.to_sql(
                    table_name,
                    conn,
                    if_exists="replace",
                    index=False
                )

                rows = len(df)

                audit.append({
                    "table": table_name,
                    "rows_loaded": rows,
                    "status": "SUCCESS"
                })

                print(f"✓ {table_name:<20} {rows:>6} rows loaded")

            except Exception as e:

                audit.append({
                    "table": table_name,
                    "rows_loaded": 0,
                    "status": f"FAILED : {e}"
                })

                print(f"✗ {table_name} -> {e}")

        conn.commit()
        conn.close()

        audit_df = pd.DataFrame(audit)

        output = Path("data") / "output"
        output.mkdir(exist_ok=True)

        audit_file = output / "load_audit.csv"

        audit_df.to_csv(audit_file, index=False)

        print("\n" + "=" * 70)
        print("Database Loading Completed")
        print(f"Audit File : {audit_file}")
        print("=" * 70)