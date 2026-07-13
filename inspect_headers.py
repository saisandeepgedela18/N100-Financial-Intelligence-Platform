import pandas as pd

files = [
    "profitandloss",
    "balancesheet",
    "cashflow",
    "analysis",
    "documents",
    "prosandcons"
]

for file in files:

    print("\n")
    print("=" * 80)
    print(file.upper())
    print("=" * 80)

    df = pd.read_excel(
        f"data/raw/{file}.xlsx",
        header=None
    )

    print(df.head(8))