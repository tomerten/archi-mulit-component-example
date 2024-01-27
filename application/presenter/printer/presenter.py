from .view import PrintView
from .view_model import PrintViewModel


class PrintPresenter:
    def __init__(self, view: PrintView, view_model: PrintViewModel):
        self.view = view
        self.view_model = view_model

    def present(self, data):
        # Present data on the screen
        pass
