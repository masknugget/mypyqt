import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsWidget, QGraphicsGridLayout, \
                            QGraphicsLinearLayout, QLabel, QLineEdit, QPushButton


class Demo(QGraphicsView):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(220, 110)
        # 1
        self.user_label = QLabel('Username:')
        self.pwd_label = QLabel('Password:')
        self.user_line = QLineEdit()
        self.pwd_line = QLineEdit()
        self.login_btn = QPushButton('Log in')
        self.signin_btn = QPushButton('Sign in')

        # 2
        self.scene = QGraphicsScene()
        self.user_label_proxy = self.scene.addWidget(self.user_label)
        self.pwd_label_proxy = self.scene.addWidget(self.pwd_label)
        self.user_line_proxy = self.scene.addWidget(self.user_line)
        self.pwd_line_proxy = self.scene.addWidget(self.pwd_line)
        self.login_btn_proxy = self.scene.addWidget(self.login_btn)
        self.signin_btn_proxy = self.scene.addWidget(self.signin_btn)
        print(type(self.user_label_proxy))

        # 3
        self.g_layout = QGraphicsGridLayout()
        self.l_h_layout = QGraphicsLinearLayout()
        self.l_v_layout = QGraphicsLinearLayout(Qt.Vertical)
        self.g_layout.addItem(self.user_label_proxy, 0, 0, 1, 1)
        self.g_layout.addItem(self.user_line_proxy, 0, 1, 1, 1)
        self.g_layout.addItem(self.pwd_label_proxy, 1, 0, 1, 1)
        self.g_layout.addItem(self.pwd_line_proxy, 1, 1, 1, 1)
        self.l_h_layout.addItem(self.login_btn_proxy)
        self.l_h_layout.addItem(self.signin_btn_proxy)
        self.l_v_layout.addItem(self.g_layout)
        self.l_v_layout.addItem(self.l_h_layout)

        # 4
        self.widget = QGraphicsWidget()
        self.widget.setLayout(self.l_v_layout)

        # 5
        self.scene.addItem(self.widget)
        self.setScene(self.scene)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())