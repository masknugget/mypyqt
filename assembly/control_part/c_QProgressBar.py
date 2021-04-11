from PySide2.QtWidgets import QApplication, QMainWindow, QProgressBar

app = QApplication([])

MainWindow = QMainWindow()

ProgressBar = QProgressBar(MainWindow)
ProgressBar.resize(100, 20)                             #设置大小
ProgressBar.setRange(0, 100)                            #设置范围
ProgressBar.setValue(50)                                #设置当前进度值

MainWindow.show()
app.exec_()
