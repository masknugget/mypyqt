from PyQt5.QtCore import *
from PySide2.QtWidgets import QApplication, QWidget, QPushButton


def sinTest():
    btn.setText("按钮文本改变")


app = QApplication([])

main = QWidget()
main.resize(200, 100)
btn = QPushButton("按钮文本", main)

##按钮btn的内置信号连接名为sinTest的槽
btn.clicked.connect(sinTest)
main.show()

app.exec_()
