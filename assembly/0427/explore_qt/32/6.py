import sys
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QPropertyAnimation, pyqtProperty
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class MyButton(QPushButton):
    def __init__(self, text=None, parent=None):
        super(MyButton, self).__init__(text, parent)
        self._color = QColor()

    def get_color(self):
        return self._color

    def set_color(self, col):
        self._color = col
        self.setStyleSheet('background-color: rgb({}, {}, {})'.format(col.red(), col.green(), col.blue()))

    color = pyqtProperty(QColor, fget=get_color, fset=set_color)


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.btn = MyButton('Color', self)
        self.btn.setGeometry(0, 0, 100, 100)

        self.animation = QPropertyAnimation(self.btn, b'color')
        self.animation.setDuration(5000)
        self.animation.setStartValue(QColor(0, 0, 0))
        self.animation.setEndValue(QColor(255, 255, 255))
        self.animation.setLoopCount(-1)
        self.animation.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())