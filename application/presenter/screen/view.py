from abc import ABC, abstractmethod


class ScreenView(ABC):
    @abstractmethod
    def display(self, view_model):
        pass
