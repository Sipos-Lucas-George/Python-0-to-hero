import datetime
from dateutil import relativedelta

from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import *
from automated_docx.app_view_modified import App_View_Modified

import docxedit
from docx import Document


class App_View(QDialog, App_View_Modified):
    def __init__(self):
        super(App_View, self).__init__()
        self.setupUi(self)
        self.connect()
        self.cnp_line_edit.installEventFilter(self)

    def connect(self):
        self.clear_button.clicked.connect(self.clear_all)
        self.start_today_button.clicked.connect(self.focus)
        self.start_today_button.pressed.connect(self.set_start_today)
        self.current_today_button.clicked.connect(self.focus)
        self.current_today_button.pressed.connect(self.set_current_today)
        self.submit_button.clicked.connect(self.focus)
        self.submit_button.clicked.connect(self.save_any)
        self.clear_name_button.clicked.connect(self.clear_name)
        self.clear_add_years_button.clicked.connect(self.clear_add_years)
        self.clear_number1_button.clicked.connect(self.clear_number1)
        self.clear_number2_button.clicked.connect(self.clear_number2)
        self.clear_number3_button.clicked.connect(self.clear_number3)
        self.clear_cnp_button.clicked.connect(self.clear_cnp)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if len(self.cnp_line_edit.text()) == 4:
                self.cnp_line_edit.setCursorPosition(0)
                return True
        return super(QDialog, self).eventFilter(source, event)

    def focus(self):
        self.bg_widget.setFocus()

    def set_start_today(self):
        self.start_date_picker.calendarWidget().setSelectedDate(QDate().currentDate())

    def set_current_today(self):
        self.current_date_picker.calendarWidget().setSelectedDate(QDate().currentDate())

    def clear_all(self):
        self.d_radio_button.click()
        self.name_line_edit.clear()
        self.add_year_line_edit.clear()
        self.number1_line_edit.clear()
        self.number2_line_edit.clear()
        self.number3_line_edit.clear()
        self.cnp_line_edit.clear()
        self.set_start_today()
        self.set_current_today()
        self.name_line_edit.setFocus()

    def clear_name(self):
        self.name_line_edit.clear()
        self.name_line_edit.setFocus()

    def clear_add_years(self):
        self.add_year_line_edit.clear()
        self.add_year_line_edit.setFocus()

    def clear_number1(self):
        self.number1_line_edit.clear()
        self.number1_line_edit.setFocus()

    def clear_number2(self):
        self.number2_line_edit.clear()
        self.number2_line_edit.setFocus()

    def clear_number3(self):
        self.number3_line_edit.clear()
        self.number3_line_edit.setFocus()

    def clear_cnp(self):
        self.cnp_line_edit.clear()
        self.cnp_line_edit.setFocus()

    def save_any(self):
        if len(self.name_line_edit.text()) == 0 or len(self.number1_line_edit.text()) == 0 \
                or len(self.number2_line_edit.text()) == 0 or len(self.number3_line_edit.text()) == 0 \
                or len(self.cnp_line_edit.text()) == 0:
            return
        if self.d_radio_button.isChecked():
            self.save_d()
        else:
            self.save_p()

    def save_d(self):
        document = Document("document_d.docx")

        name = self.name_line_edit.text()

        date_current = datetime.date(*self.current_date_picker.date().getDate()).strftime("%d.%m.%Y")
        date_release = datetime.date(*self.start_date_picker.date().getDate()).strftime("%d.%m.%Y")
        date_determined = (datetime.date(*self.start_date_picker.date().getDate()) +
                           relativedelta.relativedelta(years=int(self.add_year_line_edit.text()))).strftime("%d.%m.%Y")
        date_next_month = (datetime.date(*self.current_date_picker.date().getDate()) +
                           relativedelta.relativedelta(months=1)).strftime("01.%m.%Y")

        number1 = self.number1_line_edit.text()
        number2 = self.number2_line_edit.text()
        number3 = self.number3_line_edit.text()
        cnp = self.cnp_line_edit.text().replace(" ", "")
        # censored the file for information purpose
        docxedit.replace_string(document, "", name.upper())
        docxedit.replace_string(document, "", name.title())
        docxedit.replace_string(document, "1036", number1)
        docxedit.replace_string(document, "9724", number2)
        docxedit.replace_string(document, "5038", number3)
        docxedit.replace_string(document, "", cnp)
        docxedit.replace_string(document, "14.09.2023", date_current)
        docxedit.replace_string(document, "05.09.2023", date_release)
        docxedit.replace_string(document, "05.09.2025", date_determined)
        docxedit.replace_string(document, "01.10.2023", date_next_month)

        document.save(f"{name.upper()} d.docx")

    def save_p(self):
        document = Document("document_p.docx")

        name = self.name_line_edit.text()

        date_current = datetime.date(*self.current_date_picker.date().getDate()).strftime("%d.%m.%Y")
        date_release = datetime.date(*self.start_date_picker.date().getDate()).strftime("%d.%m.%Y")
        date_next_month = (datetime.date(*self.current_date_picker.date().getDate()) +
                           relativedelta.relativedelta(months=1)).strftime("01.%m.%Y")

        number1 = self.number1_line_edit.text()
        number2 = self.number2_line_edit.text()
        number3 = self.number3_line_edit.text()
        cnp = self.cnp_line_edit.text().replace(" ", "")

        docxedit.replace_string(document, "", name.upper())
        docxedit.replace_string(document, "", name.title())
        docxedit.replace_string(document, "956", number1)
        docxedit.replace_string(document, "9105", number2)
        docxedit.replace_string(document, "4849", number3)
        docxedit.replace_string(document, "", cnp)
        docxedit.replace_string(document, "30.08.2023", date_current)
        docxedit.replace_string(document, "23.08.2023", date_release)
        docxedit.replace_string(document, "01.09.2023", date_next_month)

        document.save(f"{name.upper()} p.docx")
