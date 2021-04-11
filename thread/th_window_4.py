import sys
import time
import socket
import os
from message import Ui_Form
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#主类
class mymainwindow(QMainWindow,Ui_Form):
    def __init__(self,parent=None):
        super(mymainwindow, self).__init__(parent)
        self.setupUi(self)
	#线程测试开始
    def threadstartslot(self):
        self.work = Thread()
        self.work.trigger.connect(self.deal)#线程中的trigger与主类中的方法进行绑定
        self.work.start()#开启线程
    #线程测试停止
    def threadstopslot(self):
        self.work.threadstartflag=False
	#更新UI方法
    def deal(self,str):
        self.textEdit.append(str)
#线程类
class Thread(QThread):
    trigger = pyqtSignal(str)#注意pyqtSignal一定要实例到__init__前面
    def __init__(self):
        super(Thread, self).__init__()
		#定义的变量
        self.threadstartflag=True
        self.timecount=0
	#执行耗时操作
    def run(self):
        while self.threadstartflag == True:
            self.trigger.emit(u"计时%d"%self.timecount)#发送更新GUI的信号
            self.timecount+=1
            time.sleep(1)
#显示GUI
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = mymainwindow()
    MainWindow.show()
    sys.exit(app.exec_())
