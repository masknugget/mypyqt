from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject,QRect
import sys


#组件Label的类 传入QLabel 也可以传入QObject 等
class Label(QLabel):
    #这里要带入父类
    def __init__(self,par):
        #继承父类 这里记得带上par 父类
        super(Label, self).__init__(par)
        self.d = par
        self.setText("10")
    def timerEvent(self,evt):
        sum = int(self.text())
        sum -= 1
        if sum==5:
            #只能在此类下进行终止定时器
            self.killTimer(self.d.id)
        else:
            self.setText(str(sum))

class LoginDlg(QDialog):

    def setui(self):
        self.setWindowTitle("这是一个定时器")
        self.resize(300,200)
        self.btn = QPushButton(self)
        self.btn.setText("按钮")
        print(111)
        self.btn.setGeometry(QRect(180, 10, 100, 50))
        #实例化这个label类
        label = Label(self)
        label.move(70, 20)
        #启动定时器
        self.id = label.startTimer(1000)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = LoginDlg()
    ui.setui()
    ui.show()
    sys.exit(app.exec_())
