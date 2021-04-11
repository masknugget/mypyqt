from PySide2.QtWidgets import QApplication, QMainWindow, QStatusBar, QLabel, QPushButton, QLineEdit

app = QApplication([])

MainWindow = QMainWindow()
MainWindow.resize(400, 200)

Label = QLabel("初始文本", MainWindow)

PushBUtton = QPushButton("按钮", MainWindow)

LineEdit = QLineEdit("初始文本", MainWindow)

StatusBar = QStatusBar(MainWindow)
StatusBar.move(0, 170)                                  #设置到窗口底部显示
StatusBar.resize(400, 30)
StatusBar.addWidget(Label)                              #把空间添加到左侧
StatusBar.addWidget(PushBUtton)
StatusBar.addPermanentWidget(LineEdit)                  #把空间添加到右侧

MainWindow.show()
app.exec_()
