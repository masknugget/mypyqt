from PySide2.QtWidgets import QApplication, QMainWindow, QTabWidget, QDialog, QPushButton
from PySide2.QtGui import QIcon

app = QApplication()

MainWindow = QMainWindow()
Dialog1 = QDialog()
Dialog1.setStyleSheet("background-color:orange")      #设置对话框背景色
Dialog2 = QDialog()
Dialog3 = QDialog()
Dialog3.setStyleSheet("background-color:blue")        #设置对话框背景色

Icon = QIcon(".\png\Icon.ico")

PushButton1 = QPushButton(Dialog1)
PushButton1.setText("按钮1")
PushButton2 = QPushButton(Dialog2)
PushButton2.setText("按钮2")
PushButton3 = QPushButton(Dialog3)
PushButton3.setText("按钮3")

TableWidget = QTabWidget(MainWindow)
TableWidget.resize(300, 300)
TableWidget.addTab(Dialog1, "Tab1")
TableWidget.addTab(Dialog2, "Tab2")
TableWidget.addTab(Dialog3, "Tab3")

TableWidget.setTabIcon(0, Icon)                       #给索引为0的Table添加Icon
TableWidget.setTabIcon(2, Icon)                       #给索引为2的Table添加Icon

#TableWidget.setEnabled(False)                        #失能整个Table控件
TableWidget.removeTab(1)                              #移除Table页，索引为1

MainWindow.show()
app.exec_()
