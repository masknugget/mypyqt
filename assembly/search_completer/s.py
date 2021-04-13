# -*- coding:utf-8 -*-

import math
import sys
import re
import os
import json, time
import shutil

from PySide2.QtCore import QStringListModel
from PySide2.QtWidgets import QApplication, QGridLayout, QLabel, QComboBox, QCompleter, QLineEdit, QDialog

# reload(sys)
# sys.setdefaultencoding("utf-8")


class ManageSubmit(QDialog):
    def __init__(self, parent=None):
        super(ManageSubmit, self).__init__(parent)
        self.initUI()
        self.setWindowTitle(u"test界面")

    def initUI(self):
        # 姓名
        name_label = QLabel(u"姓名：")
        self.name = QLineEdit(u"******")

        # 职工号
        num_label = QLabel(u"职工号：")
        self.num = QLineEdit("960521")

        # 使用软件
        pro_soft_label = QLabel("Software")
        self.pro_soft_label = QComboBox()
        # 对应json

        # 项目
        pro_label = QLabel("Project")

        self.pro_label = QComboBox()
        self.pro_label.setEditable(True)
        completer = QCompleter()
        self.pro_label.setCompleter(completer)
        model = QStringListModel()
        model.setStringList(['pro1', 'pro2', 'pro3', 'pro4', 'other'])
        completer.setModel(model)

        # 工具
        tool_label = QLabel("Tool")
        self.tool_label = QComboBox()

        leftLayout = QGridLayout()
        leftLayout.addWidget(name_label, 0, 0)
        leftLayout.addWidget(self.name, 0, 1)
        leftLayout.addWidget(self.name, 0, 1)
        leftLayout.addWidget(num_label, 1, 0)
        leftLayout.addWidget(self.num, 1, 1)

        leftLayout.addWidget(pro_soft_label, 2, 0)

        leftLayout.addWidget(self.pro_soft_label, 2, 1)

        leftLayout.addWidget(pro_label, 3, 0)
        leftLayout.addWidget(self.pro_label, 3, 1)

        leftLayout.addWidget(tool_label, 4, 0)
        leftLayout.addWidget(self.tool_label, 4, 1)

        leftLayout.setColumnStretch(0, 1)
        leftLayout.setColumnStretch(1, 3)

        self.setLayout(leftLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = ManageSubmit()
    dialog.show()
    sys.exit(app.exec_())
