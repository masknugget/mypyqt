# 打开关于窗口
from PySide2.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton
import sys
from PySide2.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("创建关于窗口")
        self.setGeometry(300, 200, 500, 400)
        self.setIcon()
        self.pushButton()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def pushButton(self):
        self.aboutButtton = QPushButton("打开关于窗口", self)
        self.aboutButtton.move(50, 100)
        self.aboutButtton.clicked.connect(self.aboutBox)

    def aboutBox(self):
        QMessageBox.about(self.aboutButtton, "关于 Pyside2", "Pyside2是Python语言的跨平台GUI库")


myapp = QApplication(sys.argv)
window = Window()
window.show()

myapp.exec_()
sys.exit()