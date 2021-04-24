from PySide2 import QtWidgets, QtCore
from PySide2.QtGui import QPixmap, QTransform
from PySide2.QtWidgets import QGraphicsScene, QGraphicsView


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.speedSlider.valueChanged.connect(self.valuechange)

        scene = QGraphicsScene()
        scene.setSceneRect(0, 0, self.width(), self.height())
        self.pixmap = QPixmap(":/img/img/speed_arrow.png")
        self.arrow = scene.addPixmap(self.pixmap)

        graphicsView = QGraphicsView(scene, self.ui.centralwidget)
        graphicsView.setStyleSheet( "background-image:url(:/img/img/central1.png);\n"
                                    "background-repeat:no-repeat;\n"
                                    "background-position: center;\n"
                                    "\n"
                                    "border:none;")
        self.ui.gridLayout.addWidget(graphicsView)

    def valuechange(self):
        angel = self.ui.speedSlider.value()
        xform = QTransform()
        xform.rotate(angel)
        xformed_pixmap = self.pixmap.transformed(xform, Qt.SmoothTransformation)
        self.arrow.setPixmap(xformed_pixmap)

        #print(self.arrow.sceneBoundingRect())


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-image:url(:/img/img/bgd.png);\n"
"possition:center;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.speedSlider = QtWidgets.QSlider(self.centralwidget)
        self.speedSlider.setMaximum(99)
        self.speedSlider.setOrientation(QtCore.Qt.Horizontal)
        self.speedSlider.setObjectName("speedSlider")
        self.gridLayout.addWidget(self.speedSlider, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))