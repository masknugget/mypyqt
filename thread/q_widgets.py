import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar

class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.currentValue = 0

        self.progessBar = QProgressBar(self)
        self.progessBar.resize(200, 50)
        self.progessBar.move(20, 20)
        self.progessBar.setValue(self.currentValue)

        # 定义一个定时器并启动定时器
        self.time = QTimer()
        self.time.timeout.connect(self.upgradeProgress)
        self.time.start(200)

    def upgradeProgress(self):
        self.currentValue = (self.currentValue + 1) % 101
        self.progessBar.setValue(self.currentValue)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.resize(500, 300)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    sys.exit(app.exec_())
