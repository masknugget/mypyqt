'''

PyQt提供了5中事件处理和过滤方法，弱到强，其中前两者常用；

（1）重写事件具体的函数（例如：mousePressEvent()/keyPressEvent()....）

（2）重新实现QObject.event()一般用在PyQt没有提供该事件的处理函数的情况下，即添加一个新的事件；

（3）通过事件过滤器

对QObject调用installEventFilter，则相当于为QObject安装了一个事件过滤器；对于QObject的全部事件来说，他们会先传递到事件过滤函数eventFilter中；

在函数中我们可以放弃或者修改某些事件，如果该过滤事件比较多，则会降低性能；

（4）在QApplication中设置事件过滤器

这种方式比前者更强大，QApplication的事件过滤器会捕获所有QObject的事件，且第一个获得事件，即在任意一个事件过滤器之前捕获；

（5）重写QApplication中notify（）方法；

  使用notify方法来分发事件；想在任意事件处理器之前捕获事件，则唯一方法就是从写notify方法；

例如：（1）（2）重写具体事件和event函数；
'''

#事件机制
#信号与槽（QTabWidget略）自定义参数
from PyQt5.QtWidgets import  QComboBox,QTableView,QAbstractItemView,QHeaderView,QTableWidget, QTableWidgetItem, QMessageBox,QListWidget,QListWidgetItem, QStatusBar,  QMenuBar,QMenu,QAction,QLineEdit,QStyle,QFormLayout,   QVBoxLayout,QWidget,QApplication ,QHBoxLayout, QPushButton,QMainWindow,QGridLayout,QLabel
from PyQt5.QtGui import QIcon,QPixmap,QStandardItem,QStandardItemModel,QCursor,QFont,QBrush,QColor,QPainter
from PyQt5.QtCore import QStringListModel,QAbstractListModel,QModelIndex,QSize,Qt,QObject,pyqtSignal,QTimer,QEvent

import sys
class Win(QWidget):
    def __init__(self,parent=None):

        super(Win, self).__init__(parent)
        self.message=""
        self.btn1=QPushButton("点击1",self)
        self.btn1.move(20,40)
        self.btn1.clicked.connect(lambda :self.btnFn(1))#点击按钮，执行btnFn方法

        self.btn2 = QPushButton("点击2", self)
        self.btn2.move(140,40)
        self.btn2.clicked.connect(lambda: self.btnFn(2))  # 点击按钮，执行btnFn方法
    def btnFn(self,flag):
        if flag==1:
            print("点击了第一个按钮")
        else:
            print("点击了第二个按钮")


    #上面之前的实例，下面从写按键事件方法
    ###第一种方式
    def keyPressEvent(self, QKeyEvent):#重写按键事件
        if QKeyEvent.key()==Qt.Key_A:#按A建
           self.btn1.click()
        if  QKeyEvent.key()==Qt.Key_Tab:
            print("TABTAB")

    def closeEvent(self, QCloseEvent):#重写关闭窗口事件
        print("重写关闭窗口事件closeEvent")

    def contextMenuEvent(self, even):#重写上下文菜单事件
        menu=QMenu(self)
        oneAction=menu.addAction("One")
        oneAction.triggered.connect(self.one)

        menu.addSeparator()#菜单添加分割线
        twoAction=menu.addAction("Two")
        twoAction.triggered.connect(self.two)

        menu.exec_(even.globalPos())#事件触发在任意位置

    def one(self):
        print("one")
        self.message="Menu option One"
        self.update()
    def two(self):
        print("two")
        self.message="Menu option Two"
        self.update()

    def paintEvent(self, event):#重写绘制事件
        painter=QPainter(self)
        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.drawText(self.rect(),Qt.AlignCenter,self.message)
        QTimer.singleShot(15000,self.clearMessage)#清空数据
        QTimer.singleShot(15000,self.update)#更新当前组件

    def clearMessage(self):
        self.message=""

    def resizeEvent(self, event):#更新窗体大小事件
        self.message="窗口大小调整为：QSize({0},{1})".format(event.size().width(),event.size().height())
        self.update()

    ###第二种方式，一般适用于PyQt没有提供事件处理函数情况，需要自定义事件，例如：
        #Tab按键不会传递给keyPressEvent;
       #第二种方式则是重写event函数，所有针对窗口的事件都会传递给event函数，event会根据事件的类型，讲事件分配给不同函数处理；

    def event(self,event):
        #？？？？？下面捕获不到tab按键的事件，if判断始终未false，不知道为何，待解决；？？？
        if ( event.type() == QEvent.KeyPress and event.key() == Qt.Key_Tab ):
            print("Tab")
            self.message="在event()中捕获Tab按键触发的事件"
            self.update()
            return True
        return QWidget.event(self,event)


if __name__=='__main__':

    app=QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec_())
