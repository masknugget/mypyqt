from PySide2 import QtCore
from PySide2.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QApplication


class Window(QWidget):
    def __init__(self, rows, columns):
        QWidget.__init__(self)
        self.table = QTableWidget(rows, columns, self)
        for column in range(columns):
            for row in range(rows):
                item = QTableWidgetItem('Text%d' % row)
                if row % 2:
                    item.setFlags(QtCore.Qt.ItemIsUserCheckable |
                                  QtCore.Qt.ItemIsEnabled)
                    item.setCheckState(QtCore.Qt.Unchecked)
                self.table.setItem(row, column, item)
        self.table.itemClicked.connect(self.handleItemClicked)
        layout = QVBoxLayout(self)
        layout.addWidget(self.table)
        self._list = []

    def handleItemClicked(self, item):
        if item.checkState() == QtCore.Qt.Checked:
            print('"%s" Checked' % item.text())
            self._list.append(item.row())
            print(self._list)
        else:
            print('"%s" Clicked' % item.text())

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Window(6, 3)
    window.resize(350, 300)
    window.show()
    sys.exit(app.exec_())