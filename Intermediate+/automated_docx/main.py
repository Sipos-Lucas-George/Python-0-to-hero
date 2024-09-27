import sys

from PyQt5.QtWidgets import QApplication, QStackedWidget, QDialog
from PyQt5.QtWidgets import QDesktopWidget
from automated_docx.app_view_backend import App_View


class Center(QDialog):
    def __init__(self):
        super().__init__()

    def center(self):
        qtRectangle = self.frameGeometry()
        qtRectangle.setRight(1000)
        qtRectangle.setBottom(700)
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        return qtRectangle.topLeft()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stack_widget = QStackedWidget()
    stack_widget.setFixedWidth(1000)
    stack_widget.setFixedHeight(700)
    app_view = App_View()
    stack_widget.addWidget(app_view)
    stack_widget.move(Center().center())
    stack_widget.show()
    app_view.name_line_edit.setFocus()
    sys.exit(app.exec_())
