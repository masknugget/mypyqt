import sys
from PySide2.QtWidgets import QApplication,QPushButton,QWidget
from PySide2.QtCore import SIGNAL,QObject

def slotBtnClicked():
	print("btn clicked..")

app = QApplication(sys.argv)
widget = QWidget()
widget.resize(300,200)
widget.show()

btn = QPushButton("Click me",widget)
btn.move(widget.width()/2. - btn.width()/2.,widget.height()/2. - btn.height()/2.)
QObject.connect(btn,SIGNAL('clicked()'),slotBtnClicked)
btn.show()

sys.exit(app.exec_())
