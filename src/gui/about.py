from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from assets.other_resources import descriptions
from src.gui import GUI


class AboutPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.description = QLabel(descriptions.text, self)
        self.description.setStyleSheet("color: white; font-size: 18px;")
        self.description.setAlignment(Qt.AlignLeft)

    def setup_second_page(self):
        second_page = QWidget()
        second_page_layout = QVBoxLayout(second_page)

        button_layout = QHBoxLayout()
        button_layout.setStretch()

        main_page_button = QtWidgets.QPushButton("Main Page", second_page)
        main_page_button.setStyleSheet("color: black; background-color: white;")
        main_page_button.setFixedSize(100, 30)
        main_page_button.clicked.connect(GUI.MainWindow)
        button_layout.addWidget(main_page_button)

        return second_page

