import sys
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar

class MyWorker(QThread):
    timeout = pyqtSignal()

    def __init__(self):
        super(MyWorker, self).__init__()

    def run(self):
        while True:
            self.timeout.emit()
            self.sleep(1)

class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.currentValue = 0

        self.progessBar = QProgressBar(self)
        self.progessBar.resize(200, 50)
        self.progessBar.move(20, 20)
        self.progessBar.setValue(self.currentValue)

        self.worker = MyWorker()
        self.worker.timeout.connect(self.upgradeProgress)
        self.worker.start()

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
