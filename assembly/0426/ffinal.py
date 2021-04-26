from PyQt5 import QtWidgets
from PyQt5 import QtGui
import sys

app = QtWidgets.QApplication(sys.argv)


window = QtWidgets.QWidget()
window.setWindowTitle("QToolBox")
window.resize(200, 100)
window.setWindowTitle('bbbba')



a = QtWidgets.QWidget()
a.setWindowTitle('aaaaa')

toolBox = QtWidgets.QListWidget()

toolBox.addItem("Tab Content 1")
toolBox.addItem("Tab Content 2")
toolBox.addItem("Tab Content 3")
toolBox.addItem("Tab Content 4")


b = QtWidgets.QWidget()
b.setWindowTitle('aaaaa')


toolBox = QtWidgets.QListWidget()

toolBox.addItem("Tab Content 1")
toolBox.addItem("Tab Content 2")
toolBox.addItem("Tab Content 3")
toolBox.addItem("Tab Content 4")



vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(a)
vbox.addWidget(toolBox)
vbox.addWidget(b)
vbox.addWidget(toolBox)

window.setLayout(vbox)



window.show()
sys.exit(app.exec_())
