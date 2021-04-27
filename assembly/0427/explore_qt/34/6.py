import sys
from PyQt5.QtCore import QPropertyAnimation, QPointF, QRectF, pyqtSignal
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsObject


class CustomRect(QGraphicsObject):
    # 1
    my_signal = pyqtSignal()

    def __init__(self):
        super(CustomRect, self).__init__()

    # 2
    def boundingRect(self):
        return QRectF(0, 0, 100, 30)

    # 3
    def paint(self, painter, styles, widget=None):
        painter.drawRect(self.boundingRect())


class Demo(QGraphicsView):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)

        # 4
        self.rect = CustomRect()
        self.rect.my_signal.connect(lambda: print('signal and slot'))
        self.rect.my_signal.emit()

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 300, 300)
        self.scene.addItem(self.rect)

        self.setScene(self.scene)

        # 5
        self.animation = QPropertyAnimation(self.rect, b'pos')
        self.animation.setDuration(3000)
        self.animation.setStartValue(QPointF(100, 30))
        self.animation.setEndValue(QPointF(100, 200))
        self.animation.setLoopCount(-1)
        self.animation.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())