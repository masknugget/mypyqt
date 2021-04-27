import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, \
                            QComboBox, QStackedWidget, QGroupBox, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button1 = QPushButton('button1', self)        # 1
        self.button2 = QPushButton('button2', self)
        self.button2.setProperty('name', 'btn')

        self.lineedit1 = QLineEdit(self)                   # 2
        self.lineedit1.setPlaceholderText('direct')
        self.lineedit2 = SubLineEdit()

        my_list = ['A', 'B', 'C', 'D']                     # 3
        self.combo = QComboBox(self)
        self.combo.addItems(my_list)
        self.combo.setObjectName('cb')

        self.gb = QGroupBox()                              # 4
        self.label1 = QLabel('label1')
        self.label2 = QLabel('label2')
        self.stack = QStackedWidget()
        self.stack.addWidget(self.label2)

        self.gb_layout = QVBoxLayout()
        self.gb_layout.addWidget(self.label1)
        self.gb_layout.addWidget(self.stack)
        self.gb.setLayout(self.gb_layout)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.button1)
        self.v_layout.addWidget(self.button2)
        self.v_layout.addWidget(self.lineedit1)
        self.v_layout.addWidget(self.lineedit2)
        self.v_layout.addWidget(self.combo)
        self.v_layout.addWidget(self.gb)
        self.setLayout(self.v_layout)


class SubLineEdit(QLineEdit):
    def __init__(self):
        super(SubLineEdit, self).__init__()
        self.setPlaceholderText('indirect')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    qss = '''
          * {color: red}
          QPushButton {background-color: blue}
          QPushButton[name='btn'] {background-color: green}
          .QLineEdit {font: bold 20px}
          QComboBox#cb {color: blue}
          QGroupBox QLabel {color: blue}  
          QGroupBox > QLabel {font: 30px}
          '''
    demo.setStyleSheet(qss)
    demo.show()
    sys.exit(app.exec_())