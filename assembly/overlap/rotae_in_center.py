import sys
import time

import PySide2
from PyQt5.QtCore import QTimer
from PySide2 import QtWidgets
from PySide2.QtCore import QRect, Qt

from PySide2.QtWidgets import QWidget, QBoxLayout, QApplication
from PySide2.QtGui import QFont, QPainter, QTransform, QPen, QBrush


class Widget(QWidget):
    def __init__(self, *args, **kwargs):
        super(Widget, self).__init__(*args, **kwargs)
        self.cnt = 0
        # 新建一个QTimer对象
        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.start()
        # 信号连接到槽
        self.timer.timeout.connect(self.onTimerOut)

    # 定义槽
    def onTimerOut(self):
        self.update()


    # def paintEvent(self, event:PySide2.QtGui.QPaintEvent) -> None:
    #     qp = QPainter()
    #     qp.begin(self)
    #     self.draw_text(qp)
    def paintEvent(self, paintEvent):
        # painter = QPainter(self)
        # painter.translate(self.width() / 2, self.height() / 2)
        # painter.rotate(90)
        # painter.drawText(50, 50, 'aaa')
        # painter.translate(-self.width() / 2, -self.height() / 2)  # 这一步看不懂

        painter = QPainter(self)
        self.draw_text(painter)

    def draw_text(self, qp):


        font = QFont()
        font.setFamily("SimFun")
        font.setPointSizeF(110)
        qp.setFont(font)
        qp.setPen(QPen(Qt.blue, 2, Qt.SolidLine))
        qp.setBrush(QBrush(Qt.green, Qt.SolidPattern))

        # qp.drawText(50, 50, 'aaaaaa')
        qp.save()
        a = QRect(500, 500, 100, 100)

        # qp.drawRect(a)
        print(a.width(), a.height())
        b = QRect(int(-a.width()/2), int(-a.height()/2), a.width(), a.height())

        cx = a.x() + a.width()/2
        cy = a.y() + a.height()/2

        print(a.center())
        qp.drawRect(a)

        # qp.resetTransform()
        qp.translate(cx, cy)
        # transform = QTransform()
        # transform.rotate(self.cnt)
        # qp.setTransform(transform)
        qp.rotate(self.cnt)
        qp.drawText(b, Qt.AlignCenter|Qt.AlignTop, 'bbbb'+str(self.cnt))
        # qp.drawRect(b)
        qp.restore()

        # qp.drawText(50, 50, "Hello, world!")
        #
        # transform.rotate(+90.0)  #// 旋转90度
        # qp.setWorldTransform(transform)
        # qp.drawText(50, 50, "Hello, world!")

        if self.cnt >= 360:
            self.cnt = 0
        else:
            time.sleep(0.1)
            self.cnt += 1



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())


