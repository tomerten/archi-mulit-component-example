from .financial_data_gateway import FinancialDataGateway
from .financial_entities import FinancialEntities


class FinancialReportGenerator:
    def __init__(self, data_gateway: FinancialDataGateway, entities: FinancialEntities):
        self.data_gateway = data_gateway
        self.entities = entities

    def generate_report(self):
        pass
