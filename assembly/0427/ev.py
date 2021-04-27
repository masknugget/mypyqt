#事件机制
from PyQt5.QtWidgets import  QDialog,QComboBox,QTableView,QAbstractItemView,QHeaderView,QTableWidget, QTableWidgetItem, QMessageBox,QListWidget,QListWidgetItem, QStatusBar,  QMenuBar,QMenu,QAction,QLineEdit,QStyle,QFormLayout,   QVBoxLayout,QWidget,QApplication ,QHBoxLayout, QPushButton,QMainWindow,QGridLayout,QLabel
from PyQt5.QtGui import QIcon,QPixmap,QStandardItem,QStandardItemModel,QCursor,QFont,QBrush,QColor,QPainter,QMouseEvent,QImage,QTransform
from PyQt5.QtCore import QStringListModel,QAbstractListModel,QModelIndex,QSize,Qt,QObject,pyqtSignal,QTimer,QEvent

import sys
class Win(QWidget):
    def __init__(self,parent=None):
        super(Win, self).__init__(parent)
        self.resize(400,400)

        self.btn=QPushButton("按钮",self)
        self.btn.move(50,50)
        self.btn.setMinimumWidth(220)

        self.image=QImage("./image/7.ico")
        self.label=QLabel('图片',self)
        self.label.setMinimumWidth(600 )
        self.label.setMinimumHeight(400)
        self.label.move(100,150)
        self.label.setPixmap(QPixmap(self.image))

        #对按钮添加事件过滤器
        self.btn.installEventFilter(self)

    def  eventFilter(self,obj, event):
         if obj==self.btn:
             if event.type()==QEvent.MouseButtonPress:
                mouseEvent=QMouseEvent(event)
                if mouseEvent.buttons()==Qt.LeftButton:
                   self.btn.setText("按鼠标左键缩小图片")
                   transform=QTransform()
                   transform.scale(0.5,0.5)#设置缩放多少倍
                   self.label.setPixmap(QPixmap.fromImage(self.image.transformed(transform)))#将label中图片设置缩放效果
                if mouseEvent.buttons()==Qt.RightButton:
                    self.btn.setText("按鼠标右键放大图片")
                    transform = QTransform()
                    transform.scale(1.5, 1.5)#设置缩放多少倍
                    self.label.setPixmap(QPixmap.fromImage(self.image.transformed(transform)))
         return QWidget.eventFilter(self,obj,event)

if __name__=='__main__':

    app=QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec_())