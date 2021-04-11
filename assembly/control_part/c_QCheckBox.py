# PySide2 QCheckBox控件应用

from PySide2.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QTextEdit
from PySide2.QtCore import Qt
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 新建4个复选框对象
        self.cb1 = QCheckBox('全选', self)
        self.cb2 = QCheckBox('复选1', self)
        self.cb3 = QCheckBox('复选2', self)
        self.cb4 = QCheckBox('复选3', self)

        bt = QPushButton('确定', self)

        self.resize(600, 400)
        self.setWindowTitle('复选框')
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.cb1)
        self.vbox.addWidget(self.cb2)
        self.vbox.addWidget(self.cb3)
        self.vbox.addWidget(self.cb4)
        self.vbox.addWidget(bt)
        self.textedit = QTextEdit()
        self.textedit.resize(400, 300)
        self.hbox = QHBoxLayout()
        self.hbox.addLayout(self.vbox)
        self.hbox.addWidget(self.textedit)
        self.setLayout(self.hbox)
        self.cb1.stateChanged.connect(self.changecb1)
        self.cb2.stateChanged.connect(self.changecb2)
        self.cb3.stateChanged.connect(self.changecb2)
        self.cb4.stateChanged.connect(self.changecb2)
        bt.clicked.connect(self.go)
        self.show()

    def go(self):
        if self.cb2.isChecked() and self.cb3.isChecked() and self.cb4.isChecked():
            self.textedit.setText('复选框2,3,4')
        elif self.cb2.isChecked() and self.cb3.isChecked():
            self.textedit.setText('复选框2,3')
        elif self.cb2.isChecked() and self.cb4.isChecked():
            self.textedit.setText('复选框2,4')
        elif self.cb3.isChecked() and self.cb4.isChecked():
            self.textedit.setText('复选框3,4')
        elif self.cb2.isChecked():
            self.textedit.setText('复选框2')
        elif self.cb3.isChecked():
            self.textedit.setText('复选框3')
        elif self.cb4.isChecked():
            self.textedit.setText('复选框4')
        else:
            print('nonono')

    def changecb1(self):
        if self.cb1.checkState() == Qt.Checked:
            self.cb2.setChecked(True)
            self.cb3.setChecked(True)
            self.cb4.setChecked(True)
        elif self.cb1.checkState() == Qt.Unchecked:
            self.cb2.setChecked(False)
            self.cb3.setChecked(False)
            self.cb4.setChecked(False)

    def changecb2(self):
        if self.cb2.isChecked() and self.cb3.isChecked() and self.cb4.isChecked():
            self.cb1.setCheckState(Qt.Checked)
        elif self.cb2.isChecked() or self.cb3.isChecked() or self.cb4.isChecked():
            self.cb1.setTristate()
            self.cb1.setCheckState(Qt.PartiallyChecked)
        else:
            self.cb1.setTristate(False)
            self.cb1.setCheckState(Qt.Unchecked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())