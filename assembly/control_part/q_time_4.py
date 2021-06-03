from PyQt5.Qt import *
import sys

#1. 继承QLabel类
class MyLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        #2. 设置标签的基本属性
        self.setText('10')
        self.move(115,55)
        self.setStyleSheet('font-size: 30px;')
        self.setText('8')
        #3. 开始定时器，并记录 id
        self.timer_id = self.startTimer(1000)
    #4. 重写定时器事件
    def timerEvent(self,evt):
        #5.获取当前秒数，
        cur_sec = int(self.text())  #将文本转为整型，否则无法正确计算
        cur_sec -= 1
        self.setText(str(cur_sec))  #将整型转为字符串，否则无法正确显示

        #当秒数为0时候，停止定时器
        if cur_sec == 0:
            self.killTimer(self.timer_id)

app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle('定时器')
w.resize(250,160)

lab = MyLabel(w)

w.show()

if __name__ == '__main__':
    sys.exit(app.exec_())
