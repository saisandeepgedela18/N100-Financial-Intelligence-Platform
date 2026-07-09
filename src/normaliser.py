"""
Data Normalizer
"""

import pandas as pd


class DataNormaliser:

    @staticmethod
    def clean_columns(df: pd.DataFrame):

        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
            .str.replace("-", "_")
        )

        return df

    @staticmethod
    def remove_empty_rows(df):

        return df.dropna(how="all")

    @staticmethod
    def remove_duplicates(df):

        return df.drop_duplicates()

    @staticmethod
    def normalize_year(df):

        if "year" in df.columns:

            df["year"] = (
                df["year"]
                .astype(str)
                .str.extract(r"(\d{4})")
            )

        return df

    @staticmethod
    def normalize_ticker(df):

        if "ticker" in df.columns:

            df["ticker"] = (
                df["ticker"]
                .astype(str)
                .str.upper()
                .str.strip()
            )

        return df