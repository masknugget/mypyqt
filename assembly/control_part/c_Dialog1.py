# PySide2 去掉 Dialog 的问号
import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QInputDialog, QApplication


class ModifyDialog(QInputDialog):

    def __init__(self, *args, **kwargs):
        super().__init__()

        self.setWindowTitle("Title")
        self.setLabelText("label")

        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)


if __name__ == '__main__':
    app = QApplication([])  # 初始化应用
    dial = ModifyDialog(app)

    dial.show()

    sys.exit(app.exec_())
