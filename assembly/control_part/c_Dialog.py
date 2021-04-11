import sys
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
                               QVBoxLayout, QDialog)


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # 创建文本和按钮控件
        self.edit = QLineEdit("Write name here")
        self.button = QPushButton("Show Greetings")
        # 创建布局并添加控件
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # 设置对话框布局
        self.setLayout(layout)
        # 添加按钮并设置触发事件
        self.button.clicked.connect(self.greetings)

    def greetings(self):
        print("Hello %s" % self.edit.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())

