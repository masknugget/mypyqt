import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QPixmap, QLinearGradient, QRadialGradient, QConicalGradient
from PyQt5.QtWidgets import QApplication, QWidget


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.brush1 = QBrush(Qt.SolidPattern)                   # 1

        self.brush2 = QBrush(Qt.Dense6Pattern)                  # 2
        self.brush2.setColor(Qt.red)

        gradient1 = QLinearGradient(200, 200, 300, 300)         # 3
        gradient1.setColorAt(0.2, Qt.red)
        gradient1.setColorAt(0.8, Qt.green)
        gradient1.setColorAt(1, Qt.blue)
        self.brush3 = QBrush(gradient1)

        gradient2 = QRadialGradient(350, 350, 50, 350, 350)     # 4
        gradient2.setColorAt(0, Qt.red)
        gradient2.setColorAt(1, Qt.blue)
        self.brush4 = QBrush(gradient2)

        gradient3 = QConicalGradient(450, 450, 90)              # 5
        gradient3.setColorAt(0, Qt.red)
        gradient3.setColorAt(1, Qt.blue)
        self.brush5 = QBrush(gradient3)

        self.brush6 = QBrush(Qt.TexturePattern)                 # 6
        self.brush6.setTexture(QPixmap('images/smile.png'))

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.setBrush(self.brush1)                           # 7
        painter.drawRect(0, 0, 100, 100)

        painter.setBrush(self.brush2)
        painter.drawRect(100, 100, 100, 100)

        painter.setBrush(self.brush3)
        painter.drawRect(200, 200, 100, 100)

        painter.setBrush(self.brush4)
        painter.drawRect(300, 300, 100, 100)

        painter.setBrush(self.brush5)
        painter.drawRect(400, 400, 100, 100)

        painter.setBrush(self.brush6)
        painter.drawRect(500, 500, 100, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())