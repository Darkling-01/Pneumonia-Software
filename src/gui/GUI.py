import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # set background-color
        self.setStyleSheet("background-color: #2c2e30")
        self.setWindowTitle("Pneumonia Detection")
        # set window size (0, 0, width, height)
        self.setGeometry(0, 0, 1400, 900)

        self.textTitle = QtWidgets.QLabel("Pneumonia Detection", self)
        self.textTitle.setStyleSheet("QLabel { align-text: center; color: white; font-size: 22px;}")

        # show form
        self.show()


if __name__ == "__main__":

    # create the application object
    app = QtWidgets.QApplication(sys.argv)
    # create the instance of window
    window_1 = MainWindow()

    # run the program
    exit(app.exec())

