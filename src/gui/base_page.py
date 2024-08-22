from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout

# this

class BasePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.create_central_widget()

    def create_central_widget(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

