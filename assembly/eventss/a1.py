
# PySide2 窗口退出时处理函数
from PySide2.QtWidgets import QApplication


def close_timer(self):
    if self.scanning_timer != None:
        self.scanning_timer.cancel()
    if self.polling_timer != None:
        self.scanning_timer.cancel()


if __name__ == '__main__':
    app = QApplication([])  # 初始化应用
    main_window = MainWindow()  # 创建主窗口

    # main_window.ui.show()  # 按实际大小显示窗口
    main_window.ui.showMaximized()  # 全屏显示窗口，必须要用，不然不显示界面

    # 退出时关闭所有 Timer
    app.aboutToQuit.connect(main_window.close_timer)

    # 应用关闭时返回0,sys关闭进程
    sys.exit(app.exec_())

