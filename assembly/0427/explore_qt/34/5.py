import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsScene, \
                            QGraphicsView


class Demo(QGraphicsView):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 300, 300)

        self.rect = QGraphicsRectItem()
        self.ellipse = QGraphicsEllipseItem()
        self.rect.setRect(120, 30, 50, 30)
        self.ellipse.setRect(100, 180, 100, 50)
        self.rect.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        self.ellipse.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)

        self.scene.addItem(self.rect)
        self.scene.addItem(self.ellipse)

        self.setScene(self.scene)

    def mouseMoveEvent(self, event):
        if self.ellipse.collidesWithItem(self.rect, Qt.IntersectsItemBoundingRect):
            print(self.ellipse.collidingItems(Qt.IntersectsItemShape))
        super().mouseMoveEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())