import unittest

from src.analytics.cashflow_kpis import CashFlowKPI


class TestCashFlowKPI(unittest.TestCase):

    # ----------------------------------
    # Free Cash Flow
    # ----------------------------------

    def test_free_cash_flow(self):
        self.assertEqual(
            CashFlowKPI.free_cash_flow(
                1000,
                -300
            ),
            700
        )

    # ----------------------------------
    # CFO Quality
    # ----------------------------------

    def test_cfo_quality_high(self):
        self.assertEqual(
            CashFlowKPI.cfo_quality_score(
                120,
                100
            ),
            "High Quality"
        )

    def test_cfo_quality_moderate(self):
        self.assertEqual(
            CashFlowKPI.cfo_quality_score(
                70,
                100
            ),
            "Moderate"
        )

    def test_cfo_quality_risk(self):
        self.assertEqual(
            CashFlowKPI.cfo_quality_score(
                30,
                100
            ),
            "Accrual Risk"
        )

    def test_cfo_quality_zero_pat(self):
        self.assertIsNone(
            CashFlowKPI.cfo_quality_score(
                100,
                0
            )
        )

    # ----------------------------------
    # CapEx Intensity
    # ----------------------------------

    def test_capex_asset_light(self):
        self.assertEqual(
            CashFlowKPI.capex_intensity(
                -20,
                1000
            ),
            "Asset Light"
        )

    def test_capex_moderate(self):
        self.assertEqual(
            CashFlowKPI.capex_intensity(
                -50,
                1000
            ),
            "Moderate"
        )

    def test_capex_capital_intensive(self):
        self.assertEqual(
            CashFlowKPI.capex_intensity(
                -200,
                1000
            ),
            "Capital Intensive"
        )

    # ----------------------------------
    # FCF Conversion
    # ----------------------------------

    def test_fcf_conversion(self):
        self.assertEqual(
            CashFlowKPI.fcf_conversion_rate(
                700,
                1000
            ),
            70.0
        )

    # ----------------------------------
    # Capital Allocation
    # ----------------------------------

    def test_reinvestor(self):
        self.assertEqual(
            CashFlowKPI.capital_allocation_pattern(
                100,
                -50,
                -25
            ),
            "Reinvestor"
        )

    def test_cash_accumulator(self):
        self.assertEqual(
            CashFlowKPI.capital_allocation_pattern(
                100,
                50,
                20
            ),
            "Cash Accumulator"
        )

    def test_distress(self):
        self.assertEqual(
            CashFlowKPI.capital_allocation_pattern(
                -100,
                50,
                20
            ),
            "Distress Signal"
        )


if __name__ == "__main__":
    unittest.main()