from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from assets.other_resources import descriptions
from .base_page import BasePage


class AboutPage(BasePage):
    def __init__(self):
        super().__init__()

        self.description = QLabel(descriptions.text, self.central_widget)
        self.description.setStyleSheet("color: white; font-size: 18px;")
        self.description.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.description)

    def setup_second_page(self):
        second_page = QWidget()
        second_page_layout = QVBoxLayout(second_page)

        button_layout = QHBoxLayout()
        button_layout.addStretch()

        main_page_button = QtWidgets.QPushButton("Main Page", second_page)
        main_page_button.setStyleSheet("color: black; background-color: white;")
        main_page_button.setFixedSize(100, 30)
        # main_page_button.clicked.connect()
        button_layout.addWidget(main_page_button)

        button_layout.addStretch()

        second_page_layout.setAlignment(Qt.AlignTop)

        second_page_layout.addLayout(button_layout)

        return second_page

