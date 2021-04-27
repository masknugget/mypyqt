import sys
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.line = QLineEdit()
        self.btn = QPushButton('开始爬取')
        self.btn.clicked.connect(self.start_slot)

        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        h_layout.addWidget(QLabel('网址：'))
        h_layout.addWidget(self.line)
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.btn)
        self.setLayout(v_layout)

        self.crawl_thread = CrawlThread(self)  # 1

    def start_slot(self):  # 2
        self.crawl_thread.start()


class CrawlThread(QThread):
    def __init__(self, demo):  # 3
        super(CrawlThread, self).__init__()
        self.demo = demo

    def run(self):  # 4
        url = self.demo.line.text().strip()
        print(f'要爬取的网址为：{url}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())