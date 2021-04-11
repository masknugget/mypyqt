from PySide2.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu
from PySide2.QtCore import Slot

app = QApplication([])

MainWindow = QMainWindow()

MenuBar = MainWindow.menuBar()                  #获取主对话框的菜单栏
MenuBar.resize(100, 20)

MenuA = MenuBar.addMenu("MenuA")                #给MenuBar添加菜单
MenuA1 = MenuA.addMenu("A1")                    #菜单嵌套子菜单
ActionA1a = MenuA1.addAction("A1a")             #菜单项添加Action
ActionA1b = MenuA1.addAction("A1b")
ActionA2 = MenuA.addAction("A2")

@Slot()
def ClickMenuBar():
    print("Click MenuBar")

@Slot()
def ClickMenuA():
    print("Click MenuA")

@Slot()
def ClickMenuA1():
    print("Click MenuA1")

@Slot()
def ClickMenuA1a():
    print("Click MenuA1a")

@Slot()
def ClickMenuA1b():
    print("Click MenuA1b")

@Slot()
def ClickMenuA2():
    print("Click MenuA2")

MenuBar.triggered.connect(ClickMenuBar)                 #给菜单栏添加点击事件
MenuA.triggered.connect(ClickMenuA)                     #给菜单A添加点击事件
MenuA1.triggered.connect(ClickMenuA1)                   #给菜单A1添加点击事件
ActionA2.triggered.connect(ClickMenuA2)                 #给ActionA2添加点击事件
ActionA1a.triggered.connect(ClickMenuA1a)               #给ActionA1a添加点击事件
ActionA1b.triggered.connect(ClickMenuA1b)               #给ActionA1b添加点击事件

MainWindow.show()
app.exec_()
