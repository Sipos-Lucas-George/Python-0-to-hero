# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'automated_docx/app_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 700)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bg_widget = QtWidgets.QWidget(Dialog)
        self.bg_widget.setStyleSheet("QWidget#bg_widget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(63, 193, 234, 255), stop:1 rgba(255, 193, 234, 255));\n"
"}")
        self.bg_widget.setObjectName("bg_widget")
        self.number2_line_edit = QtWidgets.QLineEdit(self.bg_widget)
        self.number2_line_edit.setGeometry(QtCore.QRect(350, 290, 300, 30))
        self.number2_line_edit.setStyleSheet("background-color: #fff;\n"
"border-width: 0px;\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"font-size: 20px;\n"
"padding-left: 10px;")
        self.number2_line_edit.setObjectName("number2_line_edit")
        self.submit_button = QtWidgets.QPushButton(self.bg_widget)
        self.submit_button.setGeometry(QtCore.QRect(390, 550, 220, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit_button.sizePolicy().hasHeightForWidth())
        self.submit_button.setSizePolicy(sizePolicy)
        self.submit_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"font-size: 20px;")
        self.submit_button.setObjectName("submit_button")
        self.cnp_line_edit = QtWidgets.QLineEdit(self.bg_widget)
        self.cnp_line_edit.setGeometry(QtCore.QRect(350, 410, 300, 30))
        self.cnp_line_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cnp_line_edit.setStyleSheet("background-color: #fff;\n"
"border-width: 0px;\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"font-size: 20px;\n"
"padding-left: 10px;")
        self.cnp_line_edit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.cnp_line_edit.setObjectName("cnp_line_edit")
        self.label_2 = QtWidgets.QLabel(self.bg_widget)
        self.label_2.setGeometry(QtCore.QRect(360, 270, 111, 20))
        self.label_2.setStyleSheet("color: black;\n"
"font-size: 16px;")
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.bg_widget)
        self.label_6.setGeometry(QtCore.QRect(520, 450, 121, 20))
        self.label_6.setStyleSheet("color: black;\n"
"font-size: 16px;")
        self.label_6.setObjectName("label_6")
        self.start_date_picker = QtWidgets.QDateEdit(self.bg_widget)
        self.start_date_picker.setEnabled(True)
        self.start_date_picker.setGeometry(QtCore.QRect(510, 470, 141, 26))
        self.start_date_picker.setFocusPolicy(QtCore.Qt.NoFocus)
        self.start_date_picker.setStyleSheet("QDateEdit{\n"
"    border-width: 0px;\n"
"    border-style: solid;\n"
"    border-radius: 13px;\n"
"    font-size: 20px;\n"
"    color: black;\n"
"    padding-left: 5px;\n"
"}\n"
"QDateEdit::drop-down {\n"
"    image: url(:/drop_down_icon/drop_down.png);\n"
"    width: 26px;\n"
"    height: 26px;\n"
"}\n"
"\n"
"QDateEdit::drop-arrow {\n"
"    image: url(:/drop_down_icon/drop_down.png);\n"
"    width: 26px;\n"
"    height: 26px;\n"
"}")
        self.start_date_picker.setCalendarPopup(True)
        self.start_date_picker.setObjectName("start_date_picker")
        self.number1_line_edit = QtWidgets.QLineEdit(self.bg_widget)
        self.number1_line_edit.setGeometry(QtCore.QRect(350, 230, 300, 30))
        self.number1_line_edit.setStyleSheet("background-color: #fff;\n"
"border-width: 0px;\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"font-size: 20px;\n"
"padding-left: 10px;")
        self.number1_line_edit.setObjectName("number1_line_edit")
        self.label = QtWidgets.QLabel(self.bg_widget)
        self.label.setGeometry(QtCore.QRect(360, 210, 131, 20))
        self.label.setStyleSheet("color: black;\n"
"font-size: 16px;")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.bg_widget)
        self.label_4.setGeometry(QtCore.QRect(360, 390, 41, 20))
        self.label_4.setStyleSheet("color: black;\n"
"font-size: 16px;")
        self.label_4.setObjectName("label_4")
        self.number3_line_edit = QtWidgets.QLineEdit(self.bg_widget)
        self.number3_line_edit.setGeometry(QtCore.QRect(350, 350, 300, 30))
        self.number3_line_edit.setStyleSheet("background-color: #fff;\n"
"border-width: 0px;\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"font-size: 20px;\n"
"padding-left: 10px;")
        self.number3_line_edit.setObjectName("number3_line_edit")
        self.label_3 = QtWidgets.QLabel(self.bg_widget)
        self.label_3.setGeometry(QtCore.QRect(360, 330, 131, 20))
        self.label_3.setStyleSheet("color: black;\n"
"font-size: 16px;")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.bg_widget)
        self.label_5.setGeometry(QtCore.QRect(360, 450, 111, 20))
        self.label_5.setStyleSheet("color: black;\n"
"font-size: 16px;")
        self.label_5.setObjectName("label_5")
        self.current_date_picker = QtWidgets.QDateEdit(self.bg_widget)
        self.current_date_picker.setGeometry(QtCore.QRect(350, 470, 141, 26))
        self.current_date_picker.setFocusPolicy(QtCore.Qt.NoFocus)
        self.current_date_picker.setStyleSheet("QDateEdit{\n"
"    border-width: 0px;\n"
"    border-style: solid;\n"
"    border-radius: 13px;\n"
"    font-size: 20px;\n"
"    color: black;\n"
"    padding-left: 5px;\n"
"}\n"
"QDateEdit::drop-down {\n"
"    image: url(:/drop_down_icon/drop_down.png);\n"
"    width: 26px;\n"
"    height: 26px;\n"
"}")
        self.current_date_picker.setCalendarPopup(True)
        self.current_date_picker.setObjectName("current_date_picker")
        self.add_year_line_edit = QtWidgets.QLineEdit(self.bg_widget)
        self.add_year_line_edit.setGeometry(QtCore.QRect(350, 170, 300, 30))
        self.add_year_line_edit.setStyleSheet("background-color: #fff;\n"
"border-width: 0px;\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"font-size: 20px;\n"
"padding-left: 10px;")
        self.add_year_line_edit.setObjectName("add_year_line_edit")
        self.label_7 = QtWidgets.QLabel(self.bg_widget)
        self.label_7.setGeometry(QtCore.QRect(360, 150, 101, 20))
        self.label_7.setStyleSheet("color: black;\n"
"font-size: 16px;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.bg_widget)
        self.label_8.setGeometry(QtCore.QRect(360, 90, 51, 20))
        self.label_8.setStyleSheet("color: black;\n"
"font-size: 16px;")
        self.label_8.setObjectName("label_8")
        self.name_line_edit = QtWidgets.QLineEdit(self.bg_widget)
        self.name_line_edit.setGeometry(QtCore.QRect(350, 110, 300, 30))
        self.name_line_edit.setStyleSheet("background-color: #fff;\n"
"border-width: 0px;\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"font-size: 20px;\n"
"padding-left: 10px;")
        self.name_line_edit.setObjectName("name_line_edit")
        self.d_radio_button = QtWidgets.QRadioButton(self.bg_widget)
        self.d_radio_button.setGeometry(QtCore.QRect(350, 40, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.d_radio_button.setFont(font)
        self.d_radio_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.d_radio_button.setStyleSheet("")
        self.d_radio_button.setChecked(True)
        self.d_radio_button.setObjectName("d_radio_button")
        self.p_radio_button = QtWidgets.QRadioButton(self.bg_widget)
        self.p_radio_button.setGeometry(QtCore.QRect(510, 40, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p_radio_button.setFont(font)
        self.p_radio_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.p_radio_button.setStyleSheet("")
        self.p_radio_button.setObjectName("p_radio_button")
        self.clear_button = QtWidgets.QPushButton(self.bg_widget)
        self.clear_button.setGeometry(QtCore.QRect(0, 0, 201, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_button.sizePolicy().hasHeightForWidth())
        self.clear_button.setSizePolicy(sizePolicy)
        self.clear_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"font-size: 20px;")
        self.clear_button.setObjectName("clear_button")
        self.clear_name_button = QtWidgets.QPushButton(self.bg_widget)
        self.clear_name_button.setGeometry(QtCore.QRect(655, 110, 30, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_name_button.sizePolicy().hasHeightForWidth())
        self.clear_name_button.setSizePolicy(sizePolicy)
        self.clear_name_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_name_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"font-size: 20px;")
        self.clear_name_button.setObjectName("clear_name_button")
        self.clear_add_years_button = QtWidgets.QPushButton(self.bg_widget)
        self.clear_add_years_button.setGeometry(QtCore.QRect(655, 170, 30, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_add_years_button.sizePolicy().hasHeightForWidth())
        self.clear_add_years_button.setSizePolicy(sizePolicy)
        self.clear_add_years_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_add_years_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"font-size: 20px;")
        self.clear_add_years_button.setObjectName("clear_add_years_button")
        self.clear_number1_button = QtWidgets.QPushButton(self.bg_widget)
        self.clear_number1_button.setGeometry(QtCore.QRect(655, 230, 30, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_number1_button.sizePolicy().hasHeightForWidth())
        self.clear_number1_button.setSizePolicy(sizePolicy)
        self.clear_number1_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_number1_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"font-size: 20px;")
        self.clear_number1_button.setObjectName("clear_number1_button")
        self.clear_number2_button = QtWidgets.QPushButton(self.bg_widget)
        self.clear_number2_button.setGeometry(QtCore.QRect(655, 290, 30, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_number2_button.sizePolicy().hasHeightForWidth())
        self.clear_number2_button.setSizePolicy(sizePolicy)
        self.clear_number2_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_number2_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"font-size: 20px;")
        self.clear_number2_button.setObjectName("clear_number2_button")
        self.clear_number3_button = QtWidgets.QPushButton(self.bg_widget)
        self.clear_number3_button.setGeometry(QtCore.QRect(655, 350, 30, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_number3_button.sizePolicy().hasHeightForWidth())
        self.clear_number3_button.setSizePolicy(sizePolicy)
        self.clear_number3_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_number3_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"font-size: 20px;")
        self.clear_number3_button.setObjectName("clear_number3_button")
        self.clear_cnp_button = QtWidgets.QPushButton(self.bg_widget)
        self.clear_cnp_button.setGeometry(QtCore.QRect(655, 410, 30, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_cnp_button.sizePolicy().hasHeightForWidth())
        self.clear_cnp_button.setSizePolicy(sizePolicy)
        self.clear_cnp_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_cnp_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"font-size: 20px;")
        self.clear_cnp_button.setObjectName("clear_cnp_button")
        self.horizontalLayout.addWidget(self.bg_widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.d_radio_button, self.p_radio_button)
        Dialog.setTabOrder(self.p_radio_button, self.name_line_edit)
        Dialog.setTabOrder(self.name_line_edit, self.add_year_line_edit)
        Dialog.setTabOrder(self.add_year_line_edit, self.number1_line_edit)
        Dialog.setTabOrder(self.number1_line_edit, self.number2_line_edit)
        Dialog.setTabOrder(self.number2_line_edit, self.number3_line_edit)
        Dialog.setTabOrder(self.number3_line_edit, self.cnp_line_edit)
        Dialog.setTabOrder(self.cnp_line_edit, self.current_date_picker)
        Dialog.setTabOrder(self.current_date_picker, self.start_date_picker)
        Dialog.setTabOrder(self.start_date_picker, self.submit_button)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.submit_button.setText(_translate("Dialog", "Submit"))
        self.cnp_line_edit.setInputMask(_translate("Dialog", "9  999999  999999"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p>Numar cerere:</p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p>Data eliberare:</p></body></html>"))
        self.start_date_picker.setDisplayFormat(_translate("Dialog", "dd.MM.yyyy"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>Numar dispozitie:</p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p>CNP:</p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p>Numar certificat:</p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p>Data dispozitie:</p></body></html>"))
        self.current_date_picker.setDisplayFormat(_translate("Dialog", "dd.MM.yyyy"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p>Numar de ani:</p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p>Nume:</p></body></html>"))
        self.d_radio_button.setText(_translate("Dialog", "Determinata"))
        self.p_radio_button.setText(_translate("Dialog", "Nedeterminata"))
        self.clear_button.setText(_translate("Dialog", "Clear"))
        self.clear_name_button.setText(_translate("Dialog", "X"))
        self.clear_add_years_button.setText(_translate("Dialog", "X"))
        self.clear_number1_button.setText(_translate("Dialog", "X"))
        self.clear_number2_button.setText(_translate("Dialog", "X"))
        self.clear_number3_button.setText(_translate("Dialog", "X"))
        self.clear_cnp_button.setText(_translate("Dialog", "X"))
import drop_down_icon_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
