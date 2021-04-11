from PySide2 import QtWidgets
import sys

class LayoutApp(QtWidgets.QMainWindow):
    '''
    网格布局 Demo
    '''
    def __init__(self):
        super().__init__()

        main_widget = QtWidgets.QWidget() 			# 实例化一个widget控件
        main_layout = QtWidgets.QGridLayout() 		# 实例化一个垂直布局层
        main_widget.setLayout(main_layout) 			# 设置widget控件布局为水平布局
        # 实例化3个按钮
        button_1 = QtWidgets.QPushButton('按钮一')
        button_2 = QtWidgets.QPushButton('按钮二')
        button_3 = QtWidgets.QPushButton('按钮三')
        # 将按钮添加到水平布局中
        main_layout.addWidget(button_1,1,1,1,2) 	# 添加到第1行第1列，占1行占2列
        main_layout.addWidget(button_2,2,1,1,1) 	# 添加到第2行第1列，占1行占1列
        main_layout.addWidget(button_3,3,2,1,1) 	# 添加到第3行第2列，占1行占1列

        self.setCentralWidget(main_widget) 			# 设置窗口的中央部件

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = LayoutApp()
    gui.show()
    sys.exit(app.exec_())
