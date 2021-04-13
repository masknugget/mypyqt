from PyQt5 import QtCore
from PyQt5.QtWidgets import *


class CustomEdit(QLineEdit):
    """
    带下拉框的文本输入框类（文本下拉输入框），输入文字可以搜索内容
    """
    def __init__(self, parent, size=(50, 50, 100, 20), name='edit',
                 drag=False, text_list=True, search=True, qss_file=''):
        """
        初始化控件
        :param parent: 控件显示的父对象
        :param size: 输入框控件尺寸
        :param name: 输入框控件名称
        :param drag: 拖放标识位
        :param text_list: 是否开启下拉框功能标识位
        """
        super(CustomEdit, self).__init__(None, parent)
        # 输入框的尺寸
        self.w = size[2]
        self.h = size[3]
        self.setGeometry(*size)
        # 输入框名称
        self.setObjectName(name)
        # 输入框是否支持拖放
        self.drag_flag = False
        if drag:
            self.setAcceptDrops(True)
            self.setDragEnabled(True)  # 开启可拖放事件
        else:
            self.setAcceptDrops(False)
            self.setDragEnabled(False)  # 关闭可拖放事件

        self.click_flag = False  # 点击状态，为False时显示下拉框
        self.text_list = None  # 下拉框对象
        self.p_text = ""    # placehold text，输入框背景上的灰色文字
        self.qss_file = qss_file  # 下拉框样式文件
        self.org_data = []  # 用来进行搜索的数据list

        # 如果text_list为True，则初始化下拉框
        if text_list:
            # 下拉列表模型为StringListModel
            self.list_model = QtCore.QStringListModel()
            # 初始化下拉列表对象为QListView类型
            self.text_list = QListView(parent)
            # 下拉列表名称，以list_开头
            self.text_list.setObjectName("list_%s" % name)
            # 设置下拉列表初始化尺寸
            self.text_list.setGeometry(size[0], size[1]+size[3], size[2], size[3])
            # 隐藏下拉列表
            self.text_list.hide()
            # 初始化下拉列表数据
            self.text_list.data = []


class MainWindow(QMainWindow):
    """主窗口，继承了QMainWindow类"""
    def __init__(self, name, title):
        """初始化类的成员变量"""
        super(MainWindow, self).__init__()
        self.w = 0
        self.h = 0
        self.init_ui(name, title)  # 初始化UI界面

    def init_ui(self, name, title):
        """初始化UI界面"""
        self.w = 140
        self.h = 100

        self.setObjectName(name)  # 设置主窗口对象的名称
        self.setWindowTitle(title)  # 设置主窗口显示的标题
        self.resize(self.w, self.h)  # 设置主窗口尺寸

        self.custom_edit = CustomEdit(self, size=(10, 10, 120, 24),
                name='custom_edit', search=False)
        self.custom_edit.setPlaceholderText('我是自定义输入框')


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    n = 'CustomUI'
    t = '自定义控件'
    ex = MainWindow(n, t)
    ex.show()
    sys.exit(app.exec_())
