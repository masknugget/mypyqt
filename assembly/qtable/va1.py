import sys

from PyQt5.QtWidgets import (QTableWidget, QCheckBox, QHeaderView, QAbstractItemView, QTableWidgetItem,
                             QPushButton, QApplication)
from PyQt5.QtCore import Qt, QSize, QPoint, QRect
from PyQt5.QtGui import QIcon, QMouseEvent, QFont, QColor, QBrush


class QTable(QTableWidget):
    all_checkbox = []

    def init(self, x=1, y=5):
        super(QTable, self).init(x, y)  # 默认1行 5列 第一行为表头
        self.setTableStyle()


    def setTableStyle(self):
        self.horizontalHeader().resizeSection(0, 100)
        self.horizontalHeader().resizeSection(1, 100)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)
        self.horizontalHeader().setSectionResizeMode(2, QHeaderView.Interactive)
        self.horizontalHeader().setSectionResizeMode(4, QHeaderView.Interactive)
        # self.setFocusPolicy(Qt.NoFocus)
        # self.setShowGrid(False)  # 隐藏网格
        # self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.horizontalHeader().setVisible(False)  # 隐藏原始行
        self.verticalHeader().setVisible(False)  # 隐藏列

        def setHorizontalHeaderLabels(self, *args):

            self.ch = QCheckBox()
            self.ch.setCheckState(Qt.Unchecked)
            self.ch.clicked.connect(self.selectAll)
            # self.ch.setStyleSheet('QCheckBox{margin-left:20px;}')
            self.setCellWidget(0, 0, self.ch)
            for i in range(len(args)):
                newItem = QTableWidgetItem(args[i])
                self.setItem(0, i + 1, newItem)
                newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        def addItem(self, args):

            # 插入行 行标
            cur_row = self.rowCount()

            self.insertRow(cur_row)
            ch = QCheckBox()
            self.all_checkbox.append(ch)
            ch.clicked.connect(self.onStateChanged)
            self.setCellWidget(cur_row, 0, ch)
            for i in range(len(args)):

                if isinstance(args[i], str):

                    newItem = QTableWidgetItem(args[i])
                    newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                    self.setItem(cur_row, i + 1, newItem)
                else:

                    args[i].index = cur_row
                    self.setCellWidget(cur_row, i + 1, args[i])

        def onStateChanged(self):
            select_num = [ch for ch in self.all_checkbox if ch.checkState()]
            if len(select_num) == self.rowCount() - 1:
                self.ch.setCheckState(2)
            elif len(select_num) == 0:
                self.ch.setCheckState(0)
            else:
                self.ch.setCheckState(1)

        def selectAll(self):

            if self.sender().isChecked():
                self.ch.setCheckState(2)
                for ch in self.all_checkbox:
                    ch.setCheckState(2)


            else:
                for ch in self.all_checkbox:
                    ch.setCheckState(0)

        def clearLine(self):

            for i in range(self.rowCount() - 1):
                self.removeRow(1)
            self.all_checkbox = []
        # def delRow(self,row):
        #     self.removeRow(row)
        #     self.all_checkbox.remove(self.all_checkbox[row-1])



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ta = QTable()
    ta.show()
    ta.setHorizontalHeaderLabels(['a', 'b'])
    sys.exit(app.exec_())
