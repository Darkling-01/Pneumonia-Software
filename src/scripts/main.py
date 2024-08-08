import sys
from src.gui import GUI

if __name__ == "__main__":

    # create the application object
    app = GUI.QtWidgets.QApplication(sys.argv)
    # create the instance of window
    window = GUI.MainWindow()
    window.show()

    # run the program
    exit(app.exec())

