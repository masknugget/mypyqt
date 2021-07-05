import sys
import string

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QHeaderView, QAction, QMenu, QTableWidget, QTableWidgetItem, QApplication


class Header(QHeaderView):
    def __init__(self, parent=None):
        super(Header, self).__init__(Qt.Horizontal, parent)

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.ctxMenu)
        self.hello = QAction("Hello", self)
        self.hello.triggered.connect(self.printHello)
        self.currentSection = None

    def printHello(self):
        data = self.model().headerData(self.currentSection, Qt.Horizontal)
        print(data.toString())

    def ctxMenu(self, point):
        menu = QMenu(self)
        self.currentSection = self.logicalIndexAt(point)
        menu.addAction(self.hello)
        menu.exec_(self.mapToGlobal(point))


class Table(QTableWidget):
    def __init__(self, parent=None):
        super(Table, self).__init__(parent)
        self.setHorizontalHeader(Header(self))
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(['id', 'name', 'username'])
        self.populate()

    def populate(self):
        self.setRowCount(10)
        for i in range(10):
            for j, l in enumerate(string.ascii_letters[:3]):
                self.setItem(i, j, QTableWidgetItem(l))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = Table()
    t.show()
    app.exec_()
    sys.exit()
