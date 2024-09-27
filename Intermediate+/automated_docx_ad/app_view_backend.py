from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from automated_docx_ad.app_view_modified import App_View_Modified

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

    def clear_all(self):
        self.f_radio_button.click()
        self._25_radio_button.click()
        self.name_line_edit.clear()
        self.ad_line_edit.clear()
        self.evidence_line_edit.clear()
        self.evidence_year_line_edit.clear()
        self.grad_line_edit.clear()
        self.cnp_line_edit.clear()
        self.name_line_edit.setFocus()

    def clear_name(self):
        self.name_line_edit.clear()
        self.name_line_edit.setFocus()

    def clear_add_years(self):
        self.ad_line_edit.clear()
        self.ad_line_edit.setFocus()

    def clear_number1(self):
        self.evidence_line_edit.clear()
        self.evidence_line_edit.setFocus()

    def clear_number2(self):
        self.evidence_year_line_edit.clear()
        self.evidence_year_line_edit.setFocus()

    def clear_number3(self):
        self.grad_line_edit.clear()
        self.grad_line_edit.setFocus()

    def clear_cnp(self):
        self.cnp_line_edit.clear()
        self.cnp_line_edit.setFocus()

    def save_any(self):
        if len(self.name_line_edit.text()) == 0 or len(self.evidence_line_edit.text()) == 0 \
                or len(self.evidence_year_line_edit.text()) == 0 or len(self.grad_line_edit.text()) == 0 \
                or len(self.cnp_line_edit.text()) == 0:
            return
        self.save_ad()

    def save_ad(self):
        document = Document("act_aditional.docx")

        name = self.name_line_edit.text()
        ad = self.ad_line_edit.text()
        evidence = self.evidence_line_edit.text()
        evidence_year = self.evidence_year_line_edit.text()
        gradation = self.grad_line_edit.text()
        cnp = self.cnp_line_edit.text().replace(" ", "")

        docxedit.replace_string(document, "Numex Prenumex", name.upper())
        docxedit.replace_string(document, "numar_act", ad)
        docxedit.replace_string(document, "16x7", evidence)
        docxedit.replace_string(document, "2x012", evidence_year)
        docxedit.replace_string(document, "nr_grad", gradation)
        docxedit.replace_string(document, "2780518xxxxxx", cnp)
        docxedit.replace_string(document, "doamna", "doamna" if self.f_radio_button.isChecked() else "domnul")
        docxedit.replace_string(document, "x25x", "25" if self._25_radio_button.isChecked() else "21")

        document.save(f"{name.title()} {ad}.docx")
