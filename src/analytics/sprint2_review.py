"""
sprint2_review.py

Sprint 2 Final Review
"""

import sqlite3
from pathlib import Path
import pandas as pd


class Sprint2Review:

    def __init__(self):
        self.db = Path("db") / "nifty100.db"

    def run(self):

        print("=" * 70)
        print("SPRINT 2 REVIEW")
        print("=" * 70)

        conn = sqlite3.connect(self.db)

        ratios = pd.read_sql(
            "SELECT * FROM financial_ratios",
            conn
        )

        print(f"\nTotal Ratio Records : {len(ratios)}")

        if len(ratios) >= 1100:
            print("✓ Row Count Requirement Passed")
        else:
            print("✗ Row Count Requirement Failed")

        print("\nChecking KPI Columns...")

        kpis = [
            "net_profit_margin_pct",
            "operating_profit_margin_pct",
            "return_on_equity_pct",
            "debt_to_equity",
            "interest_coverage",
            "asset_turnover",
            "free_cash_flow_cr"
        ]

        for column in kpis:

            if column in ratios.columns:

                if ratios[column].notna().sum() > 0:
                    print(f"✓ {column}")
                else:
                    print(f"✗ {column}")

            else:
                print(f"✗ Missing : {column}")

        print("\nSample Records\n")

        print(
            ratios.head(5)
        )

        conn.close()

        print("\n" + "=" * 70)
        print("Sprint 2 Review Completed")
        print("=" * 70)