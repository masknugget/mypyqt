import sys
import logging
from PySide2 import QtGui
from PySide2.QtWidgets import QWidget, QApplication

logging.getLogger().setLevel(logging.DEBUG)


def print_data(mime_data, msg_prefix = ""):
    if mime_data.hasImage():
        msg = repr(mime_data.imageData())
    elif mime_data.hasHtml():
        msg = repr(mime_data.html())
    elif mime_data.hasText():
        msg = repr(mime_data.text())
    elif mime_data.hasUrls():
        msg = repr(mime_data.urls())
    else:
        raise Exception("unexpected mime data")

    logging.info(msg_prefix + msg)


class DropArea(QWidget):
    def __init__(self, *args, **kwargs):
        super(DropArea, self).__init__(*args, **kwargs)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, evt):
#        mime_data = evt.mimeData()
#        print_data(mime_data)

        evt.acceptProposedAction()

    def dragMoveEvent(self, evt):
#        mime_data = evt.mimeData()
#        print_data(mime_data)

        evt.acceptProposedAction()

    def dropEvent(self, evt):
        mime_data = evt.mimeData()
        print_data(mime_data, msg_prefix="drop ")

        evt.acceptProposedAction()

    def dragLeaveEvent(self, evt):
#        mime_data = evt.mimeData()
#        print_data(mime_data)

        evt.accept()

    def main(self):
        self.show()
        self.raise_()


app = QApplication(sys.argv)

win = DropArea()
win.main()

sys.exit(app.exec_())