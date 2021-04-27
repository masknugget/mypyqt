import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsScene, QGraphicsView


class Demo(QGraphicsView):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 300, 300)

        # 1
        self.rect = self.scene.addRect(100, 30, 100, 30)
        self.ellipse = self.scene.addEllipse(100, 80, 50, 40)
        self.pic = self.scene.addPixmap(QPixmap('pic.png').scaled(60, 60))
        self.pic.setOffset(100, 130)

        self.rect.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsFocusable)
        self.ellipse.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsFocusable)
        self.pic.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsFocusable)

        self.setScene(self.scene)

        # 2
        print(self.scene.items())
        print(self.scene.items(order=Qt.AscendingOrder))
        print(self.scene.itemsBoundingRect())
        print(self.scene.itemAt(110, 40, QTransform()))

        # 3
        self.scene.focusItemChanged.connect(self.my_slot)

    def my_slot(self, new_item, old_item):
        print('new item: {}\nold item: {}'.format(new_item, old_item))

    # 4
    def mouseMoveEvent(self, event):
        print(self.scene.collidingItems(self.ellipse, Qt.IntersectsItemShape))
        super().mouseMoveEvent(event)

    # 5 还需要修改
    def mouseDoubleClickEvent(self, event):
        item = self.scene.itemAt(event.pos(), QTransform())
        self.scene.removeItem(item)
        super().mouseDoubleClickEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
    