import sys

import matplotlib
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set background-color
        self.setStyleSheet("background-color: #2c2e30")
        self.setWindowTitle("Pneumonia Detection")
        # set window size (0, 0, width, height)
        self.setGeometry(0, 0, 1400, 900)

        # Title
        self.textTitle = QLabel("Pneumonia Detection", self)
        self.textTitle.move(550, 30)
        self.textTitle.resize(220, 30)
        self.textTitle.setAlignment(Qt.AlignHCenter)
        self.textTitle.setStyleSheet("color: white; font-size: 22px;")

        self.UiComponents()
        self.DisplayImage()
        # showing all the widgets
        self.show()

    def UiComponents(self):
        button = QPushButton("Select A File", self)
        # (x, y, width, height)
        button.setGeometry(627, 100, 80, 30)
        button.setStyleSheet("color: black; background-color: white;")
        button.clicked.connect(self.FileDialog)

    # create file dialog to open File Explorer

    def FileDialog(self):
        self.fileDialog = QFileDialog.getOpenFileName(self, "Pick An image", "home/", "Images (*.png *.xpm *.jpeg)")

    def DisplayImage(self):
        chosen_image = QLabel(self)
        chosen_image.setPixmap(QPixmap(r"C:\Users\Alejandro Barragan\PycharmProjects\Pneumonia-Software\data\test\normal\IM-0003-0001.jpeg"))
        chosen_image.resize(400, 400)
        chosen_image.move(500, 500)


if __name__ == "__main__":

    # create the application object
    app = QApplication(sys.argv)
    # create the instance of window
    window_1 = MainWindow()

    # run the program
    exit(app.exec())

