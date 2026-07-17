"""
ratio_engine.py

Sprint 2
Financial Ratio Engine
"""

import sqlite3
from pathlib import Path

import pandas as pd

from src.analytics.ratios import RatioEngine
from src.analytics.cashflow_kpis import CashFlowKPI


class FinancialRatioEngine:

    def __init__(self):

        self.db = Path("db") / "nifty100.db"

    def run(self):

        print("=" * 70)
        print("Generating Financial Ratios")
        print("=" * 70)

        conn = sqlite3.connect(self.db)

        pnl = pd.read_sql("SELECT * FROM profitandloss", conn)
        bs = pd.read_sql("SELECT * FROM balancesheet", conn)
        cf = pd.read_sql("SELECT * FROM cashflow", conn)

        merged = pnl.merge(
            bs,
            on=["company_id", "year"],
            how="left",
            suffixes=("_pnl", "_bs")
        )

        merged = merged.merge(
            cf,
            on=["company_id", "year"],
            how="left"
        )

        ratios = []

        for _, row in merged.iterrows():

            npm = RatioEngine.net_profit_margin(
                row["net_profit"],
                row["sales"]
            )

            opm = RatioEngine.operating_profit_margin(
                row["operating_profit"],
                row["sales"]
            )

            roe = RatioEngine.return_on_equity(
                row["net_profit"],
                row["equity_capital"],
                row["reserves"]
            )

            de = RatioEngine.debt_to_equity(
                row["borrowings"],
                row["equity_capital"],
                row["reserves"]
            )

            icr = RatioEngine.interest_coverage_ratio(
                row["operating_profit"],
                row["other_income"],
                row["interest"]
            )

            asset_turnover = RatioEngine.asset_turnover(
                row["sales"],
                row["total_assets"]
            )

            fcf = CashFlowKPI.free_cash_flow(
                row["operating_activity"],
                row["investing_activity"]
            )

            ratios.append({

                "company_id": row["company_id"],
                "year": row["year"],

                "net_profit_margin_pct": npm,
                "operating_profit_margin_pct": opm,
                "return_on_equity_pct": roe,

                "debt_to_equity": de,
                "interest_coverage": icr,

                "asset_turnover": asset_turnover,

                "free_cash_flow_cr": fcf,

                "earnings_per_share": row["eps"],
                "dividend_payout_ratio_pct": row["dividend_payout"]

            })

        ratio_df = pd.DataFrame(ratios)

        ratio_df.to_sql(
            "financial_ratios_generated",
            conn,
            if_exists="replace",
            index=False
        )

        conn.close()

        print()

        print(f"Rows Generated : {len(ratio_df)}")

        print()

        print("=" * 70)
        print("Financial Ratio Table Created Successfully")
        print("=" * 70)