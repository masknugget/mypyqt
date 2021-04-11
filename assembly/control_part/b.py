from PySide2.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton
from PySide2.QtGui import QIcon

app = QApplication([])

MainWindow = QMainWindow()

Icon = QIcon(".\png\Icon.ico")

PushButton1 = QPushButton(MainWindow)
PushButton1.setIcon(Icon)
PushButton2 = QPushButton(MainWindow)
PushButton2.setIcon(Icon)
PushButton3 = QPushButton(MainWindow)
PushButton3.setText("初始文本")

ToolBar = MainWindow.addToolBar("Tool Bar")
ToolBar.addWidget(PushButton1)
ToolBar.addWidget(PushButton2)
ToolBar.addWidget(PushButton3)

MainWindow.show()
app.exec_()
