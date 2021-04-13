from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QCompleter, QLineEdit
import sys
from PySide2.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 Completer")
        self.setGeometry(300, 200, 300, 250)

        self.createCompleter()
        self.setIcon()
        self.show()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def createCompleter(self):
        vbox = QVBoxLayout()

        names = ["Afghanistan", "Argentina", "India", "Pakistan", "Japan", "Indonesia", "China", "UAE", "America",
                 "Armanistan", "Azerbaijan", "Chicago", "Chile"]

        completer = QCompleter(names)

        self.lineEdit = QLineEdit()
        self.lineEdit.setCompleter(completer)
        vbox.addWidget(self.lineEdit)

        self.setLayout(vbox)


myapp = QApplication(sys.argv)
window = Window()

myapp.exec_()
sys.exit()
