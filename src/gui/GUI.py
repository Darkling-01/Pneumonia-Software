import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog
import cv2
import matplotlib as plt
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
        self.layout = QVBoxLayout(self.central_widget)      # lines up widgets vertically

        # Title
        self.textTitle = QLabel("Pneumonia Detection", self.central_widget)
        self.textTitle.setAlignment(Qt.AlignHCenter)
        self.textTitle.setStyleSheet("color: white; font-size: 22px;")
        self.layout.addWidget(self.textTitle)

        # create QLabel for displaying image
        self.image_label = QLabel(self.central_widget)
        self.layout.addWidget(self.image_label)

        # load and display the original image
        # self.original_image = cv2.imread(r"C:\Users\Alejandro Barragan\PycharmProjects\Pneumonia-Software"
        #                                  r"\data\test\normal\IM-0007-0001.jpeg")
        # convert color image to 'hot'
        # self.original_image = cv2.applyColorMap(self.original_image, cv2.COLORMAP_VIRIDIS)
        # self.display_image(self.original_image)

        # calling functions
        self.ui_components()

        # placeholder for loaded image
        self.load_image = None

    def ui_components(self):
        self.load_button = QtWidgets.QPushButton("Select An Image", self.central_widget)
        # x, y, width, height
        self.load_button.setGeometry(230,233, 33, 23)
        self.load_button.setStyleSheet("color: black; background-color: white;")
        self.load_button.clicked.connect(self.open_file_dialog)
        self.layout.addWidget(self.load_button)

    # create file dialog to open File Explorer
    def open_file_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog

        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Pick An image", "home/",
                                                            "Images (*.png *.xpm *.jpeg)")
        if filename:
            print(f"Selected File: {filename}")
            self.load_image = cv2.imread(filename)

            if self.load_image is not None:
                self.display_image(self.load_image)
            else:
                print(f"Error loading images from file: {filename}")

    def display_image(self, image):

        # convert image to QImage
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        # Format_RGB888 stores image using a 24-bit RBG format (8-8-8)
        qimage = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

        # convert QImage to QPixmap and set it to the QLabel
        pixmap = QPixmap.fromImage(qimage)
        scaled_image = pixmap.scaled(550, 400)
        self.image_label.setPixmap(scaled_image)

    def change_color(self):
        # convert image to grayscale
        gray_scale = cv2.cvtColor(self.load_image, cv2.COLOR_BGR2GRAY)

        # display the processed image
        self.display_image(gray_scale)


if __name__ == "__main__":

    # create the application object
    app = QtWidgets.QApplication(sys.argv)
    # create the instance of window
    window_1 = MainWindow()
    window_1.show()
    # run the program
    exit(app.exec())

