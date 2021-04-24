import sys

import PySide2
from PySide2.QtGui import QPainter, Qt, QPen, QBrush, QPainterPath
from PySide2.QtWidgets import QWidget, QApplication


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle(u'asdada')
        self.resize(600, 300)


    def paintEvent(self, event:PySide2.QtGui.QPaintEvent) -> None:
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        p.setPen(QPen(Qt.black, 1, Qt.DashLine))
        p.drawLine(200, 0, 200, 300)
        p.drawLine(400, 0, 400, 300)

        p.setPen(QPen(Qt.blue, 2, Qt.SolidLine))
        p.setBrush(QBrush(Qt.green, Qt.SolidPattern))

        #
        path = QPainterPath()
        path.addRect(-50, -80, 100, 160)

        p.save()
        p.translate(100, 150)
        p.drawPath(path)
        p.restore()

        p.translate(300, 150)
        p.scale(0.8, 0.8)
        p.rotate(45)
        p.drawPath(path)

        p.resetTransform()
        p.translate(500, 150)
        p.rotate(90)
        p.drawPath(path)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


