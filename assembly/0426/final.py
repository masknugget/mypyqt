from PyQt5 import QtWidgets
from PyQt5 import QtGui
import sys

app = QtWidgets.QApplication(sys.argv)

main_v = QtWidgets.QListWidget()

window = QtWidgets.QWidget()
window.setWindowTitle("QToolBox")
window.resize(200, 100)
window.setWindowTitle('a')
toolBox = QtWidgets.QListWidget()

toolBox.addItem("Tab Content 1")
toolBox.addItem("Tab Content 2")
toolBox.addItem("Tab Content 3")
toolBox.addItem("Tab Content 4")

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(toolBox)
window.setLayout(vbox)


window_2 = QtWidgets.QWidget()
window_2.setWindowTitle("QToolBox")
window_2.resize(200, 100)
toolBox = QtWidgets.QListWidget()

toolBox.addItem("Tab Content 2")
toolBox.addItem("Tab Content 3")
toolBox.addItem("Tab Content 4")
toolBox.addItem("Tab Content 5")

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(toolBox)
window_2.setLayout(vbox)

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(window)
vbox.addWidget(window_2)
main_v.setLayout(vbox)



main_v.show()
sys.exit(app.exec_())
