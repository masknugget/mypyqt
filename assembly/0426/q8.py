from PyQt5.Qt import *
import sys

#0.创建一个APP
app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle("QToolButton")
w.resize(300,300)

#创建菜单
menu = QMenu()
#创建子菜单
sub_menu = QMenu(menu)
sub_menu.setTitle("子菜单")
sub_menu.setIcon(QIcon("menu.ico"))

#在菜单中添加子菜单
menu.addMenu(sub_menu)

#创建action并添加到菜单中
act0 = QAction(QIcon("menu.ico"),"行为_0",menu)
act1 = QAction(QIcon("menu.ico"),"行为_1",menu)
act2 = QAction(QIcon("menu.ico"),"行为_3",menu)

menu.addActions([act0,act1,act2])

act0.setData("act0")
act1.setData("act1")
act2.setData("act2")


#创建一个 QToolButton
tb = QToolButton(w)
tb.setIcon(QIcon("menu.ico"))
tb.setAutoRaise(True)

#QToolBool添加菜单
tb.setMenu(menu)


def action_slot(action):
    print(action.data())

tb.triggered.connect(action_slot)

w.show()

sys.exit(app.exec_())
