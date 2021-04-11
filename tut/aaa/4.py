from PySide2.QtWidgets import QApplication, QWidget, QLabel, QToolTip
import sys
from PySide2.QtGui import QIcon, QPixmap, QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Icon Modes")
        self.setGeometry(300, 300, 500, 400)

        QToolTip.setFont(QFont("Decorative", 10, QFont.Bold))
        self.setToolTip('Our Main Window')

    def setIcon(self):
        appIcon = QIcon("wan.ico")
        self.setWindowIcon(appIcon)

    def setIconModes(self):
        icon1 = QIcon("wan.ico")
        label1 = QLabel('Sample', self)
        pixmap1 = icon1.pixmap(100, 100, QIcon.Active, QIcon.On)
        label1.setPixmap(pixmap1)
        label1.setToolTip("Active Icon")

        icon2 = QIcon("wan.ico")
        label2 = QLabel('Sample', self)
        pixmap2 = icon2.pixmap(100, 100, QIcon.Disabled, QIcon.Off)
        label2.setPixmap(pixmap2)
        label2.move(100, 0)
        label2.setToolTip("Disable Icon")

        icon3 = QIcon("wan.ico")
        label3 = QLabel('Sample', self)
        pixmap3 = icon3.pixmap(100, 100, QIcon.Selected, QIcon.On)
        label3.setPixmap(pixmap3)
        label3.move(200, 0)
        label3.setToolTip("Selected Icon")


myApp = QApplication(sys.argv)
window = Window()
window.setIcon()
window.setIconModes()
window.show()

myApp.exec_()
sys.exit(0)