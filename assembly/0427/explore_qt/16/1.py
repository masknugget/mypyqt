'''

以上方法理解如下：

    x()——得到窗口左上角在显示屏屏幕上的x坐标；
    y()——得到窗口左上角在显示屏屏幕上的y坐标；
    pos()——得到窗口左上角在显示屏屏幕上的x和y坐标，类型为QPoint()；
    geometry().x()——的到客户区左上角在显示屏屏幕上的x坐标；
    geometry().y()——的到客户区左上角在显示屏屏幕上的y坐标；
    geometry()——的到客户区左上角在显示屏屏幕上的x和y坐标，以及客户区的宽度和长度，类型为QRect()；
    width()——得到客户区的宽度；
    height()——得到客户区的长度；
    geometry().width()——得到客户区的宽度；
    geometry().height()——得到客户区的长度；
    frameGeometry().width()——得到窗口的宽度；
    frameGeometry().height()——得到窗口的长度；

补充：

    frameGeometry().x()——即x()，得到窗口左上角在显示屏屏幕上的x坐标；frameGeometry().y()——即y()，得到窗口左上角在显示屏屏幕上的y坐标；frameGeometry()——即pos()，得到窗口左上角在显示屏屏幕上的x和y坐标，以及窗口的宽度和长度，类型为QRect()；

    注：通过geometry()和frameGeometry()获取坐标的相关方法需要在窗口调用show()方法之后才能使用，否则获取的将是无用数据。

'''