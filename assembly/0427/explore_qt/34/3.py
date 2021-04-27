import sys
from PyQt5.QtWidgets import QApplication, QGraphicsRectItem, QGraphicsScene, QGraphicsView


class CustomItem(QGraphicsRectItem):
    def __init__(self, num):
        super(CustomItem, self).__init__()
        self.setRect(100, 30, 100, 30)
        self.num = num

    def mousePressEvent(self, event):
        print('event from QGraphicsItem{}'.format(self.num))
        super().mousePressEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = QGraphicsView()
    scene = QGraphicsScene()
    item1 = CustomItem(1)
    item2 = CustomItem(2)
    item2.setParentItem(item1)

    scene.addItem(item1)
    view.setScene(scene)

    view.show()
    sys.exit(app.exec_())