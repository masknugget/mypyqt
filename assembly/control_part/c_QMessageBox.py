from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox

app = QApplication([])

MainWindow = QMainWindow()

MessageBox = QMessageBox()
MessageBox.critical(MainWindow, "标题", "内容")                 #Critical对话框

MainWindow.show()
app.exec_()


#
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox

app = QApplication([])

MainWindow = QMainWindow()

MessageBox = QMessageBox()
MessageBox.warning(MainWindow, "标题", "内容")                 #Critical对话框

MainWindow.show()
app.exec_()



#
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox

app = QApplication([])

MainWindow = QMainWindow()

MessageBox = QMessageBox()
MessageBox.information(MainWindow, "标题", "内容")                 #Critical对话框

MainWindow.show()
app.exec_()


#
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox

app = QApplication([])

MainWindow = QMainWindow()

MessageBox = QMessageBox()
MessageBox.about(MainWindow, "标题", "内容")                 #Critical对话框

MainWindow.show()
app.exec_()


#
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox

app = QApplication([])

MainWindow = QMainWindow()

MessageBox = QMessageBox()
Ret = MessageBox.question(MainWindow, "标题", "内容")                 #Critical对话框
print(Ret)

MainWindow.show()
app.exec_()

