# -*- coding: utf-8 -*-

'''
    【简介】
	PyQT5将窗口放在屏幕中间例子
    
'''

from PyQt5.QtWidgets import QDesktopWidget, QApplication ,QMainWindow
import sys  
    
class Winform( QMainWindow): 
    
    def __init__(self, parent=None):
        super( Winform, self).__init__(parent)
          
        self.setWindowTitle('主窗口放在屏幕中间例子')  
        self.resize(370,  250)  
        self.center()  
          
    def center(self):  
        # 计算屏幕的大小
        screen = QDesktopWidget().screenGeometry()  

        # 获取窗口的大小
        size = self.geometry()

        # 移动到屏幕的中央，         
        self.move((screen.width() - size.width()) / 2,  (screen.height() - size.height()) / 2)  
  
if __name__ == "__main__": 
    app = QApplication(sys.argv)   
    win = Winform()  
    win.show()  
    sys.exit(app.exec_())  
