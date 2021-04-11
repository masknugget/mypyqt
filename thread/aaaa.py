import sys
import time
from PyQt5 import QtWidgets, QtCore

class WorkerThread(QtCore.QObject):
    signalExample = QtCore.pyqtSignal(str, int)

    def __init__(self):
        super().__init__()

    @QtCore.pyqtSlot()
    def run(self):
        while True:
            self.signalExample.emit("leet", 1337)
            time.sleep(5)

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.worker = WorkerThread()
        self.workerThread = QtCore.QThread()
        self.workerThread.started.connect(self.worker.run)
        self.worker.signalExample.connect(self.signalExample)
        self.worker.moveToThread(self.workerThread)
        self.workerThread.start()

    def signalExample(self, text, number):
        print(text)
        print(number)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    gui = Main()
    sys.exit(app.exec())