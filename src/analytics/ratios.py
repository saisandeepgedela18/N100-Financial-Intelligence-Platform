"""
ratios.py

Sprint 2
Financial Ratio Engine
"""

from typing import Optional


class RatioEngine:

    # ==========================================================
    # PROFITABILITY RATIOS
    # ==========================================================

    @staticmethod
    def net_profit_margin(net_profit, sales) -> Optional[float]:
        """
        Net Profit Margin = Net Profit / Sales × 100
        """

        if sales is None or sales == 0:
            return None

        return round((net_profit / sales) * 100, 2)

    @staticmethod
    def operating_profit_margin(operating_profit, sales) -> Optional[float]:
        """
        Operating Profit Margin = Operating Profit / Sales × 100
        """

        if sales is None or sales == 0:
            return None

        return round((operating_profit / sales) * 100, 2)

    @staticmethod
    def return_on_equity(
        net_profit,
        equity_capital,
        reserves
    ) -> Optional[float]:
        """
        ROE = Net Profit / (Equity Capital + Reserves) × 100
        """

        capital = equity_capital + reserves

        if capital <= 0:
            return None

        return round((net_profit / capital) * 100, 2)

    @staticmethod
    def return_on_capital_employed(
        ebit,
        equity_capital,
        reserves,
        borrowings
    ) -> Optional[float]:
        """
        ROCE = EBIT / Capital Employed × 100
        """

        capital = equity_capital + reserves + borrowings

        if capital <= 0:
            return None

        return round((ebit / capital) * 100, 2)

    @staticmethod
    def return_on_assets(
        net_profit,
        total_assets
    ) -> Optional[float]:
        """
        ROA = Net Profit / Total Assets × 100
        """

        if total_assets is None or total_assets == 0:
            return None

        return round((net_profit / total_assets) * 100, 2)

    # ==========================================================
    # VALIDATION
    # ==========================================================

    @staticmethod
    def validate_operating_profit_margin(
        calculated_opm,
        source_opm,
        tolerance=1.0
    ):
        """
        Compare calculated OPM with source OPM.
        """

        if calculated_opm is None or source_opm is None:
            return True, 0

        difference = abs(calculated_opm - source_opm)

        return difference <= tolerance, round(difference, 2)

    @staticmethod
    def validate_roce(
        roce,
        broad_sector,
        benchmark=15
    ):
        """
        Financial companies are evaluated separately.
        """

        if roce is None:
            return None

        if broad_sector == "Financials":
            return "Financial Sector Benchmark"

        return roce >= benchmark

    # ==========================================================
    # LEVERAGE RATIOS
    # ==========================================================

    @staticmethod
    def debt_to_equity(
        borrowings,
        equity_capital,
        reserves
    ):
        """
        Debt-to-Equity Ratio
        """

        if borrowings == 0:
            return 0

        capital = equity_capital + reserves

        if capital <= 0:
            return None

        return round(borrowings / capital, 2)

    @staticmethod
    def high_leverage_flag(
        debt_to_equity,
        broad_sector
    ):
        """
        High leverage warning.
        """

        if broad_sector == "Financials":
            return False

        if debt_to_equity is None:
            return False

        return debt_to_equity > 5

    @staticmethod
    def interest_coverage_ratio(
        operating_profit,
        other_income,
        interest
    ):
        """
        Interest Coverage Ratio
        """

        if interest == 0:
            return None

        return round(
            (operating_profit + other_income) / interest,
            2
        )

    @staticmethod
    def icr_label(
        interest
    ):
        """
        Debt-free label.
        """

        if interest == 0:
            return "Debt Free"

        return None

    @staticmethod
    def interest_warning(
        icr
    ):
        """
        Warning if Interest Coverage < 1.5
        """

        if icr is None:
            return False

        return icr < 1.5

    @staticmethod
    def net_debt(
        borrowings,
        investments
    ):
        """
        Net Debt
        """

        return borrowings - investments

    @staticmethod
    def asset_turnover(
        sales,
        total_assets
    ):
        """
        Asset Turnover
        """

        if total_assets is None or total_assets == 0:
            return None

        return round(
            sales / total_assets,
            2
        )