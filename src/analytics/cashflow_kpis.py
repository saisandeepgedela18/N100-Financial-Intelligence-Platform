"""
cashflow_kpis.py

Sprint 2
Cash Flow KPI Engine
"""

from pathlib import Path
import pandas as pd


class CashFlowKPI:

    @staticmethod
    def free_cash_flow(operating_activity, investing_activity):
        """
        Free Cash Flow = CFO + CFI
        (Investing activity is usually negative)
        """
        return operating_activity + investing_activity

    @staticmethod
    def cfo_quality_score(cfo, pat):
        """
        CFO / PAT
        """

        if pat == 0:
            return None

        score = cfo / pat

        if score > 1:
            return "High Quality"

        if score >= 0.5:
            return "Moderate"

        return "Accrual Risk"

    @staticmethod
    def capex_intensity(investing_activity, sales):
        """
        CapEx Intensity
        """

        if sales == 0:
            return None

        capex = abs(investing_activity)

        pct = (capex / sales) * 100

        if pct < 3:
            return "Asset Light"

        if pct <= 8:
            return "Moderate"

        return "Capital Intensive"

    @staticmethod
    def fcf_conversion_rate(fcf, operating_profit):
        """
        FCF Conversion Rate
        """

        if operating_profit == 0:
            return None

        return round((fcf / operating_profit) * 100, 2)

    @staticmethod
    def capital_allocation_pattern(cfo, cfi, cff):
        """
        8-pattern classifier
        """

        signs = (
            "+" if cfo >= 0 else "-",
            "+" if cfi >= 0 else "-",
            "+" if cff >= 0 else "-"
        )

        mapping = {
            ("+", "-", "-"): "Reinvestor",
            ("+", "+", "-"): "Liquidating Assets",
            ("-", "+", "+"): "Distress Signal",
            ("-", "-", "+"): "Growth Funded by Debt",
            ("+", "+", "+"): "Cash Accumulator",
            ("-", "-", "-"): "Pre-Revenue",
            ("+", "-", "+"): "Mixed"
        }

        return mapping.get(signs, "Unknown")

    @staticmethod
    def export_capital_allocation(df):

        output = Path("data") / "output"
        output.mkdir(parents=True, exist_ok=True)

        file = output / "capital_allocation.csv"

        df.to_csv(file, index=False)

        return file