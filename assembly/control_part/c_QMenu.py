from PySide2.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu

app = QApplication([])

MainWindow = QMainWindow()

MenuBar = MainWindow.menuBar()                  #获取主对话框的菜单栏
MenuBar.resize(100, 20)

MenuA = MenuBar.addMenu("MenuA")                #给MenuBar添加菜单
MenuA1 = MenuA.addMenu("A1")                    #菜单嵌套子菜单
MenuA1.addAction("A1a")
MenuA1.addAction("A1b")
ActionA2 = MenuA.addAction("A2")                #菜单添加Action
MenuB = MenuBar.addMenu("MenuB")
MenuB1 = MenuB.addMenu("B1")
MenuB1.addAction("B1a")
MenuB1.addAction("B1b")
MenuB.addAction("B2")

MainWindow.show()
app.exec_()
