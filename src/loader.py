import pandas as pd
from pathlib import Path
from src.config import SOURCE_FILES


class ExcelLoader:

    def __init__(self):
        self.source_files = SOURCE_FILES

    def load_all(self):

        dataframes = {}

        print("=" * 60)
        print("Loading Excel Files")
        print("=" * 60)

        special_files = [
            "financial_ratios",
            "market_cap",
            "peer_groups",
            "sectors",
            "stock_prices"
        ]

        # Create processed folder if it doesn't exist
        processed_dir = Path("data") / "processed"
        processed_dir.mkdir(parents=True, exist_ok=True)

        for name, path in self.source_files.items():

            try:

                if name in special_files:
                    df = pd.read_excel(path)

                else:
                    df = pd.read_excel(path, header=1)

                # Store dataframe in memory
                dataframes[name] = df

                # Save processed CSV
                df.to_csv(processed_dir / f"{name}.csv", index=False)

                print(f"✓ {name:20} Rows:{len(df):6} Columns:{len(df.columns):4}")

            except Exception as e:
                print(f"✗ Error loading {name}: {e}")

        print("=" * 60)
        print("ETL Loading Completed Successfully")
        print("=" * 60)

        return dataframes