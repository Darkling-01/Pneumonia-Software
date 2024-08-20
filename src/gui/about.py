from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from assets.other_resources import descriptions


class AboutPage(QWidget):
    def __init__(self):
        super().__init__()

        self.description = QLabel(descriptions.text, self)
        self.description.setStyleSheet("color: white; font-size: 18px;")
        self.description.setGeometry(750, 400, 520, 330)

