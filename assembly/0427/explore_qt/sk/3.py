# QTableWidget单元格文本居中

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QHeaderView, \
    QPushButton, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(500, 300)

        self.table = QTableWidget()  # 1
        self.set_table_properties()
        self.btn = QPushButton('文本居中')  # 2
        self.btn.clicked.connect(self.center_slot)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.table)
        v_layout.addWidget(self.btn)
        self.setLayout(v_layout)

    def set_table_properties(self):
        """设置表格属性"""
        self.table.setColumnCount(3)
        self.table.setRowCount(6)
        self.table.setHorizontalHeaderLabels(['标题1', '标题2', '标题3'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setHidden(True)

        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                self.table.setItem(row, col, QTableWidgetItem(f'({row}, {col})'))

    def center_slot(self):
        """文本居中槽函数"""
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                self.table.item(row, col).setTextAlignment(Qt.AlignCenter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())