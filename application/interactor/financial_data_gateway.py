from abc import ABC, abstractmethod


class FinancialDataGateway(ABC):
    @abstractmethod
    def get_financial_data(self, stock_symbol: str) -> dict:
        pass
