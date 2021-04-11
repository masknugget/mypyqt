import functools
import threading
from time import sleep
from PySide2.QtCore import QObject, QThread, Signal, Slot
from PySide2.QtWidgets import QApplication

class Main(QObject):
    signal_for_function = Signal()

    def __init__(self):
        print('The main thread is "%s"' % threading.current_thread().name)
        super().__init__()
        self.thread = QThread(self)
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.start()
        self.signal_for_function.connect(self.worker.some_function)

def some_decorator(func):
    print(func.__name__, func.__module__, func.__doc__, func.__dict__)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    print(wrapper.__name__, wrapper.__module__, wrapper.__doc__, wrapper.__dict__)
    return wrapper

class Worker(QObject):
    # @some_decorator
    def some_function(self):
        print('some_function is running on thread "%s"' % threading.current_thread().name)


app = QApplication()
m = Main()
m.signal_for_function.emit()

sleep(0.100)
m.thread.quit()
m.thread.wait()