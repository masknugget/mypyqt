from PyQt5.Qt import *
import sys

#0.创建一个APP
app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle("QToolButton")
w.resize(300,300)

#创建一个 QToolButton
tb = QToolButton(w)
tb.setIcon(QIcon("menu.ico"))
#设置自动提示
tb.setAutoRaise(True)
w.show()

sys.exit(app.exec_())
