# 无边框简单的移动事件
class Mywindow(QMainWindow):
    def __int__(self):
        super().__init__()

    def mousePressEvent(self, event):  ##事件开始
        if event.button() == QtCore.Qt.LeftButton:
            self.Move = True  ##设定bool为True
            self.Point = event.globalPos() - self.pos()  ##记录起始点坐标
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):  ##移动时间
        if QtCore.Qt.LeftButton and self.Move:  ##切记这里的条件不能写死，只要判断move和鼠标执行即可！
            self.move(QMouseEvent.globalPos() - self.Point)  ##移动到鼠标到达的坐标点！
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):  ##结束事件
        self.Move = False


class GUI():
    def __init__(self):
        self.window = Mywindow()  ##记得要引用重写的函数，而不是QmainWindow（）

