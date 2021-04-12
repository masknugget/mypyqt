import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QLabel, QTreeWidgetItem, QHBoxLayout
from PySide2.QtWidgets import QAbstractItemView
from PySide2.QtWidgets import QBoxLayout

app = QApplication(sys.argv)

tree = QtWidgets.QTreeWidget()
tree.setColumnWidth(20, 50)
tree.setColumnCount(1)

tree.setSelectionMode(QAbstractItemView.MultiSelection)
tree.setSelectionMode(QAbstractItemView.SingleSelection)


for i in range(10):
    child = QTreeWidgetItem(tree)
    # for i in range(10):
    child.setText(0, 'a'+str(i))
    # child.set

for i in range(5):
    child = QTreeWidgetItem(tree)
    # for i in range(10):
    child.setText(0, 'a'+str(i))

tree.show()



tree_1 = QtWidgets.QTreeWidget()
tree_1.setColumnWidth(20, 50)
tree_1.setColumnCount(1)

tree_1.setSelectionMode(QAbstractItemView.MultiSelection)
tree_1.setSelectionMode(QAbstractItemView.SingleSelection)


for i in range(10):
    child = QTreeWidgetItem(tree_1)
    # for i in range(10):
    child.setText(0, 'a'+str(i))
    # child.set


# tree.show()
main_widget = QtWidgets.QWidget()
layout = QHBoxLayout()
layout.addWidget(tree)
layout.addWidget(tree_1)
main_widget.setLayout(layout)

main_widget.show()
label = QLabel("Hello World!")
label = QLabel("<font color=red size=40>Hello World!</font>")
# label.show()
app.exec_()