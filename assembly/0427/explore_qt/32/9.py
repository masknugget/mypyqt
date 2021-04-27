import sys
from PyQt5.QtCore import QTimeLine
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

'''
    QTimeLine.NotRunningQTimeLine.RunningQTimeLine.Paused

在未开始或者运行结束时，QTimeLine就会处于NotRunning状态；当调用start()方法启动后，变为Running状态，期间QTimeLine会不断发出frameChanged信号；而当在运行中调用setPaused(True)让QTimeLine暂停的话，状态就会变为Paused。每当状态发生改变，QTimeLine都会发出stateChanged信号，我们可以根据该信号来判断动画所处的状态并作相应的处理。

以下四个方法用于改变QTimeLine状态：

    start()：让QTimeLine进入Running状态。stop()：让QTimeLine进入NotRunning状态。resume()：让QTimeLine从Paused状态或者NotRunning状态转为Running状态，动画从当前帧继续(注意start()方法不是从当前帧继续，而是直接从头开始)。setPaused()：传入True，让QTimeLine进入Paused状态；传入False，让QTimeLine进入Running状态(传入False时QTimeLine的状态必须为Paused)。
'''
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.label = QLabel('Hello PyQt5', self)
        self.label.move(-100, 100)

        self.timeline = QTimeLine(5000, self)                       # 1
        self.timeline.setFrameRange(0, 700)                         # 2
        self.timeline.frameChanged.connect(self.set_frame_func)     # 3
        self.timeline.setLoopCount(0)                               # 4
        self.timeline.start()

    def set_frame_func(self, frame):
        self.label.move(-100+frame, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
