import sys
from PyQt5.QtWidgets import QApplication, QGraphicsRectItem, QGraphicsScene, QGraphicsView


class CustomItem(QGraphicsRectItem):
    def __init__(self):
        super(CustomItem, self).__init__()
        self.setRect(100, 30, 100, 30)

    def mousePressEvent(self, event):
        print('event from QGraphicsItem')
        super().mousePressEvent(event)


class CustomScene(QGraphicsScene):
    def __init__(self):
        super(CustomScene, self).__init__()
        self.setSceneRect(0, 0, 300, 300)

    def mousePressEvent(self, event):
        print('event from QGraphicsScene')
        super().mousePressEvent(event)


class CustomView(QGraphicsView):
    def __init__(self):
        super(CustomView, self).__init__()
        self.resize(300, 300)

    def mousePressEvent(self, event):
        print('event from QGraphicsView')
        super().mousePressEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = CustomView()
    scene = CustomScene()
    item = CustomItem()

    scene.addItem(item)
    view.setScene(scene)

    view.show()
    sys.exit(app.exec_())