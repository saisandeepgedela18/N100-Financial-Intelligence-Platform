"""
Project Configuration
N100 Financial Intelligence Platform
"""

from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data Directories
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_DIR = PROJECT_ROOT / "data" / "output"

# Database
DATABASE_PATH = PROJECT_ROOT / "db" / "nifty100.db"

# Log Directory
LOG_DIR = PROJECT_ROOT / "logs"

# Source Excel Files
SOURCE_FILES = {
    "companies": RAW_DATA_DIR / "companies.xlsx",
    "profitandloss": RAW_DATA_DIR / "profitandloss.xlsx",
    "balancesheet": RAW_DATA_DIR / "balancesheet.xlsx",
    "cashflow": RAW_DATA_DIR / "cashflow.xlsx",
    "analysis": RAW_DATA_DIR / "analysis.xlsx",
    "documents": RAW_DATA_DIR / "documents.xlsx",
    "prosandcons": RAW_DATA_DIR / "prosandcons.xlsx",
    "sectors": RAW_DATA_DIR / "sectors.xlsx",
    "stock_prices": RAW_DATA_DIR / "stock_prices.xlsx",
    "financial_ratios": RAW_DATA_DIR / "financial_ratios.xlsx",
    "peer_groups": RAW_DATA_DIR / "peer_groups.xlsx",
    "market_cap": RAW_DATA_DIR / "market_cap.xlsx",
}