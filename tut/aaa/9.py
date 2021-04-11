# StatusBar
from PySide2.QtWidgets import QApplication, QMainWindow, QStatusBar
import sys
from PySide2.QtGui import QIcon


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Status Bar")
        self.setGeometry(300, 200, 500, 400)

        self.setIcon()
        self.createStatusBar()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def createStatusBar(self):
        self.myStatus = QStatusBar()
        self.myStatus.showMessage("显示3秒", 3000)
        self.setStatusBar(self.myStatus)


myapp = QApplication(sys.argv)
window = Window()
window.show()
myapp.exec_()
sys.exit()