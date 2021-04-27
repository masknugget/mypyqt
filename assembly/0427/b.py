from PyQt5.QtCore import QThread, pyqtSignal, QDateTime, QObject,QEvent
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QLabel
import time
import sys


class BackendThread(QObject):
    # 通过类成员对象定义信号
    update_date = pyqtSignal(str)

    # 处理业务逻辑
    def run(self):
        while True:
            data = QDateTime.currentDateTime()
            currTime = data.toString("yyyy-MM-dd hh:mm:ss")
            self.update_date.emit(str(currTime))
            time.sleep(1)


class Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle('PyQt 5界面实时更新例子')
        self.resize(400, 100)
        self.input = QLabel(self)
        self.input.resize(400, 100)
        self.initUI()

    def initUI(self):
        # 创建线程
        self.backend = BackendThread()
        # 连接信号
        self.backend.update_date.connect(self.handleDisplay)
        self.thread = QThread()
        self.backend.moveToThread(self.thread)
        # 开始线程
        self.thread.started.connect(self.backend.run)
        self.thread.start()



    # 将当前时间输出到文本框
    def handleDisplay(self, data):
        self.input.setText(data)

    def keyPressEvent(self, event):
        print('keyPressEvent')
        pass

    def eventFilter(self, objwatched, event):
        eventType = event.type()
        #print(eventType)
        if eventType == QEvent.KeyPress:
            print('eventFilter KeyPress')

        elif eventType == QEvent.MetaCall:
            print('eventFilter MetaCall')
        return super().eventFilter(objwatched, event)

    #
    # def eventFilter(self, obj, event):
    #     if obj == self.lineEdit:
    #         if event.type() == QEvent.FocusIn:
    #             # self.inp_text_signal.emit("已进")
    #             if self.lineEdit.text().strip() == '请输入用户名':
    #                 self.lineEdit.clear()
    #
    #             print("ok1")
    #         elif event.type() == QEvent.FocusOut:
    #             if self.lineEdit.text().strip() == '':
    #                 self.lineEdit.setText("请输入用户名")
    #             print("ok2")
    #         else:
    #             pass
    #         return False
    #


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    app.installEventFilter(win)
    sys.exit(app.exec_())