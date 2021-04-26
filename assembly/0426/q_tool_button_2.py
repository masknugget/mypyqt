from PyQt5.Qt import *
import sys

#0.创建一个APP
app = QApplication(sys.argv)


w = QWidget()
w.setWindowTitle("QToolButton")
w.resize(300,300)

#创建一个 QToolButton
tb = QToolButton(w)
tb.setToolTip("这是一个菜单工具图标")
tb.setIcon(QIcon("menu.ico"))

w.show()

sys.exit(app.exec_())
