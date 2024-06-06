import sys
from PyQt5 import QtWidgets, QtCore, QtGui


# create the application object
app = QtWidgets.QApplication(sys.argv)
# create the form object
widget = QtWidgets.QWidget()
# set window size (width, height)
widget.resize(1400, 900)
# set the form title
widget.setWindowTitle("Pneumonia")
# show form
widget.show()

# run the program
exit(app.exec())

