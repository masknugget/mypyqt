import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QObject, Signal, Slot

app = QApplication(sys.argv)

@Slot(int)
@Slot(str)
def say_something(stuff):
	print(stuff)

@Slot(int)
@Slot(str)
def say_word_number(word,number):
	print(word,number)

class Communicate(QObject):
	#定义一个信号
 	speak = Signal(str,int)


someone = Communicate()
# someone.speak[str].connect(say_something)
# someone.speak[int].connect(say_something)
someone.speak.connect(say_word_number)

# someone.speak[str].emit("hello world.")
# someone.speak[int].emit(1234)
someone.speak.emit("hello world",2345)

