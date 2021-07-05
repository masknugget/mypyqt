# 自定义控件--实现了一个带全选功能的复选框
import sys
from PyQt5.QtWidgets import QApplication, QListWidget, QCheckBox, QListWidgetItem
from PyQt5.QtCore import Qt


class FilteredList(QListWidget):
    # 继承自列表控件
    def __init__(self, textList, parent=None):
        super().__init__(parent)
        self.selectAll_ch = QCheckBox("全选(selectAll)")
        self.selectAll_ch.setCheckState(Qt.Checked)
        self.selectAll_ch.stateChanged[int].connect(self.on_selectAll)  #
        item = QListWidgetItem(self)
        self.setItemWidget(item, self.selectAll_ch)  # 列表控件的项设为 QCheckBox
        self.dict = dict()
        self.boxes = set()
        for index, text in enumerate(textList):
            ch = QCheckBox(text)
            ch.setCheckState(Qt.Unchecked)
            ch.stateChanged[int].connect(self.on_stateChanged)
            # item.setCheckState(Qt.Unchecked)#
            item = QListWidgetItem(self)
            self.setItemWidget(item, ch)
            self.boxes.add(ch)
            self.dict[index] = ch

    def on_selectAll(self, state):
        if state == 2:
            for ch in self.boxes:
                ch.setCheckState(2)
        if state == 0:
            for ch in self.boxes:
                ch.setCheckState(0)

    def on_stateChanged(self, state):
        ch = self.sender()
        if state:
            if len([ch for ch in self.boxes if ch.checkState()]) == self.count() - 1:
                # 0 不选中， 1 部分选中，2 全选中 #Qt.Unchecked #Qt.PartiallyChecked #Qt.Checked
                self.selectAll_ch.setCheckState(2)
            else:
                self.selectAll_ch.setCheckState(1)
        else:
            if len([k for k in self.boxes if k.checkState()]):
                self.selectAll_ch.setCheckState(1)
            else:
                self.selectAll_ch.setCheckState(0)

    def keyPressEvent(self, event):
        # Ctrl+A 全选
        if event.modifiers() & Qt.ControlModifier and event.key() == Qt.Key_A:
            self.selectAll_ch.setCheckState(2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myList = FilteredList(textList=["a", "b", "c", "d"])
    myList.show()
    sys.exit(app.exec_())