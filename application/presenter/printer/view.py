from abc import ABC, abstractmethod


class PrintView(ABC):
    @abstractmethod
    def display(self, view_model):
        pass
