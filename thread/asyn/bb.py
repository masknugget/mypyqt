import sys
import quamash
import asyncio
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


@asyncio.coroutine
def op():
    print('op()')


@asyncio.coroutine
def slow_operation():
    print('clicked')
    yield from op()
    print('op done')
    yield from asyncio.sleep(0.1)
    print('timeout expired')
    yield from asyncio.sleep(2)
    print('second timeout expired')

    loop.stop()


def coroCallHelper(coro):
    asyncio.ensure_future(coro(), loop=loop)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        def btnCallback(obj):
            # ~ loop.call_soon(coroCallHelper, slow_operation)
            asyncio.ensure_future(slow_operation(), loop=loop)
            print('btnCallback returns...')

        btn = QPushButton('Button', self)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        btn.clicked.connect(btnCallback)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Async')
        self.show()


app = QApplication(sys.argv)
loop = quamash.QEventLoop(app)
asyncio.set_event_loop(loop)  # NEW must set the event loop

with loop:
    w = Example()
    w.show()
    loop.run_forever()
print('Coroutine has ended')
