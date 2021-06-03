#!/usr/bin/python3
# coding:utf-8

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, QRect, QTimer
import sys


# 记得导入定时器 也只能在这个类下停止
# QTime貌似只能stop不能kill 不停止重新调用就会 加快
class LoginDlg(QDialog):

    def setui(self):
        self.setWindowTitle("这是一个定时器")
        self.resize(300, 200)
        self.btn = QPushButton(self)
        self.btn.setText("点击开始")
        self.btn.setGeometry(QRect(180, 10, 100, 50))
        self.btn.clicked.connect(self.star)

    def a(self):
        print(1)

    def star(self):
        # 这里是错误的示范 应该写在上面的启动窗口里面 具体原因看最后
        # 实例化定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.a)
        # 注意这里是start不是startTimer
        self.timer.start(1000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = LoginDlg()
    ui.setui()
    ui.show()
    sys.exit(app.exec_())
