import sys

from PySide2.QtWebEngineWidgets import QWebEngineView


from PyQt5.QtCore import QUrl,Qt
from PyQt5.QtWidgets import QWidget, QLabel, QApplication,QMainWindow,QVBoxLayout,QHBoxLayout,QLineEdit,QPushButton,QDialog

class MyPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口")
        self.showMaximized()
        self.browser = QWebEngineView()
        self.browser.load(QUrl("http://www.baidu.com"))
        # 如果这里setCentralWidget且子窗口作为父窗口的子组件显示不出来
        # 如果不作为子组件，则是两个窗口
        self.setCentralWidget(self.browser)

    def keyPressEvent(self, event):
        if(QApplication.keyboardModifiers() == Qt.ControlModifier and event.key() == Qt.Key_F):
            # self.searchBox = SearchBox(self) # 指定为子组件
            self.searchBox = SearchBox()
            self.searchBox.show()

class SearchBox(QLineEdit): # 我现在通过一个新窗口的方式去做，感觉不好
     def __init__(self):
        super().__init__()
        self.setWindowTitle("子窗口")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyPage()
    ex.show()
    sys.exit(app.exec_())