import sys
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QWidget, \
    QStackedWidget

import cv2

# 'about.py' gives a description about the application
from src.gui.about import AboutPage
from src.scripts.preprocessing import X_train, y_train, X_val, y_val
from .base_page import BasePage


class TrainingThread(QThread):
    progress = pyqtSignal(object)   # signal to emit training status

    def __init__(self, X_train, y_train, X_val, y_val):
        super().__init__()
        self.X_train = X_train
        self.y_train = y_train
        self.X_val = X_val
        self.y_val = y_val

    def run(self):
        from src.scripts import model    # import here to avoid import errors
        try:
            final_accuracy = model.train_model(self.X_train, self.y_train,
                                        self.X_val, self.y_val)
            self.progress.emit(final_accuracy)   # emit the result

        except Exception as e:
            print(f"Training Failed -> {e}")


class ImageProcessor(QThread):
    image_processed = pyqtSignal(object)

    def __init__(self, file_location):
        super().__init__()
        self.file_location = file_location

    def run(self):
        image = cv2.imread(self.file_location)
        if image is not None:
            # convert image to grayscale
            grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # apply colormap (e.g. viridis)
            color_mapped_image = cv2.applyColorMap(grayscale, cv2.COLORMAP_VIRIDIS)

            # emit signal with processed image
            self.image_processed.emit((color_mapped_image, self.file_location))
        else:
            print(f"Error loading image from file: {self.file_location}")


class MainWindow(BasePage):
    def __init__(self):
        super().__init__()

        self.about_page = None

        # set background-color
        self.setStyleSheet("background-color: #2c2e30")
        self.main_title = self.setWindowTitle("Pneumonia Detection")
        # set window size (0, 0, width, height)
        self.setGeometry(0, 0, 1400, 900)

        # Title
        self.textTitle = QLabel("Pneumonia Detection", self.central_widget)
        self.textTitle.setStyleSheet("color: white; font-size: 22px;")
        self.textTitle.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.textTitle)

        # create a stacked widget
        self.stacked_widget = QStackedWidget()
        self.main_layout.addWidget(self.stacked_widget)

        # create two pages
        self.main_page = self.setup_main_page()
        self.about_page = AboutPage()

        # add pages to stacked widget
        self.stacked_widget.addWidget(self.main_page)
        self.stacked_widget.addWidget(self.about_page)

        # show the main page initially
        self.stacked_widget.setCurrentWidget(self.main_page)

        # create a layout for the information labels
        self.info_layout = QVBoxLayout()
        self.main_layout.addLayout(self.info_layout)

        # QLabel for displaying image
        self.image_label = QLabel(self.central_widget)
        self.info_layout.addWidget(self.image_label)

        # create QLabel to display filename
        self.image_location = QtWidgets.QLabel(self.central_widget)
        self.image_location.setStyleSheet("color: white; font-size: 14px;")
        self.info_layout.addWidget(self.image_location)

        # display information about model, accuracy, tests, and runtime
        # label for model used to train
        self.framework_label = QLabel(self.central_widget)
        self.framework_label.setGeometry(750, 400, 520, 23)
        self.framework_label.setStyleSheet("color: white; font-size: 18px;")

        # label for accuracy
        self.model_accuracy = QLabel(self.central_widget)
        self.model_accuracy.setGeometry(750, 460, 520, 23)
        self.model_accuracy.setStyleSheet("color: white; font-size: 18px;")

        # label for tests used
        self.model_test = QLabel(self.central_widget)
        self.model_test.setGeometry(750, 520, 520, 23)
        self.model_test.setStyleSheet("color: white; font-size: 18px;")

        self.training_thread = None

        # placeholder for loaded image
        self.load_image = None

    def start_training(self):

        self.training_thread = TrainingThread(X_train, y_train, X_val, y_val)
        self.training_thread.progress.connect(self.on_training_done)
        self.training_thread.start()

    def on_training_done(self, accuracy):
        # update GUI results
        if accuracy is not None:
            self.framework_label.setText(f"FRAMEWORK -> Keras")
            self.model_accuracy.setText(f"ACCURACY -> {accuracy:.2f}")
        else:
            self.model_accuracy.setText(f"N/A")

    def setup_main_page(self):
        main_page = QWidget()
        main_page_layout = QVBoxLayout(main_page)

        # create a horizontal layout for buttons
        button_layout = QHBoxLayout()
        # add stretchable space to push buttons to the center
        button_layout.addStretch()

        load_button = QtWidgets.QPushButton("Select An Image", main_page)
        load_button.setStyleSheet("color: black; background-color: white;")
        load_button.setFixedSize(100, 30)
        load_button.clicked.connect(self.open_file_dialog)
        button_layout.addWidget(load_button)

        # transitions to 'about' window
        about_button = QtWidgets.QPushButton("About", main_page)
        about_button.setStyleSheet("color: black; background-color: white;")
        about_button.setFixedSize(100, 30)
        about_button.clicked.connect(self.show_about_page)
        button_layout.addWidget(about_button)

        # add stretchable space to push buttons together
        button_layout.addStretch()

        main_page_layout.setAlignment(Qt.AlignTop)
        # add the button layout to the main page layout
        main_page_layout.addLayout(button_layout)

        return main_page

    # create file dialog to open File Explorer
    def open_file_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog

        file_location, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Pick An image", "home/",
                                                            "Images (*.png *.xpm *.jpeg)")
        if file_location:
            print(f"Selected File: {file_location}")
            # start image processing thread immediately
            self.image_processor_thread = ImageProcessor(file_location)
            self.image_processor_thread.image_processed.connect(self.display_image)
            self.image_processor_thread.start()

    def display_image(self, image):
        color_mapped_image, file_location = image

        # display filename in QLabel
        self.image_location.setText(f"FILE LOCATION:\n{file_location}")

        # convert image to QImage
        height, width, channel = color_mapped_image.shape
        bytes_per_line = 3 * width
        # Format_RGB888 stores image using a 24-bit RBG format (8-8-8)
        qimage = QImage(color_mapped_image.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

        # convert QImage to QPixmap and set it to the QLabel
        pixmap = QPixmap.fromImage(qimage)
        scaled_image = pixmap.scaled(550, 400, Qt.KeepAspectRatio)
        self.image_label.setPixmap(scaled_image)

    def show_about_page(self):
        # hide elements not needed on the about page
        self.image_location.hide()
        self.image_label.hide()
        self.textTitle.hide()

        # show the about page
        self.stacked_widget.setCurrentWidget(self.about_page)

        self.about_page.show()

