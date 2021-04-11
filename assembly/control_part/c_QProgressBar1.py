import time
from PySide2.QtWidgets import QApplication, QMainWindow, QProgressBar, QPushButton
from PySide2.QtCore import Slot

app = QApplication([])

MainWindow = QMainWindow()

ProgressBar = QProgressBar(MainWindow)
ProgressBar.move(2, 0)
ProgressBar.resize(100, 20)                             #设置大小
ProgressBar.setRange(0, 100)                            #设置范围
ProgressBar.setValue(0)                                 #设置当前进度值

PushButton = QPushButton(MainWindow)
PushButton.setText("开始")
PushButton.move(110, 0)
PushButton.resize(50, 20)

@Slot()
def TestProgressBar():
    for Percent in range(100 + 1):                      #从0计数到100
        ProgressBar.setValue(Percent)                   #设置当前进度值
        time.sleep(0.05)                                #延迟50ms

    ProgressBar.reset()                                 #重置进度条

PushButton.clicked.connect(TestProgressBar)

MainWindow.show()
app.exec_()
