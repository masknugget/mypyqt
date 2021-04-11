import sys
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QDialog, QPushButton, QApplication, QLineEdit, QFormLayout, QGridLayout


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Button demo")
        '''添加行编辑器'''
        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.lineEdit4 = QLineEdit()
        '''添加按钮'''
        self.btn1 = QPushButton('Button1')
        self.btn2 = QPushButton('Button2')
        self.btn3 = QPushButton('Button3')
        self.btn4 = QPushButton('Button4')
        '''添加按钮1事件'''
        self.btn1.setCheckable(True)  # 设置按钮是否已经被选中，如果为True，则表示按钮将保持已点击和释放状态
        self.btn1.toggle()  # 在按钮状态之间进行切换
        self.btn1.clicked.connect(self.btnstate)  # 点击信号与槽函数进行连接，实现输入按钮的当前状态，按下还是释放
        '''添加按钮2事件'''
        self.btn2.setIcon(QIcon(QPixmap('test.png')))  # 为按钮2添加图标
        self.btn2.clicked.connect(self.btn2func)  # 点击信号与槽函数进行连接
        '''添加按钮3事件'''
        self.btn3.setEnabled(False)
        self.lineEdit3.setText('button3被禁用了')
        '''添加按钮4事件'''
        self.btn4.setDefault(True)  # 设置按钮的默认状态
        self.btn4.clicked.connect(self.btn4func)  # 点击信号与槽函数进行连接
        '''添加表单布局'''
        self.formlayout1 = QFormLayout()
        self.formlayout2 = QFormLayout()
        self.formlayout3 = QFormLayout()
        self.formlayout4 = QFormLayout()
        '''将button和lineEdit一一对应起来'''
        self.formlayout1.addRow(self.btn1, self.lineEdit1)
        self.formlayout2.addRow(self.btn2, self.lineEdit2)
        self.formlayout3.addRow(self.btn3, self.lineEdit3)
        self.formlayout4.addRow(self.btn4, self.lineEdit4)
        '''每一个gridlayout之间的布局'''
        self.gridlayout = QGridLayout()
        self.gridlayout.addItem(self.formlayout1, 0, 0)
        self.gridlayout.addItem(self.formlayout2, 1, 0)
        self.gridlayout.addItem(self.formlayout3, 2, 0)
        self.gridlayout.addItem(self.formlayout4, 3, 0)
        '''添加布局'''
        self.setLayout(self.gridlayout)

    '''isChecked()：判断按钮的状态，返回值为True或False'''

    def btnstate(self):
        if self.btn1.isChecked():
            self.lineEdit1.setText('button1被按下了')
        else:
            self.lineEdit1.setText('button1被释放了')

    '''定义链接函数'''

    def btn4func(self):
        self.lineEdit4.setText("button4被点击")

    def btn2func(self):
        self.lineEdit2.setText("button2被点击")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    btnDemo = Form()
    btnDemo.show()
    sys.exit(app.exec_())