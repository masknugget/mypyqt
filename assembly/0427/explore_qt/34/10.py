import sys
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QColor, QBrush
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsScene, QGraphicsView


class Demo(QGraphicsView):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 500, 500)
        self.ellipse = self.scene.addEllipse(QRectF(200, 200, 50, 50), brush=QBrush(QColor(Qt.blue)))
        self.rect = self.scene.addRect(QRectF(300, 300, 50, 50), brush=QBrush(QColor(Qt.red)))
        self.ellipse.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.rect.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)

        self.setScene(self.scene)

        self.press_x = None

    # 1
    def wheelEvent(self, event):
        if event.angleDelta().y() < 0:
            self.scale(0.9, 0.9)
        else:
            self.scale(1.1, 1.1)
        # super().wheelEvent(event)

    # 2
    def mousePressEvent(self, event):
        self.press_x = event.x()
        # super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.x() > self.press_x:
            self.rotate(10)
        else:
            self.rotate(-10)
        # super().mouseMoveEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

    