''' 居中'''

from PySide2.QtWidgets import QApplication, QWidget, QDesktopWidget
import sys
from PySide2.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Center Window")
        self.setGeometry(500, 400, 500, 400)

        self.setIcon()
        self.center()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())


myapp = QApplication(sys.argv)
window = Window()
window.show()

myapp.exec_()
sys.exit()
