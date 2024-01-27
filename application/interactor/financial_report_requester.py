from abc import ABC, abstractmethod
from .financial_report_request import FinancialReportRequest


class FinancialReportRequester(ABC):
    @abstractmethod
    def request_financial_report(self, request: FinancialReportRequest):
        pass
