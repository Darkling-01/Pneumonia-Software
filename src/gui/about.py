from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, \
    QHBoxLayout, QStackedWidget
from assets.other_resources import descriptions
from src.gui.shared import SharedClass


class AboutPage(SharedClass):
    def __init__(self):
        super().__init__()

        # create description label
        self.description = QLabel(descriptions.text, self)
        self.description.setStyleSheet("color: white; font-size: 18px;")
        self.description.setAlignment(Qt.AlignCenter)

        # add the label to horizontal layout
        self.main_layout.addWidget(self.description)

        # create pages
        self.second_page = self.setup_second_page()

        # add pages to stacked widget
        self.add_widget(self.second_page)

        # show the second page initially
        self.set_current_widget(self.second_page)

    def setup_second_page(self):
        second_page = QWidget()
        second_page_layout = QVBoxLayout(second_page)

        button_layout = QHBoxLayout()
        button_layout.addStretch()

        main_button = QtWidgets.QPushButton("Main Page", second_page)
        main_button.setStyleSheet("color: black; background-color: white;")
        main_button.setFixedSize(100, 30)
        # main_button.clicked.connect(self.show_main_page)
        button_layout.addWidget(main_button)

        button_layout.addStretch()

        second_page_layout.setAlignment(Qt.AlignTop)

        second_page_layout.addLayout(button_layout)

        return second_page

    def show_main_page(self):
        self.description.hide()

        self.stacked_widget.setCurrentWidget(self.main_page)

        self.main_page.show()

