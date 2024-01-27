from .view import ScreenView
from .view_model import ScreenViewModel


class ScreenPresenter:
    def __init__(self, view: ScreenView, view_model: ScreenViewModel):
        self.view = view
        self.view_model = view_model

    def present(self, data):
        # Present data on the screen
        pass
