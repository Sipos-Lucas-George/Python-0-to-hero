from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QDate, QRegExp
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtWidgets import QButtonGroup

from automated_docx_ad.app_view import Ui_Dialog


class App_View_Modified(Ui_Dialog):
    def __init__(self):
        super().__init__()

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.cnp_line_edit.setCursorPosition(0)
        self.ad_line_edit.setValidator(QRegExpValidator(QRegExp("[0-9]{2}")))
        self.evidence_line_edit.setValidator(QRegExpValidator(QRegExp("[0-9]{4}")))
        self.evidence_year_line_edit.setValidator(QRegExpValidator(QRegExp("[0-9]{4}")))
        self.grad_line_edit.setValidator(QRegExpValidator(QRegExp("[0-5]")))

        self.buttonGroup1 = QButtonGroup()  # Create button group 1
        self.buttonGroup1.addButton(self.f_radio_button)  # Add the first two radio buttons
        self.buttonGroup1.addButton(self.m_radio_button)
        self.buttonGroup2 = QButtonGroup()  # Create button group 2
        self.buttonGroup2.addButton(self._25_radio_button)  # Add the last two radio buttons
        self.buttonGroup2.addButton(self._21_radio_button)
        self.f_radio_button.setChecked(True)
        self._25_radio_button.setChecked(True)
