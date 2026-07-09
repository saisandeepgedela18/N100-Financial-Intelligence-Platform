"""
validator.py

N100 Financial Intelligence Platform
Sprint 1 - Data Quality Validation
"""

from pathlib import Path
import pandas as pd


class DataValidator:

    def __init__(self):
        self.failures = []

    def log_failure(self, dataset, rule, severity, message):

        self.failures.append({
            "dataset": dataset,
            "rule": rule,
            "severity": severity,
            "message": message
        })

    def validate_duplicates(self, dataset_name, df):

        duplicate_count = df.duplicated().sum()

        if duplicate_count > 0:
            self.log_failure(
                dataset_name,
                "DQ-01",
                "WARNING",
                f"{duplicate_count} duplicate rows found"
            )

    def validate_empty_rows(self, dataset_name, df):

        empty_rows = df.isnull().all(axis=1).sum()

        if empty_rows > 0:
            self.log_failure(
                dataset_name,
                "DQ-02",
                "WARNING",
                f"{empty_rows} completely empty rows found"
            )

    def validate_missing_values(self, dataset_name, df):

        missing = df.isnull().sum().sum()

        if missing > 0:
            self.log_failure(
                dataset_name,
                "DQ-03",
                "WARNING",
                f"{missing} missing values detected"
            )

    def validate_positive_sales(self, dataset_name, df):

        if "sales" in df.columns:

            negative = (df["sales"] < 0).sum()

            if negative > 0:

                self.log_failure(
                    dataset_name,
                    "DQ-06",
                    "CRITICAL",
                    f"{negative} negative sales values found"
                )

    def validate_year(self, dataset_name, df):

        if "year" in df.columns:

            invalid = df["year"].isnull().sum()

            if invalid > 0:

                self.log_failure(
                    dataset_name,
                    "DQ-04",
                    "WARNING",
                    f"{invalid} invalid year values"
                )

    def validate_ticker(self, dataset_name, df):

        if "ticker" in df.columns:

            invalid = df["ticker"].astype(str).str.strip().eq("").sum()

            if invalid > 0:

                self.log_failure(
                    dataset_name,
                    "DQ-05",
                    "WARNING",
                    f"{invalid} blank ticker values"
                )

    def validate(self, dataframes):

        print("\n" + "=" * 70)
        print("Running Data Quality Validation")
        print("=" * 70)

        for dataset_name, df in dataframes.items():

            print(f"Validating : {dataset_name}")

            self.validate_duplicates(dataset_name, df)
            self.validate_empty_rows(dataset_name, df)
            self.validate_missing_values(dataset_name, df)
            self.validate_positive_sales(dataset_name, df)
            self.validate_year(dataset_name, df)
            self.validate_ticker(dataset_name, df)

        output = Path("data/output")
        output.mkdir(parents=True, exist_ok=True)

        report = output / "validation_failures.csv"

        pd.DataFrame(self.failures).to_csv(report, index=False)

        print("\nValidation Complete")

        print(f"Failures Found : {len(self.failures)}")
        print(f"Saved Report : {report}")

        return self.failures