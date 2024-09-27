# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lucas/Desktop/Intermediate+/automated_docx_ad/app_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 750)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bg_widget = QtWidgets.QWidget(Dialog)
        self.bg_widget.setStyleSheet("QWidget#bg_widget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(63, 193, 234, 255), stop:1 rgba(255, 193, 234, 255));\n"
"}")
        self.bg_widget.setObjectName("bg_widget")
        self.evidence_year_line_edit = QtWidgets.QLineEdit(self.bg_widget)
        self.evidence_year_line_edit.setGeometry(QtCore.QRect(345, 320, 300, 30))
        self.evidence_year_line_edit.setStyleSheet("background-color: #fff;\n"
"border-width: 0px;\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"font-size: 20px;\n"
"padding-left: 10px;")
        self.evidence_year_line_edit.setObjectName("evidence_year_line_edit")
        self.submit_button = QtWidgets.QPushButton(self.bg_widget)
        self.submit_button.setGeometry(QtCore.QRect(400, 520, 220, 60))
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
        self.cnp_line_edit.setGeometry(QtCore.QRect(345, 440, 300, 30))
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
        self.label_2.setGeometry(QtCore.QRect(355, 300, 91, 20))
        self.label_2.setStyleSheet("color: black;\n"
"font-size: 16px;")
        self.label_2.setObjectName("label_2")
        self.evidence_line_edit = QtWidgets.QLineEdit(self.bg_widget)
        self.evidence_line_edit.setGeometry(QtCore.QRect(345, 260, 300, 30))
        self.evidence_line_edit.setStyleSheet("background-color: #fff;\n"
"border-width: 0px;\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"font-size: 20px;\n"
"padding-left: 10px;")
        self.evidence_line_edit.setObjectName("evidence_line_edit")
        self.label = QtWidgets.QLabel(self.bg_widget)
        self.label.setGeometry(QtCore.QRect(355, 240, 131, 20))
        self.label.setStyleSheet("color: black;\n"
"font-size: 16px;")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.bg_widget)
        self.label_4.setGeometry(QtCore.QRect(355, 420, 41, 20))
        self.label_4.setStyleSheet("color: black;\n"
"font-size: 16px;")
        self.label_4.setObjectName("label_4")
        self.grad_line_edit = QtWidgets.QLineEdit(self.bg_widget)
        self.grad_line_edit.setGeometry(QtCore.QRect(345, 380, 300, 30))
        self.grad_line_edit.setStyleSheet("background-color: #fff;\n"
"border-width: 0px;\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"font-size: 20px;\n"
"padding-left: 10px;")
        self.grad_line_edit.setObjectName("grad_line_edit")
        self.label_3 = QtWidgets.QLabel(self.bg_widget)
        self.label_3.setGeometry(QtCore.QRect(355, 360, 71, 20))
        self.label_3.setStyleSheet("color: black;\n"
"font-size: 16px;")
        self.label_3.setObjectName("label_3")
        self.ad_line_edit = QtWidgets.QLineEdit(self.bg_widget)
        self.ad_line_edit.setGeometry(QtCore.QRect(345, 200, 300, 30))
        self.ad_line_edit.setStyleSheet("background-color: #fff;\n"
"border-width: 0px;\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"font-size: 20px;\n"
"padding-left: 10px;")
        self.ad_line_edit.setObjectName("ad_line_edit")
        self.label_7 = QtWidgets.QLabel(self.bg_widget)
        self.label_7.setGeometry(QtCore.QRect(355, 180, 151, 20))
        self.label_7.setStyleSheet("color: black;\n"
"font-size: 16px;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.bg_widget)
        self.label_8.setGeometry(QtCore.QRect(355, 120, 51, 20))
        self.label_8.setStyleSheet("color: black;\n"
"font-size: 16px;")
        self.label_8.setObjectName("label_8")
        self.name_line_edit = QtWidgets.QLineEdit(self.bg_widget)
        self.name_line_edit.setGeometry(QtCore.QRect(345, 140, 300, 30))
        self.name_line_edit.setStyleSheet("background-color: #fff;\n"
"border-width: 0px;\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"font-size: 20px;\n"
"padding-left: 10px;")
        self.name_line_edit.setObjectName("name_line_edit")
        self.f_radio_button = QtWidgets.QRadioButton(self.bg_widget)
        self.f_radio_button.setGeometry(QtCore.QRect(350, 40, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.f_radio_button.setFont(font)
        self.f_radio_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.f_radio_button.setStyleSheet("")
        self.f_radio_button.setChecked(True)
        self.f_radio_button.setObjectName("f_radio_button")
        self.m_radio_button = QtWidgets.QRadioButton(self.bg_widget)
        self.m_radio_button.setGeometry(QtCore.QRect(510, 40, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.m_radio_button.setFont(font)
        self.m_radio_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.m_radio_button.setStyleSheet("")
        self.m_radio_button.setObjectName("m_radio_button")
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
        self.clear_name_button.setGeometry(QtCore.QRect(650, 140, 30, 30))
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
        self.clear_add_years_button.setGeometry(QtCore.QRect(650, 200, 30, 30))
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
        self.clear_number1_button.setGeometry(QtCore.QRect(650, 260, 30, 30))
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
        self.clear_number2_button.setGeometry(QtCore.QRect(650, 320, 30, 30))
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
        self.clear_number3_button.setGeometry(QtCore.QRect(650, 380, 30, 30))
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
        self.clear_cnp_button.setGeometry(QtCore.QRect(650, 440, 30, 30))
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
        self._25_radio_button = QtWidgets.QRadioButton(self.bg_widget)
        self._25_radio_button.setGeometry(QtCore.QRect(350, 80, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self._25_radio_button.setFont(font)
        self._25_radio_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self._25_radio_button.setStyleSheet("")
        self._25_radio_button.setChecked(False)
        self._25_radio_button.setObjectName("_25_radio_button")
        self._21_radio_button = QtWidgets.QRadioButton(self.bg_widget)
        self._21_radio_button.setGeometry(QtCore.QRect(510, 80, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self._21_radio_button.setFont(font)
        self._21_radio_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self._21_radio_button.setStyleSheet("")
        self._21_radio_button.setChecked(False)
        self._21_radio_button.setObjectName("_21_radio_button")
        self.horizontalLayout.addWidget(self.bg_widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.f_radio_button, self.m_radio_button)
        Dialog.setTabOrder(self.m_radio_button, self.name_line_edit)
        Dialog.setTabOrder(self.name_line_edit, self.ad_line_edit)
        Dialog.setTabOrder(self.ad_line_edit, self.evidence_line_edit)
        Dialog.setTabOrder(self.evidence_line_edit, self.evidence_year_line_edit)
        Dialog.setTabOrder(self.evidence_year_line_edit, self.grad_line_edit)
        Dialog.setTabOrder(self.grad_line_edit, self.cnp_line_edit)
        Dialog.setTabOrder(self.cnp_line_edit, self.submit_button)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.submit_button.setText(_translate("Dialog", "Submit"))
        self.cnp_line_edit.setInputMask(_translate("Dialog", "9  999999  999999"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p>An evidenta:</p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>Numar evidenta:</p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p>CNP:</p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p>Gradatia:</p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p>Numar act aditional:</p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p>Nume:</p></body></html>"))
        self.f_radio_button.setText(_translate("Dialog", "doamna"))
        self.m_radio_button.setText(_translate("Dialog", "domnul"))
        self.clear_button.setText(_translate("Dialog", "Clear"))
        self.clear_name_button.setText(_translate("Dialog", "X"))
        self.clear_add_years_button.setText(_translate("Dialog", "X"))
        self.clear_number1_button.setText(_translate("Dialog", "X"))
        self.clear_number2_button.setText(_translate("Dialog", "X"))
        self.clear_number3_button.setText(_translate("Dialog", "X"))
        self.clear_cnp_button.setText(_translate("Dialog", "X"))
        self._25_radio_button.setText(_translate("Dialog", "25"))
        self._21_radio_button.setText(_translate("Dialog", "21"))
import drop_down_icon_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())