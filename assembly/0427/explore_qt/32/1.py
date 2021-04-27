import sys
from PyQt5.QtCore import QPropertyAnimation, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.btn = QPushButton('Bigger', self)
        self.btn.resize(100, 100)

        self.animation = QPropertyAnimation(self.btn, b'size')  # 1
        self.animation.setDuration(6000)                        # 2
        self.animation.setStartValue(QSize(100, 100))           # 3
        self.animation.setEndValue(QSize(600, 600))             # 4
        self.animation.start()                                  # 5


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())