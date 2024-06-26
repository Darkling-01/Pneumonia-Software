import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
import cv2
import numpy as np


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set background-color
        self.setStyleSheet("background-color: #2c2e30")
        self.setWindowTitle("Pneumonia Detection")
        # set window size (0, 0, width, height)
        self.setGeometry(0, 0, 1400, 900)

        # create central widget and layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)      # lines up widget vertically

        # Title
        self.textTitle = QLabel("Pneumonia Detection", self.central_widget)
        self.textTitle.setAlignment(Qt.AlignHCenter)
        self.textTitle.setStyleSheet("color: white; font-size: 22px;")
        self.layout.addWidget(self.textTitle)

        # create QLabel for displaying image
        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

        # load and display the original image
        self.original_image = cv2.imread(r"C:\Users\Alejandro Barragan\PycharmProjects\Pneumonia-Software"
                                         r"\data\test\normal\IM-0007-0001.jpeg")
        self.display_image(self.original_image)

        # calling functions
        self.UiComponents()

    def UiComponents(self):
        button = QtWidgets.QPushButton("Select A File", self)
        # (x, y, width, height)
        button.setGeometry(667, 100, 80, 30)
        button.setStyleSheet("color: black; background-color: white;")
        button.clicked.connect(self.FileDialog)

    # create file dialog to open File Explorer
    def FileDialog(self):
        self.fileDialog = QtWidgets.QFileDialog.getOpenFileName(self, "Pick An image", "home/", "Images (*.png *.xpm *.jpeg)")

    def display_image(self, image):
        # convert image from BGR to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # convert image to QImage
        height, width, channel = image_rgb.shape
        bytes_per_line = 3 * width
        # Format_RGB888 stores image using a 24-bit RBG format (8-8-8)
        qimage = QImage(image_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # convert QImage to QPixmap and set it to the QLabel
        pixmap = QPixmap.fromImage(qimage)
        scaled_image = pixmap.scaled(550, 400)
        self.image_label.setPixmap(scaled_image)

    def change_color(self):
        # convert image to grayscale
        gray_scale = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        self.display_image(gray_scale)


if __name__ == "__main__":

    # create the application object
    app = QtWidgets.QApplication(sys.argv)
    # create the instance of window
    window_1 = MainWindow()
    window_1.show()
    # run the program
    exit(app.exec())

