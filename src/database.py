"""
database.py

N100 Financial Intelligence Platform
Sprint 1 - Production SQLite Database Manager
"""

import sqlite3
from pathlib import Path
from datetime import datetime

import pandas as pd


class DatabaseManager:

    def __init__(self):

        self.database_path = Path("db") / "nifty100.db"
        self.schema_path = Path("db") / "schema_production.sql"

    # ------------------------------------------------------------
    # Create Database
    # ------------------------------------------------------------
    def create_database(self):

        self.database_path.parent.mkdir(exist_ok=True)

        conn = sqlite3.connect(self.database_path)

        conn.execute("PRAGMA foreign_keys = ON")

        with open(self.schema_path, "r", encoding="utf-8") as f:
            conn.executescript(f.read())

        conn.commit()
        conn.close()

        print("=" * 70)
        print("Production SQLite Database Created Successfully")
        print("=" * 70)

    # ------------------------------------------------------------
    # Load Data
    # ------------------------------------------------------------
    def load_data(self, dataframes):

        print("\n" + "=" * 70)
        print("Loading Data into SQLite")
        print("=" * 70)

        conn = sqlite3.connect(self.database_path)

        conn.execute("PRAGMA foreign_keys = ON")

        audit = []

        for table_name, df in dataframes.items():

            try:

                print(f"Loading {table_name}...")

                # Remove old data but preserve schema
                conn.execute(f"DELETE FROM {table_name}")

                # Insert new data
                df.to_sql(
                    table_name,
                    conn,
                    if_exists="append",
                    index=False
                )

                rows_loaded = len(df)

                audit.append({
                    "table": table_name,
                    "rows_loaded": rows_loaded,
                    "rows_rejected": 0,
                    "status": "SUCCESS",
                    "timestamp": datetime.now()
                })

                print(f"✓ {table_name:<20} {rows_loaded:>6} rows loaded")

            except Exception as e:

                audit.append({
                    "table": table_name,
                    "rows_loaded": 0,
                    "rows_rejected": len(df),
                    "status": f"FAILED : {e}",
                    "timestamp": datetime.now()
                })

                print(f"✗ {table_name}")
                print(e)

        # ------------------------------------------------------------
        # Foreign Key Check
        # ------------------------------------------------------------

        print("\n" + "=" * 70)
        print("Foreign Key Validation")
        print("=" * 70)

        cursor = conn.cursor()

        cursor.execute("PRAGMA foreign_key_check")

        fk_errors = cursor.fetchall()

        if len(fk_errors) == 0:
            print("✓ Foreign Key Check Passed")
        else:
            print(f"✗ Foreign Key Errors : {len(fk_errors)}")

        conn.commit()
        conn.close()

        # ------------------------------------------------------------
        # Save Audit
        # ------------------------------------------------------------

        audit_df = pd.DataFrame(audit)

        output = Path("data") / "output"
        output.mkdir(parents=True, exist_ok=True)

        audit_file = output / "load_audit.csv"

        audit_df.to_csv(audit_file, index=False)

        print("\n" + "=" * 70)
        print("Database Loading Completed")
        print(f"Audit File : {audit_file}")
        print("=" * 70)

    # ------------------------------------------------------------
    # Verify Database
    # ------------------------------------------------------------

    def verify_database(self):

        print("\n" + "=" * 70)
        print("DATABASE VERIFICATION")
        print("=" * 70)

        conn = sqlite3.connect(self.database_path)

        cursor = conn.cursor()

        tables = [
            "companies",
            "profitandloss",
            "balancesheet",
            "cashflow",
            "analysis",
            "documents",
            "prosandcons",
            "sectors",
            "stock_prices",
            "financial_ratios",
            "peer_groups",
            "market_cap"
        ]

        for table in tables:

            try:

                cursor.execute(f"SELECT COUNT(*) FROM {table}")

                rows = cursor.fetchone()[0]

                print(f"{table:<20} {rows:>8} rows")

            except Exception:

                print(f"{table:<20} NOT FOUND")

        print("\nChecking Foreign Keys...")

        cursor.execute("PRAGMA foreign_key_check")

        errors = cursor.fetchall()

        if len(errors) == 0:
            print("✓ No Foreign Key Errors")
        else:
            print(f"✗ {len(errors)} Foreign Key Errors Found")

        conn.close()

        print("=" * 70)