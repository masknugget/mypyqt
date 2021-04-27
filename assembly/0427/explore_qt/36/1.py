# pip install pyqtgraph

import pyqtgraph.examples
pyqtgraph.examples.run()

pyqtgraph.setConfigOptions(**opts) # 同时设置多项参数
pyqtgraph.getConfigOption(opt)     # 只设置一项参数

# 指定y坐标轴上的值，线条画笔为红色，坐标点符号为'o'
PlotWidget.plot([1, 2, 3, 4, 5], pen='r', symbol='o')
