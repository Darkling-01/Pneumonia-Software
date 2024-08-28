# this file will share functionality modules

from PyQt5.QtWidgets import QStackedWidget, QWidget, QVBoxLayout


class SharedClass:
    def __init__(self, parent=None):
        super().__init__()

        # initialize the stacked widget and layout
        self.parent = parent
        self.stacked_widget = QStackedWidget()
        self.create_layout()

    def create_layout(self):
        # create and configure layout
        self.central_widget = QWidget(self.parent)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.addWidget(self.stacked_widget)

    def add_widget(self, widget):
        # method to add widgets to the stacked widget
        self.stacked_widget.addWidget(widget)

    def set_current_widget(self, index):
        # method to set the current widget in the stacked widget
        self.stacked_widget.setCurrentWidget(index)

