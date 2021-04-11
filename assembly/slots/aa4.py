import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QObject, Signal, Slot

app = QApplication(sys.argv)

@Slot(int)
@Slot(str)
def say_some_words(words):
	print(words)

class Communicate(QObject):
	#定义一个信号
 speak_words = Signal(str)
 speak_number = Signal(int)


someone = Communicate()
someone.speak_words.connect(say_some_words)
someone.speak_words.emit("hello world.")

someone.speak_number.connect(say_some_words)
someone.speak_number.emit(1234)

