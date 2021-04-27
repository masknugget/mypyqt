import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()

        x = 0
        y = 0

        self.text = "x: {0},  y: {1}".format(x, y)

        self.label = QLabel(self.text, self)  # 在标签框中显示鼠标坐标
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True)  # True开启跟踪鼠标事件，默认是False关闭，跟踪关闭时只能接收鼠标按键动作，无法跟踪移动轨迹。

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()

    def mouseMoveEvent(self, e):  # e是一个事件对象，它包含被触发事件的数据，在这里被转化成字符串显示出来。

        x = e.x()
        y = e.y()

        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    