import pandas as pd

files = [
    "analysis",
    "balancesheet",
    "cashflow",
    "companies",
    "documents",
    "financial_ratios",
    "market_cap",
    "peer_groups",
    "profitandloss",
    "prosandcons",
    "sectors",
    "stock_prices"
]

for file in files:
    print("\n" + "=" * 80)
    print(file.upper())
    print("=" * 80)

    df = pd.read_excel(f"data/raw/{file}.xlsx")

    print("Rows:", len(df))
    print("Columns:")
    for col in df.columns:
        print(" -", col)