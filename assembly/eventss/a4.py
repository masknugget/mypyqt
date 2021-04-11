# Qmainwindow之间的界面简单的跳转
self.QPushButtonregister.clicked.connect(self.Register)  ##写好connect的跳转函数

def Register(self):##在主函数里面引入跳转界面的类，并show！
     self.register = Registerwindow()
     self.register.Subwindow.show()

##要跳转的界面，写在主函数下段；
class Registerwindow():
    def __init__(self):
        self.Subwindow = QMainWindow()
        self.Subwindow.resize(300, 600)
