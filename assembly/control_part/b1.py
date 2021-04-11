from PySide2.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QAction, QLineEdit
from PySide2.QtGui import QIcon

app = QApplication([])

MainWindow = QMainWindow()
MainWindow.resize(400, 200)

Icon = QIcon(".\png\Icon.ico")

PushButton1 = QPushButton(MainWindow)
PushButton1.setIcon(Icon)
PushButton1.setToolTip("PushButton Tip")                #设置PushButton作为按钮时的提示信息
PushButton2 = QPushButton(MainWindow)
PushButton2.setText("初始文本")

Action1 = QAction()
Action1.setIcon(Icon)
Action2 = QAction("Action")

LineEdit = QLineEdit("常作为搜索框")

ToolBar = MainWindow.addToolBar("Tool Bar")
ToolBar.setFloatable(False)                             #禁用浮动
ToolBar.setMovable(False)                               #禁用移动
ToolBar.setToolTip("ToolBar Tip")                           #工具栏提示信息
ToolBar.addWidget(PushButton1)                          #工具栏添加按钮
ToolBar.addWidget(PushButton2)
ToolBar.addAction(Action1)                             #工具栏添加Action
ToolBar.addAction(Action2)
ToolBar.addWidget(LineEdit)

MainWindow.show()
app.exec_()
