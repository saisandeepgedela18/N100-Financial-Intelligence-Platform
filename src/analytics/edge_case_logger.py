"""
edge_case_logger.py

Sprint 2
Ratio Edge Case Logger
"""

import sqlite3
from pathlib import Path

import pandas as pd


class RatioEdgeCaseLogger:

    def __init__(self):

        self.db = Path("db") / "nifty100.db"

        self.output = Path("data") / "output"
        self.output.mkdir(parents=True, exist_ok=True)

    def run(self):

        print("=" * 70)
        print("Ratio Edge Case Analysis")
        print("=" * 70)

        conn = sqlite3.connect(self.db)

        companies = pd.read_sql(
            "SELECT * FROM companies",
            conn
        )

        ratios = pd.read_sql(
            "SELECT * FROM financial_ratios",
            conn
        )

        sectors = pd.read_sql(
            "SELECT * FROM sectors",
            conn
        )

        merged = ratios.merge(
            companies[
                [
                    "id",
                    "roce_percentage",
                    "roe_percentage"
                ]
            ],
            left_on="company_id",
            right_on="id",
            how="left"
        )

        merged = merged.merge(
            sectors[
                [
                    "company_id",
                    "broad_sector"
                ]
            ],
            on="company_id",
            how="left"
        )

        log = []

        for _, row in merged.iterrows():

            # -----------------------------
            # Financial Sector
            # -----------------------------

            if row["broad_sector"] == "Financials":

                log.append({

                    "company_id": row["company_id"],
                    "issue": "Financial Sector",
                    "category": "Bank ROCE Carve-Out"

                })

                continue

            # -----------------------------
            # ROE Difference
            # -----------------------------

            if pd.notna(row["return_on_equity_pct"]):

                diff = abs(
                    row["return_on_equity_pct"]
                    - row["roe_percentage"]
                )

                if diff > 5:

                    log.append({

                        "company_id": row["company_id"],
                        "issue": "ROE Difference",
                        "category": "Formula Discrepancy"

                    })

        conn.close()

        log_df = pd.DataFrame(log)

        file = self.output / "ratio_edge_cases.log"

        log_df.to_csv(
            file,
            index=False
        )

        print()

        print(f"Edge Cases Logged : {len(log_df)}")

        print(f"Saved : {file}")

        print("=" * 70)