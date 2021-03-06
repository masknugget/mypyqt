# 布局管理

from PySide2.QtWidgets import QApplication, QWidget, QDialog, QHBoxLayout, QVBoxLayout, QGroupBox, QPushButton
import sys
from PySide2.QtGui import QIcon, QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("布局管理")
        self.setGeometry(300, 200, 500, 400)
        self.setIcon()
        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        self.show()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def createLayout(self):
        self.groupBox = QGroupBox("请选择一门语言")
        self.groupBox.setFont(QFont("Sanserif", 13))

        hbox = QHBoxLayout()

        button = QPushButton("Python", self)
        button.setIcon(QIcon("Python.png"))
        button.setMinimumHeight(40)
        hbox.addWidget(button)

        button1 = QPushButton("C++", self)
        button1.setIcon(QIcon("cpp.png"))
        button1.setMinimumHeight(40)
        hbox.addWidget(button1)

        button2 = QPushButton("Javascript", self)
        button2.setIcon(QIcon("javascript.png"))
        button2.setMinimumHeight(40)
        hbox.addWidget(button2)

        self.groupBox.setLayout(hbox)


myapp = QApplication(sys.argv)
window = Window()

myapp.exec_()
sys.exit()