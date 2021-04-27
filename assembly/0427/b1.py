import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from ctypes.wintypes import MSG


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

    def nativeEvent(self, eventType, msg):
        message = MSG.from_address(int(msg))
        if message.message == 0x219:  # WM_DEVICECHANGE
            if message.wParam == 0x8000:  # DBT_DEVICEARRIVAL
                print("in")
            elif message.wParam == 0x8004:  # DBT_DEVICEREMOVECOMPLETE
                print("out")
            elif message.wParam == 0x0007:  # DBT_DEVNODE_CHANGED
                print("node")
        return False, msg


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())