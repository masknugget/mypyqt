#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout,QVBoxLayout
import sys
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QFormLayout,QLineEdit,QLabel, QListWidget,QListWidgetItem


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

        layout = QVBoxLayout(self)
        # 列表
        self.listWidget = QListWidget(self)
        layout.addWidget(self.listWidget)

        self.get_content_button = QPushButton('获得内容', self)
        self.show_content_label = QLabel("content:")

        layout.addWidget(self.show_content_label)
        layout.addWidget(self.get_content_button)

        item = QListWidgetItem()  # 创建QListWidgetItem对象
        item.setSizeHint(QSize(300, 100))  # 设置QListWidgetItem大小

        self.tab1 = QWidget()
        self.tab1UI()

        self.listWidget.addItem(item)  # 添加item
        self.listWidget.setItemWidget(item, self.tab1 )  # 为item设置widget

        item2 = QListWidgetItem()  # 创建QListWidgetItem对象
        item2.setSizeHint(QSize(300, 100))  # 设置QListWidgetItem大小

        self.tab2 = QWidget()
        self.tab2UI()

        self.listWidget.addItem(item2)  # 添加item
        self.listWidget.setItemWidget(item2, self.tab2)  # 为item设置widget

        self.list_ui("lab1", "lab2", "AAA", "BBB")
        self.list_ui("lab1", "lab2", "111", "222")

        self.get_content_button.clicked.connect(self.get_content)

    def get_content(self):
        pass
        windows = self.listWidget.currentItem()
        print(type(windows))
        widget = self.listWidget.itemWidget(windows)
        print(type(widget))

        item = widget.findChild(QLabel, "lab1")
        print(type(item))

        if item:
            print(item.text())
            self.show_content_label.setText('content:' + item.text())

    def list_ui(self,label1_name,label2_name,label1_content,label2_content):
        control = QListWidgetItem()
        control.setSizeHint(QSize(300, 100))  # 设置QListWidgetItem大小
        widget = QWidget()
        layout = QHBoxLayout()
        label1 = QLabel(label1_content)
        label2 = QLabel(label2_content)
        label1.setObjectName(label1_name)
        label2.setObjectName(label2_name)
        layout.addWidget(label1)
        layout.addWidget(label2)

        widget.setLayout(layout)

        self.listWidget.addItem(control)
        self.listWidget.setItemWidget(control, widget)

    def tab1UI(self):
        layout = QFormLayout()
        layout.addRow("姓名", QLineEdit())
        layout.addRow("地址", QLineEdit())
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QFormLayout()
        layout.addRow("年龄", QLineEdit())
        layout.addRow("性别", QLineEdit())
        self.tab2.setLayout(layout)

    def initUI(self):
        self.setGeometry(300, 300, 600, 620)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
