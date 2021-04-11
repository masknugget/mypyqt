from PySide2.QtWidgets import QApplication, QMainWindow, QComboBox

app = QApplication([])

MainWindow = QMainWindow()

ComboBox = QComboBox(MainWindow)
ComboBox.addItem("1")
ComboBox.addItem("2")
ComboBox.addItem("3")

MainWindow.show()
app.exec_()




from PySide2.QtWidgets import QApplication, QMainWindow, QComboBox

app = QApplication([])

MainWindow = QMainWindow()

ComboBox = QComboBox(MainWindow)
ComboBox.addItem("1")
ComboBox.addItem("2")
ComboBox.addItem("3")
ComboBox.clear()                        #清空组合框项

MainWindow.show()
app.exec_()




from PySide2.QtWidgets import QApplication, QMainWindow, QComboBox

app = QApplication([])

MainWindow = QMainWindow()

ComboBox = QComboBox(MainWindow)
ComboBox.addItem("1")
ComboBox.addItem("2")
ComboBox.addItem("3")
ComboBox.insertItem(1, "0")             #索引1后插入项

MainWindow.show()
app.exec_()




from PySide2.QtWidgets import QApplication, QMainWindow, QComboBox

app = QApplication([])

MainWindow = QMainWindow()

ComboBox = QComboBox(MainWindow)
ComboBox.addItem("1")
ComboBox.addItem("2")
ComboBox.addItem("3")
ComboBox.setEnabled(False)                  #失能组合框

MainWindow.show()
app.exec_()




from PySide2.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton
from PySide2.QtCore import Slot
from PySide2.QtGui import QIcon

app = QApplication([])

MainWindow = QMainWindow()

PushButton = QPushButton(MainWindow)
PushButton.setText("按钮")
PushButton.move(90, 0)
PushButton.resize(50, 20)

Icon = QIcon(".\png\PNG.png")

ComboBox = QComboBox(MainWindow)
ComboBox.move(0, 0)
ComboBox.resize(80, 20)
ComboBox.addItem(Icon, "Item1")
ComboBox.addItem(Icon, "Item2")
ComboBox.addItem(Icon, "Item3")

@Slot()
def PressButton():
    print(ComboBox.currentIndex(), ComboBox.currentText())

PushButton.clicked.connect(PressButton)

MainWindow.show()
app.exec_()


