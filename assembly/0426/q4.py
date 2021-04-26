from PyQt5.Qt import *
import sys

#0.创建一个APP
app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle("QToolButton")
w.resize(300,300)

#创建一个 QToolButton
tb = QToolButton(w)
#显示一个向上的箭头
tb.setArrowType(Qt.UpArrow)

w.show()
sys.exit(app.exec_())
