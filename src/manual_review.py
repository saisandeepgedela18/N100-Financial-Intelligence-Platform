"""
manual_review.py

N100 Financial Intelligence Platform
Sprint 1 - Day 6
Manual Data Quality Review
"""

from pathlib import Path
import pandas as pd


class ManualReview:

    def __init__(self):

        self.processed = Path("data") / "processed"

    def review_companies(self):

        companies = pd.read_csv(self.processed / "companies.csv")

        # Remove accidental header row if present
        if str(companies.iloc[0, 0]).lower() == "id":
            companies = companies.iloc[1:].reset_index(drop=True)

        print("=" * 70)
        print("MANUAL REVIEW")
        print("=" * 70)

        print(f"\nTotal Companies : {len(companies)}")

        print("\nRandom Sample (5 Companies)\n")

        sample = companies.sample(
            n=min(5, len(companies)),
            random_state=42
        )

        print(sample)

        return companies

    def year_coverage(self):

        print("\n" + "=" * 70)
        print("YEAR COVERAGE")
        print("=" * 70)

        try:

            pnl = pd.read_csv(self.processed / "profitandloss.csv")

            if "year" in pnl.columns and "company_id" in pnl.columns:

                coverage = (
                    pnl.groupby("company_id")["year"]
                    .nunique()
                    .reset_index()
                )

                low = coverage[coverage["year"] < 5]

                print(f"\nCompanies with less than 5 years : {len(low)}")

                if len(low) > 0:
                    print(low)

            else:
                print("Year or company_id column not found.")

        except Exception as e:
            print(e)

    def dataset_summary(self):

        print("\n" + "=" * 70)
        print("DATASET SUMMARY")
        print("=" * 70)

        files = [
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

        for file in files:

            try:

                df = pd.read_csv(self.processed / f"{file}.csv")

                print(
                    f"{file:<20}"
                    f"Rows : {len(df):6}"
                    f"   Columns : {len(df.columns):3}"
                )

            except Exception:

                print(f"{file:<20} Not Found")

    def run(self):

        self.review_companies()

        self.year_coverage()

        self.dataset_summary()

        print("\n" + "=" * 70)
        print("Manual Review Completed Successfully")
        print("=" * 70)


if __name__ == "__main__":

    review = ManualReview()

    review.run()