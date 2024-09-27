from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIntValidator

from automated_docx.app_view import Ui_Dialog


class App_View_Modified(Ui_Dialog):
    def __init__(self):
        super().__init__()

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        layout1 = QtWidgets.QVBoxLayout()
        self.start_date_picker.setLayout(layout1)
        self.start_today_button = QtWidgets.QPushButton('&Today')
        self.start_today_button.setStyleSheet("""background-color: rgb(255, 255, 255);
border-width: 1px;
border-style: solid;
border-radius: 10px;
font-size: 20px;""")
        self.start_date_picker.calendarWidget().layout().addWidget(self.start_today_button)
        self.start_date_picker.calendarWidget().setSelectedDate(QDate().currentDate())
        layout2 = QtWidgets.QVBoxLayout()
        self.current_date_picker.setLayout(layout2)
        self.current_today_button = QtWidgets.QPushButton('&Today')
        self.current_today_button.setStyleSheet("""background-color: rgb(255, 255, 255);
border-width: 1px;
border-style: solid;
border-radius: 10px;
font-size: 20px;""")
        self.current_date_picker.calendarWidget().layout().addWidget(self.current_today_button)
        self.current_date_picker.calendarWidget().setSelectedDate(QDate().currentDate())
        self.cnp_line_edit.setCursorPosition(0)
        self.add_year_line_edit.setValidator(QIntValidator(1, 10))
