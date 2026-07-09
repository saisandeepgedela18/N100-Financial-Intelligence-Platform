from src.loader import ExcelLoader
from src.validator import DataValidator
from src.database import DatabaseManager
from src.manual_review import ManualReview 

print("=" * 70)
print("N100 Financial Intelligence Platform")
print("Sprint 1")
print("=" * 70)

loader = ExcelLoader()
dataframes = loader.load_all()

validator = DataValidator()
validator.validate(dataframes)

database = DatabaseManager()
database.create_database()
database.load_data(dataframes)
review = ManualReview()

review.run()
print("\nSprint 1 Day 6 Completed Successfully")