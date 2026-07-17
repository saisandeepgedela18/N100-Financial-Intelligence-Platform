import unittest

from src.analytics.cagr import CAGRCalculator


class TestCAGRCalculator(unittest.TestCase):

    # -------------------------
    # Normal CAGR
    # -------------------------

    def test_normal_cagr(self):
        value, flag = CAGRCalculator.calculate_cagr(
            100,
            200,
            5
        )

        self.assertEqual(flag, "NORMAL")
        self.assertAlmostEqual(value, 14.87, places=2)

    # -------------------------
    # Revenue CAGR
    # -------------------------

    def test_revenue_cagr(self):
        value, flag = CAGRCalculator.revenue_cagr(
            500,
            1000,
            5
        )

        self.assertEqual(flag, "NORMAL")

    # -------------------------
    # PAT CAGR
    # -------------------------

    def test_pat_cagr(self):
        value, flag = CAGRCalculator.pat_cagr(
            100,
            200,
            5
        )

        self.assertEqual(flag, "NORMAL")

    # -------------------------
    # EPS CAGR
    # -------------------------

    def test_eps_cagr(self):
        value, flag = CAGRCalculator.eps_cagr(
            20,
            40,
            5
        )

        self.assertEqual(flag, "NORMAL")

    # -------------------------
    # Decline to Loss
    # -------------------------

    def test_decline_to_loss(self):
        value, flag = CAGRCalculator.calculate_cagr(
            100,
            -20,
            5
        )

        self.assertIsNone(value)
        self.assertEqual(flag, "DECLINE_TO_LOSS")

    # -------------------------
    # Turnaround
    # -------------------------

    def test_turnaround(self):
        value, flag = CAGRCalculator.calculate_cagr(
            -100,
            50,
            5
        )

        self.assertIsNone(value)
        self.assertEqual(flag, "TURNAROUND")

    # -------------------------
    # Both Negative
    # -------------------------

    def test_both_negative(self):
        value, flag = CAGRCalculator.calculate_cagr(
            -100,
            -50,
            5
        )

        self.assertIsNone(value)
        self.assertEqual(flag, "BOTH_NEGATIVE")

    # -------------------------
    # Zero Base
    # -------------------------

    def test_zero_base(self):
        value, flag = CAGRCalculator.calculate_cagr(
            0,
            100,
            5
        )

        self.assertIsNone(value)
        self.assertEqual(flag, "ZERO_BASE")

    # -------------------------
    # Insufficient Years
    # -------------------------

    def test_insufficient_years(self):
        value, flag = CAGRCalculator.calculate_cagr(
            100,
            200,
            0
        )

        self.assertIsNone(value)
        self.assertEqual(flag, "INSUFFICIENT")

    # -------------------------
    # Unknown Case
    # -------------------------

    def test_unknown_case(self):
        value, flag = CAGRCalculator.calculate_cagr(
            100,
            0,
            5
        )

        self.assertIsNone(value)
        self.assertEqual(flag, "UNKNOWN")


if __name__ == "__main__":
    unittest.main()