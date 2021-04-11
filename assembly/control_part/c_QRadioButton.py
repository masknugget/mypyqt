from PySide2.QtWidgets import QApplication, QMainWindow, QRadioButton

app = QApplication([])

MainWindow = QMainWindow()

RadioBUtton1 = QRadioButton(MainWindow)
RadioBUtton1.move(0, 0)
RadioBUtton1.setText("选项1")
RadioBUtton2 = QRadioButton(MainWindow)
RadioBUtton2.move(0, 20)
RadioBUtton2.setText("选项2")
RadioBUtton3 = QRadioButton(MainWindow)
RadioBUtton3.move(0, 40)
RadioBUtton3.setText("选项3")

MainWindow.show()
app.exec_()
