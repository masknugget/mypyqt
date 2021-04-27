import sys
from PyQt5.QtWidgets import QApplication, QWidget


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(100, 100)
        self.center()

    def center(self):
        # 1
        desktop = QApplication.desktop()
        d_width = desktop.width()
        d_height = desktop.height()

        # 2
        pos_x = d_width / 2 - self.frameGeometry().width() / 2
        pos_y = d_height / 2 - self.frameGeometry().height() / 2

        # 3
        self.move(int(pos_x), int(pos_y))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())