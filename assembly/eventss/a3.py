from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QApplication


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = QWidget()

    # 键盘监听事件，当按下ctrl+Z的组合是，关闭窗口
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Z and event.modifiers() == Qt.ControlModifier:
            self.close()


if __name__ == "__main__":
    app = QApplication([])
    mainwindow = MainWindow()

    # 全屏显示
    mainwindow.showFullScreen()
    app.exec_()