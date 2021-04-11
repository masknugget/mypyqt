# QTableView 添加右键菜单
from PySide2.QtGui import Qt

def init_context_menu(self):
    """
    初始化右键菜单
    :return:
    """
    # tableView 允许右键菜单
    self.ui.tableView.setContextMenuPolicy(Qt.ActionsContextMenu)

    # 具体菜单项
    send_option = QAction(self.ui.tableView)
    send_option.setText("发送控制代码")
    send_option.triggered.connect(self.show_modify_dialog) # 点击菜单中的“发送控制代码”执行的函数

    # tableView 添加具体的右键菜单
    self.ui.tableView.addAction(send_option)
