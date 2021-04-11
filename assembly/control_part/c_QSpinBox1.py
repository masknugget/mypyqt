from PySide2.QtWidgets import QApplication, QMainWindow, QSpinBox, QPushButton
from PySide2.QtCore import Slot

app = QApplication([])

MainWindow = QMainWindow()

GetValueButton = QPushButton(MainWindow)
GetValueButton.setText("读取")
GetValueButton.resize(50, 20)
GetValueButton.move(120, 0)

SetValueButton = QPushButton(MainWindow)
SetValueButton.setText("50")
SetValueButton.resize(50, 20)
SetValueButton.move(120, 20)

EnableButton = QPushButton(MainWindow)
EnableButton.setText("Enable")
EnableButton.resize(50, 20)
EnableButton.move(120, 40)

SpinBox = QSpinBox(MainWindow)
SpinBox.resize(100, 20)
SpinBox.value()
SpinBox.setRange(0, 100)                        #设置数值范围

@Slot()
def GetValue():
    print(SpinBox.value())

@Slot()
def SetValue():
    SpinBox.setValue(50)

bEnable = False
@Slot()
def CtrlEnable():
    global bEnable                              #声明全局变量

    SpinBox.setEnabled(bEnable)
    if bEnable == False:
        bEnable = True
    else:
        bEnable = False

GetValueButton.clicked.connect(GetValue)
SetValueButton.clicked.connect(SetValue)
EnableButton.clicked.connect(CtrlEnable)

MainWindow.show()
app.exec_()
