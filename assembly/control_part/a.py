import sys
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QDialog, QPushButton, QApplication, QLineEdit, QFormLayout, QGridLayout

from PySide2 import QtWidgets

QtWidgets.QAction
QtWidgets.QTreeWidget
QtWidgets.QDockWidget

['QAbstractButton', 'QAbstractGraphicsShapeItem', 'QAbstractItemDelegate', 'QAbstractItemView', 'QAbstractScrollArea',
 'QAbstractSlider', 'QAbstractSpinBox', 'QAccessibleWidget', 'QAction', 'QActionGroup', 'QApplication', 'QBoxLayout',
 'QButtonGroup', 'QCalendarWidget', 'QCheckBox', 'QColorDialog', 'QColormap', 'QColumnView', 'QComboBox',
 'QCommandLinkButton', 'QCommonStyle', 'QCompleter', 'QDataWidgetMapper', 'QDateEdit', 'QDateTimeEdit',
 'QDesktopWidget', 'QDial', 'QDialog', 'QDialogButtonBox', 'QDirModel', 'QDockWidget', 'QDoubleSpinBox',
 'QErrorMessage', 'QFileDialog', 'QFileIconProvider', 'QFileSystemModel', 'QFocusFrame', 'QFontComboBox', 'QFontDialog',
 'QFormLayout', 'QFrame', 'QGesture', 'QGestureEvent', 'QGestureRecognizer', 'QGraphicsAnchor', 'QGraphicsAnchorLayout',
 'QGraphicsBlurEffect', 'QGraphicsColorizeEffect', 'QGraphicsDropShadowEffect', 'QGraphicsEffect',
 'QGraphicsEllipseItem', 'QGraphicsGridLayout', 'QGraphicsItem', 'QGraphicsItemAnimation', 'QGraphicsItemGroup',
 'QGraphicsLayout', 'QGraphicsLayoutItem', 'QGraphicsLineItem', 'QGraphicsLinearLayout', 'QGraphicsObject',
 'QGraphicsOpacityEffect', 'QGraphicsPathItem', 'QGraphicsPixmapItem', 'QGraphicsPolygonItem', 'QGraphicsProxyWidget',
 'QGraphicsRectItem', 'QGraphicsRotation', 'QGraphicsScale', 'QGraphicsScene', 'QGraphicsSceneContextMenuEvent',
 'QGraphicsSceneDragDropEvent', 'QGraphicsSceneEvent', 'QGraphicsSceneHelpEvent', 'QGraphicsSceneHoverEvent',
 'QGraphicsSceneMouseEvent', 'QGraphicsSceneMoveEvent', 'QGraphicsSceneResizeEvent', 'QGraphicsSceneWheelEvent',
 'QGraphicsSimpleTextItem', 'QGraphicsTextItem', 'QGraphicsTransform', 'QGraphicsView', 'QGraphicsWidget',
 'QGridLayout', 'QGroupBox', 'QHBoxLayout', 'QHeaderView', 'QInputDialog', 'QItemDelegate', 'QItemEditorCreatorBase',
 'QItemEditorFactory', 'QKeyEventTransition', 'QKeySequenceEdit', 'QLCDNumber', 'QLabel', 'QLayout', 'QLayoutItem',
 'QLineEdit', 'QListView', 'QListWidget', 'QListWidgetItem', 'QMainWindow', 'QMdiArea', 'QMdiSubWindow', 'QMenu',
 'QMenuBar', 'QMessageBox', 'QMouseEventTransition', 'QOpenGLWidget', 'QPanGesture', 'QPinchGesture',
 'QPlainTextDocumentLayout', 'QPlainTextEdit', 'QProgressBar', 'QProgressDialog', 'QProxyStyle', 'QPushButton',
 'QRadioButton', 'QRubberBand', 'QScrollArea', 'QScrollBar', 'QScroller', 'QScrollerProperties', 'QShortcut',
 'QSizeGrip', 'QSizePolicy', 'QSlider', 'QSpacerItem', 'QSpinBox', 'QSplashScreen', 'QSplitter', 'QSplitterHandle',
 'QStackedLayout', 'QStackedWidget', 'QStatusBar', 'QStyle', 'QStyleFactory', 'QStyleHintReturn',
 'QStyleHintReturnMask', 'QStyleHintReturnVariant', 'QStyleOption', 'QStyleOptionButton', 'QStyleOptionComboBox',
 'QStyleOptionComplex', 'QStyleOptionDockWidget', 'QStyleOptionFocusRect', 'QStyleOptionFrame',
 'QStyleOptionGraphicsItem', 'QStyleOptionGroupBox', 'QStyleOptionHeader', 'QStyleOptionMenuItem',
 'QStyleOptionProgressBar', 'QStyleOptionRubberBand', 'QStyleOptionSizeGrip', 'QStyleOptionSlider',
 'QStyleOptionSpinBox', 'QStyleOptionTab', 'QStyleOptionTabBarBase', 'QStyleOptionTabWidgetFrame',
 'QStyleOptionTitleBar', 'QStyleOptionToolBar', 'QStyleOptionToolBox', 'QStyleOptionToolButton', 'QStyleOptionViewItem',
 'QStylePainter', 'QStyledItemDelegate', 'QSwipeGesture', 'QSystemTrayIcon', 'QTabBar', 'QTabWidget', 'QTableView',
 'QTableWidget', 'QTableWidgetItem', 'QTableWidgetSelectionRange', 'QTapAndHoldGesture', 'QTapGesture', 'QTextBrowser',
 'QTextEdit', 'QTileRules', 'QTimeEdit', 'QToolBar', 'QToolBox', 'QToolButton', 'QToolTip', 'QTreeView', 'QTreeWidget',
 'QTreeWidgetItem', 'QTreeWidgetItemIterator', 'QUndoCommand', 'QUndoGroup', 'QUndoStack', 'QUndoView', 'QVBoxLayout',
 'QWhatsThis', 'QWidget', 'QWidgetAction', 'QWidgetItem', 'QWizard', 'QWizardPage', '__doc__', '__file__', '__loader__',
 '__name__', '__package__', '__spec__']


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Button demo")
        '''??????????????????'''
        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.lineEdit4 = QLineEdit()
        '''????????????'''
        self.btn1 = QPushButton('Button1')
        self.btn2 = QPushButton('Button2')
        self.btn3 = QPushButton('Button3')
        self.btn4 = QPushButton('Button4')
        '''????????????1??????'''
        self.btn1.setCheckable(True)  # ?????????????????????????????????????????????True???????????????????????????????????????????????????
        self.btn1.toggle()  # ?????????????????????????????????
        self.btn1.clicked.connect(self.btnstate)  # ?????????????????????????????????????????????????????????????????????????????????????????????
        '''????????????2??????'''
        self.btn2.setIcon(QIcon(QPixmap('test.png')))  # ?????????2????????????
        self.btn2.clicked.connect(self.btn2func)  # ????????????????????????????????????
        '''????????????3??????'''
        self.btn3.setEnabled(False)
        self.lineEdit3.setText('button3????????????')
        '''????????????4??????'''
        self.btn4.setDefault(True)  # ???????????????????????????
        self.btn4.clicked.connect(self.btn4func)  # ????????????????????????????????????
        '''??????????????????'''
        self.formlayout1 = QFormLayout()
        self.formlayout2 = QFormLayout()
        self.formlayout3 = QFormLayout()
        self.formlayout4 = QFormLayout()
        '''???button???lineEdit??????????????????'''
        self.formlayout1.addRow(self.btn1, self.lineEdit1)
        self.formlayout2.addRow(self.btn2, self.lineEdit2)
        self.formlayout3.addRow(self.btn3, self.lineEdit3)
        self.formlayout4.addRow(self.btn4, self.lineEdit4)
        '''?????????gridlayout???????????????'''
        self.gridlayout = QGridLayout()
        self.gridlayout.addItem(self.formlayout1, 0, 0)
        self.gridlayout.addItem(self.formlayout2, 1, 0)
        self.gridlayout.addItem(self.formlayout3, 2, 0)
        self.gridlayout.addItem(self.formlayout4, 3, 0)
        '''????????????'''
        self.setLayout(self.gridlayout)

    '''isChecked()???????????????????????????????????????True???False'''

    def btnstate(self):
        if self.btn1.isChecked():
            self.lineEdit1.setText('button1????????????')
        else:
            self.lineEdit1.setText('button1????????????')

    '''??????????????????'''

    def btn4func(self):
        self.lineEdit4.setText("button4?????????")

    def btn2func(self):
        self.lineEdit2.setText("button2?????????")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    btnDemo = Form()
    btnDemo.show()
    sys.exit(app.exec_())
