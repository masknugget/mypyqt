from PySide2.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu
from PySide2.QtGui import QIcon

app = QApplication([])

MainWindow = QMainWindow()

Icon = QIcon(".\png\Icon.ico")

MenuBar = MainWindow.menuBar()                  #获取主对话框的菜单栏
MenuBar.resize(100, 20)

MenuA = MenuBar.addMenu("MenuA")                #给MenuBar添加菜单，MenuA文本将不会显示
MenuA.setIcon(Icon)
MenuA1 = MenuA.addMenu("A1")                    #菜单嵌套子菜单
MenuA1.setIcon(Icon)
MenuA.addSeparator()                            #添加分割线
ActionA1a = MenuA1.addAction("A1a")
ActionA1a.setIcon(Icon)
MenuA1.addSeparator()                           #添加分割线
ActionA1b = MenuA1.addAction("A1b")
ActionA1b.setIcon(Icon)
ActionA1c = MenuA1.addAction("A1c")
ActionA1c.setIcon(Icon)
ActionA2 = MenuA.addAction("A2")                #菜单添加Action
ActionA2.setIcon(Icon)

MainWindow.show()
app.exec_()
