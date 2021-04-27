from PyQt5.QtCore import pyqtProperty
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QPushButton


class MyButton(QPushButton):
    def __init__(self, text=None, parent=None):
        super(MyButton, self).__init__(text, parent)
        self._color = QColor()

    @pyqtProperty(QColor)
    def color(self):
        return self._color

    @color.setter
    def color(self, col):
        self._color = col
        self.setStyleSheet('background-color: rgb({}, {}, {})'.format(col.red(), col.green(), col.blue()))




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