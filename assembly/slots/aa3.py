import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QObject, Signal, Slot

app = QApplication(sys.argv)
#定义一个接受字符串类型的槽
@Slot(str)
def say_some_words(words):
	print(words)

class Communicate(QObject):
	#定义一个信号
  speak = Signal(str)

someone = Communicate()
someone.speak.connect(say_some_words)  #连接信号和槽
someone.speak.emit("hello world.")       #发送信号
