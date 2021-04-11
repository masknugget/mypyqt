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
 	speak = Signal((str,int),(int,))

someone = Communicate()
someone.speak[str,int].connect(say_word_number)
someone.speak[str,int].emit("hello world",2345)

