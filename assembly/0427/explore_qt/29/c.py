import sys
from PyQt5.QtCore import Qt, QTranslator, QEvent
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QComboBox, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('Start', self)
        self.label = QLabel('Hello, World', self)
        self.label.setAlignment(Qt.AlignCenter)

        self.combo = QComboBox(self)
        self.combo.addItem('English')
        self.combo.addItem('中文')
        self.combo.addItem('français')
        self.combo.currentTextChanged.connect(self.change_func)

        self.trans = QTranslator(self)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.combo)
        self.v_layout.addWidget(self.button)
        self.v_layout.addWidget(self.label)
        self.setLayout(self.v_layout)

    def change_func(self):
        print(self.combo.currentText())
        if self.combo.currentText() == '中文':
            self.trans.load('eng-chs')
            _app = QApplication.instance()
            _app.installTranslator(self.trans)

        elif self.combo.currentText() == 'français':
            self.trans.load('eng-fr')
            _app = QApplication.instance()
            _app.installTranslator(self.trans)

        else:
            _app = QApplication.instance()
            _app.removeTranslator(self.trans)

    def retranslateUi(self):        # 1
        self.button.setText(QApplication.translate('Demo', 'Start'))
        self.label.setText(QApplication.translate('Demo', 'Hello, World'))

    def changeEvent(self, event):   # 2
        if event.type() == QEvent.LanguageChange:
            self.retranslateUi()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())