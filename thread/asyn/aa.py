# -*- coding:utf-8 -*-
import threading
import time

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton


class CreateThread(QThread):
    signal_time = QtCore.pyqtSignal(str,int)
    def __init__(self, parent=None):
        super(CreateThread,self).__init__(parent)

    def start_thread(self):
        self.start()

    def run(self):
        print('start block')
        print('new thread :', threading.current_thread())
        time.sleep(3)    #模拟阻塞
        self.signal_time.emit("new button","aaa")
        print('end block')


# -*- coding:utf-8 -*-
import threading



class TestUI(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.instance = self
        self.setGeometry(100,100,500,400)
        self.layout = QGridLayout()
        self.btnTest = QPushButton()
        self.btnTest.setText("单击, 异步动态添加控件")
        self.btnTest.setGeometry(QtCore.QRect(190, 74, 75, 23))
        self.layout.addWidget(self.btnTest)
        self.setLayout(self.layout)

        self.timetool = CreateThread()
        self.timetool.signal_time.connect(self.add_widget)

        self.btnTest.clicked.connect(self.click_start_btn)
        pass

    def click_start_btn(self):
        self.timetool.start_thread()

    def add_widget(self, text):
        btnaaa = QPushButton()
        btnaaa.setText(text)
        self.layout.addWidget(btnaaa)

    def keyPressEvent(self, e):
        print(e.key())

if __name__ == '__main__':
    print(threading.current_thread())
    import sys
    app = QApplication(sys.argv)
    form = TestUI()
    form.show()
    sys.exit(app.exec_())
