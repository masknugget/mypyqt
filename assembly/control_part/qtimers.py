from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject,QRect
import sys


#只能在类外部进行终止定时器 我是没能知道怎么在内部进行终止
#类包含一个timeEvent定时器
class myobject(QObject):
    #这是每个对象所包含的一个定时器函数
    def timerEvent(self,event):
        #不能在这个类下面进行终止
        print(event,"1")


class LoginDlg(QDialog):

    def setui(self):
        self.setWindowTitle("这是一个定时器")
        self.resize(300,200)
        self.btn = QPushButton(self)
        self.btn.setText("按钮")

        self.btn.setGeometry(QRect(180, 10, 100, 50))


        self.btn.clicked.connect(self.pause)
        # 先把这个类实例化
        self.obj = myobject(self)
        #启动定时器并把这个定时器赋值到self.id
        self.id = self.obj.startTimer(1000)

    def pause(self):

        #终止这个类下的定时器
        self.obj.killTimer(self.id)
        print("已停止")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = LoginDlg()
    ui.setui()
    ui.show()
    sys.exit(app.exec_())
