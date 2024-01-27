from abc import ABC, abstractmethod


class FinancialReportPresenter(ABC):
    @abstractmethod
    def present(self, response):
        pass
