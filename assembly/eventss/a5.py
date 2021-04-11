# 在表格中，编辑完某单元格之后调用函数
# itemChanged：单元格内容发送改变时，通过 connect 连接到指定函数，也就是需#要执行的函数
self.ui.table_1.itemChanged.connect(self.submit_control_code)

def submit_control_code(self, item):
    i = item.row()
    j = item.column()
    self.append_info("发送" + self.ui.table_1.item(i, j-1).text() + "：" + item.text())
