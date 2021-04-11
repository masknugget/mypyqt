import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QLabel, QTreeWidgetItem
app = QApplication(sys.argv)

tree = QtWidgets.QTreeWidget()
tree.setColumnWidth(0, 30)
tree.setColumnCount(2)

for i in range(10):
    child = QTreeWidgetItem(tree)
    # for i in range(10):

    child.setText(0, 'a')
    child.setText(1, 'b')
    child.setText(2, 'c')
    # child.set


tree.show()


label = QLabel("Hello World!")
label = QLabel("<font color=red size=40>Hello World!</font>")
# label.show()
app.exec_()