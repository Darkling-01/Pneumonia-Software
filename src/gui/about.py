from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton


class AboutPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("color: white")
        self.app_info = QLabel("This is a test run...", self)

