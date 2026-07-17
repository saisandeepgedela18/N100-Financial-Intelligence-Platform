import unittest

from src.analytics.ratios import RatioEngine


class TestRatioEngine(unittest.TestCase):

    # -------------------------
    # Day 09 Tests
    # -------------------------

    def test_debt_to_equity_normal(self):
        self.assertEqual(
            RatioEngine.debt_to_equity(500, 100, 900),
            0.5
        )

    def test_debt_to_equity_debt_free(self):
        self.assertEqual(
            RatioEngine.debt_to_equity(0, 100, 900),
            0
        )

    def test_interest_coverage(self):
        self.assertEqual(
            RatioEngine.interest_coverage_ratio(300, 50, 50),
            7.0
        )

    def test_interest_zero(self):
        self.assertIsNone(
            RatioEngine.interest_coverage_ratio(300, 50, 0)
        )

    def test_debt_free_label(self):
        self.assertEqual(
            RatioEngine.icr_label(0),
            "Debt Free"
        )

    def test_high_leverage_flag(self):
        self.assertTrue(
            RatioEngine.high_leverage_flag(6, "Technology")
        )

    def test_net_debt(self):
        self.assertEqual(
            RatioEngine.net_debt(1000, 200),
            800
        )

    def test_asset_turnover(self):
        self.assertEqual(
            RatioEngine.asset_turnover(1000, 500),
            2.0
        )

    # -------------------------
    # Day 08 Tests
    # -------------------------

    def test_net_profit_margin_normal(self):
        self.assertEqual(
            RatioEngine.net_profit_margin(200, 1000),
            20.00
        )

    def test_net_profit_margin_zero_sales(self):
        self.assertIsNone(
            RatioEngine.net_profit_margin(200, 0)
        )

    def test_operating_profit_margin_normal(self):
        self.assertEqual(
            RatioEngine.operating_profit_margin(300, 1000),
            30.00
        )

    def test_operating_profit_margin_zero_sales(self):
        self.assertIsNone(
            RatioEngine.operating_profit_margin(300, 0)
        )

    def test_return_on_equity_normal(self):
        self.assertEqual(
            RatioEngine.return_on_equity(200, 100, 900),
            20.00
        )

    def test_return_on_equity_negative_equity(self):
        self.assertIsNone(
            RatioEngine.return_on_equity(200, -500, 100)
        )

    def test_return_on_capital_employed(self):
        self.assertEqual(
            RatioEngine.return_on_capital_employed(
                300,
                100,
                900,
                500
            ),
            20.00
        )

    def test_return_on_assets(self):
        self.assertEqual(
            RatioEngine.return_on_assets(200, 1000),
            20.00
        )


if __name__ == "__main__":
    unittest.main()