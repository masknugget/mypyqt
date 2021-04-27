import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)  # 1

    def mousePressEvent(self, event):  # 2
        self.start_x = event.x()
        self.start_y = event.y()

    def mouseMoveEvent(self, event):  # 3
        dis_x = event.x() - self.start_x
        dis_y = event.y() - self.start_y
        self.move(self.x() + dis_x, self.y() + dis_y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())