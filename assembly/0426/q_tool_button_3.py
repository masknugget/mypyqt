from PyQt5.Qt import *
import sys

#0.创建一个APP
app = QApplication(sys.argv)


w = QWidget()
w.setWindowTitle("QToolButton")
w.resize(300,300)

#创建一个 QToolButton
tb = QToolButton(w)
tb.setText("工具")
tb.setIcon(QIcon("menu.ico"))

#设置文本显示在图标右侧
tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

w.show()

sys.exit(app.exec_())
