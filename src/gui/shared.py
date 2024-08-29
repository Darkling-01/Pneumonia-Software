# this file will share functionality modules

from PyQt5.QtWidgets import QStackedWidget, QWidget, QVBoxLayout


class SharedClass(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.stacked_widget = QStackedWidget()
        self.create_layout()

    def create_layout(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.stacked_widget)

    def add_widget(self, widget):
        self.stacked_widget.addWidget(widget)

    def set_current_widget(self, index):
        self.stacked_widget.setCurrentWidget(index)

