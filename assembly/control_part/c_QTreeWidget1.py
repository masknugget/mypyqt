from PySide2 import QtWidgets, QtCore, QtGui

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent=parent)

        layout = QtWidgets.QVBoxLayout()

        self.treewidget = QtWidgets.QTreeWidget()
        self.treewidget.setColumnCount(4)

        layout.addWidget(self.treewidget)

        self.setLayout(layout)

        self.build_tree()


    def build_tree(self):
        for index in range(10):
            item = QtWidgets.QTreeWidgetItem(self.treewidget)
            item.setText(0, 'icon 1')
            item.setText(1, 'icon 2')

            line_edit = QtWidgets.QLineEdit(self.treewidget)

            push_button = QtWidgets.QPushButton(self.treewidget)
            push_button.setText('TEST')

            self.treewidget.setItemWidget(item, 2, line_edit)
            self.treewidget.setItemWidget(item, 3, push_button)


app = QtWidgets.QApplication([])
window = Window()
window.show()
app.exec_()