"""
cagr.py

Sprint 2
CAGR Engine
"""

from typing import Optional


class CAGRCalculator:

    @staticmethod
    def calculate_cagr(start_value, end_value, years):
        """
        Calculate CAGR with edge case handling.

        Returns:
            (cagr_value, flag)
        """

        # -------------------------
        # Insufficient years
        # -------------------------
        if years <= 0:
            return None, "INSUFFICIENT"

        # -------------------------
        # Zero Base
        # -------------------------
        if start_value == 0:
            return None, "ZERO_BASE"

        # -------------------------
        # Positive → Positive
        # -------------------------
        if start_value > 0 and end_value > 0:

            cagr = (
                ((end_value / start_value) ** (1 / years)) - 1
            ) * 100

            return round(cagr, 2), "NORMAL"

        # -------------------------
        # Positive → Negative
        # -------------------------
        if start_value > 0 and end_value < 0:
            return None, "DECLINE_TO_LOSS"

        # -------------------------
        # Negative → Positive
        # -------------------------
        if start_value < 0 and end_value > 0:
            return None, "TURNAROUND"

        # -------------------------
        # Negative → Negative
        # -------------------------
        if start_value < 0 and end_value < 0:
            return None, "BOTH_NEGATIVE"

        return None, "UNKNOWN"

    @staticmethod
    def revenue_cagr(start_sales, end_sales, years):
        return CAGRCalculator.calculate_cagr(
            start_sales,
            end_sales,
            years
        )

    @staticmethod
    def pat_cagr(start_pat, end_pat, years):
        return CAGRCalculator.calculate_cagr(
            start_pat,
            end_pat,
            years
        )

    @staticmethod
    def eps_cagr(start_eps, end_eps, years):
        return CAGRCalculator.calculate_cagr(
            start_eps,
            end_eps,
            years
        )