# Slider拖动条
from PySide2.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QSlider
import sys
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt
from PySide2 import QtGui


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 Slider")
        self.setGeometry(300, 200, 300, 250)

        self.setStyleSheet('background-color:red')

        self.createSlider()

        self.setIcon()
        self.show()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def createSlider(self):
        hbox = QHBoxLayout()

        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)

        self.slider.valueChanged.connect(self.changedValue)

        self.label = QLabel("0")
        self.label.setFont(QtGui.QFont("Sanserif", 15))

        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def changedValue(self):
        size = self.slider.value()
        self.label.setText(str(size))


myapp = QApplication(sys.argv)
window = Window()

myapp.exec_()
sys.exit()