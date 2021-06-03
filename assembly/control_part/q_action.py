import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MyMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.resize(380, 300)
        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 380, 23))
        self.menu = QMenu(self.menubar)
        self.menu_2 = QMenu(self.menubar)

        self.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.toolBar = QToolBar(self)
        self.toolBar.setObjectName("toolBar")
        self.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.action_open = QAction(self)
        self.action_open.setObjectName("action_open")
        self.action_store = QAction(self)
        self.action_store.setObjectName("action_store")
        self.action_close = QAction(self)
        self.action_close.setObjectName("action_close")

        self.actionX = QAction(self)
        self.actionX.setObjectName("actionX")
        self.actionY = QAction(self)
        self.actionY.setObjectName("actionY")
        self.actionZ = QAction(self)
        self.actionZ.setObjectName("actionZ")

        self.menu.addAction(self.action_open)
        self.menu.addAction(self.action_store)
        self.menu.addAction(self.action_close)

        self.menu_2.addAction(self.actionX)
        self.menu_2.addAction(self.actionY)
        self.menu_2.addAction(self.actionZ)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.toolBar.addAction(self.action_open)
        self.toolBar.addAction(self.action_store)
        self.toolBar.addAction(self.action_close)

        self.toolBar.addAction(self.actionX)
        self.toolBar.addAction(self.actionY)
        self.toolBar.addAction(self.actionZ)

        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "可视化编程与测绘"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "绘图"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_open.setText(_translate("MainWindow", "打开"))
        self.action_store.setText(_translate("MainWindow", "保存"))
        self.action_close.setText(_translate("MainWindow", "关闭"))
        self.actionX.setText(_translate("MainWindow", "X方向"))
        self.actionY.setText(_translate("MainWindow", "Y方向"))
        self.actionZ.setText(_translate("MainWindow", "Z方向"))

        self.action_close.triggered.connect(self.call_back_action_close_func)

        self.action_open.triggered.connect(self.call_back_action_open_func)

        self.action_store.triggered.connect(self.call_back_action_store_func)

        self.actionX.triggered.connect(self.call_back_actionX_func)
        self.actionY.triggered.connect(self.call_back_actionY_func)
        self.actionZ.triggered.connect(self.call_back_actionZ_func)

    def call_back_actionX_func(self):
        print("call_back_actionX_func")
        self.statusbar.showMessage("call_back_actionX_func")

    def call_back_actionY_func(self):
        print("call_back_actionY_func")
        self.statusbar.showMessage("call_back_actionY_func")

    def call_back_actionZ_func(self):
        print("call_back_actionZ_func")
        self.statusbar.showMessage("call_back_actionZ_func")

    def call_back_action_store_func(self):
        print("call_back_action_store_func")
        self.statusbar.showMessage("call_back_action_store_func")

    def call_back_action_open_func(self):
        print("call_back_action_open_func")
        self.statusbar.showMessage("call_back_action_open_func")

    def call_back_action_close_func(self):
        print("call_back_action_close_func")
        self.statusbar.showMessage("call_back_action_close_func")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
