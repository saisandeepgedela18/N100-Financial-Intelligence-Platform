from src.loader import ExcelLoader
from src.validator import DataValidator
from src.database import DatabaseManager
from src.manual_review import ManualReview
from src.analytics.ratio_engine import FinancialRatioEngine
from src.analytics.edge_case_logger import RatioEdgeCaseLogger
from src.analytics.sprint2_review import Sprint2Review

print("=" * 70)
print("N100 Financial Intelligence Platform")
print("Sprint 2")
print("=" * 70)


# -------------------------------
# Load Data
# -------------------------------
loader = ExcelLoader()
dataframes = loader.load_all()

# -------------------------------
# Validate Data
# -------------------------------
validator = DataValidator()
validator.validate(dataframes)

# -------------------------------
# Create & Load Database
# -------------------------------
database = DatabaseManager()
database.create_database()
database.load_data(dataframes)

# -------------------------------
# Generate Financial Ratios
# -------------------------------
ratio_engine = FinancialRatioEngine()
ratio_engine.run()

edge_logger = RatioEdgeCaseLogger()
edge_logger.run()

# -------------------------------
# Manual Review
# -------------------------------
review = ManualReview()
review.run()

sprint_review = Sprint2Review()
sprint_review.run()

print("\nSprint 2 Completed Successfully")