# Purpose: financial data mapper
from .financial_database import FinancialDatabase


class FinancialDataMapper:
    def __init__(self, db: FinancialDatabase):
        self.db = db

    def get_financial_data(self, query: str):
        return self.db.query_data(query)
