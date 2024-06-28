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

        # create QLabel to display filename
        self.image_name = QLabel(self.central_widget)
        self.layout.addWidget(self.image_name)

        # placeholder for loaded image
        self.load_image = None

        # calling functions
        self.ui_components()

    def ui_components(self):
        load_button = QtWidgets.QPushButton("Select An Image", self.central_widget)

        load_button.setStyleSheet("color: black; background-color: white;")
        load_button.setGeometry(654, 73, 100, 30)
        load_button.clicked.connect(self.open_file_dialog)
        # self.layout.addWidget(self.load_button)

        image_location = QtWidgets.QLabel("FILENAME: ", self.central_widget)
        image_location.setStyleSheet("color: white; font-size: 18px;")
        image_location.setGeometry(24, 190, 120, 25)

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
                # self.display_image(self.load_image)
                self.change_color()
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
        scaled_image = pixmap.scaled(550, 400, Qt.KeepAspectRatio)
        self.image_label.setPixmap(scaled_image)

    def change_color(self):
        # convert image to grayscale
        gray_scale = cv2.cvtColor(self.load_image, cv2.COLOR_BGR2GRAY)
        color_mapped_img = cv2.applyColorMap(gray_scale, cv2.COLORMAP_CIVIDIS)
        # display the processed image
        self.display_image(color_mapped_img)


if __name__ == "__main__":

    # create the application object
    app = QtWidgets.QApplication(sys.argv)
    # create the instance of window
    window_1 = MainWindow()
    window_1.show()
    # run the program
    exit(app.exec())

