from PySide2.QtWidgets import QApplication, QMainWindow, QTabWidget, QDialog, QPushButton

app = QApplication()

MainWindow = QMainWindow()
Dialog1 = QDialog()
Dialog2 = QDialog()
Dialog3 = QDialog()

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

MainWindow.show()
app.exec_()
