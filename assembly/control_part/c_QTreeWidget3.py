# 对每个项进行编号，之所以不连续是为了以后预留
class AllCertCaseValue:
    ROOT_PROTOCON = 0
    # STA 协议一致性所有case
    ROOT_PROTOCON_STA_CHILD = 1
    # sta scan tmi band0/1/2/3
    ROOT_PROTOCON_STA_TMISCAN_B0 = 2
    ROOT_PROTOCON_STA_TMISCAN_B1 = 3
    ROOT_PROTOCON_STA_TMISCAN_B2 = 4
    ROOT_PROTOCON_STA_TMISCAN_B3 = 5
    # sta tonemask band0/1/2/3
    ROOT_PROTOCON_STA_TM_B0 = 6
    ROOT_PROTOCON_STA_TM_B1 = 7
    ROOT_PROTOCON_STA_TM_B2 = 8
    ROOT_PROTOCON_STA_TM_B3 = 9

    ROOT_PROTOCON_STA_MAX = ROOT_PROTOCON_STA_TM_B3 + 1

    # CCO 协议一致性所有case
    ROOT_PROTOCON_CCO_CHILD = 40
    # cco scan tmi band0/1/2/3
    ROOT_PROTOCON_CCO_TMISCAN_B0 = 41
    ROOT_PROTOCON_CCO_TMISCAN_B1 = 42
    ROOT_PROTOCON_CCO_TMISCAN_B2 = 43
    ROOT_PROTOCON_CCO_TMISCAN_B3 = 44
    # sta tonemask band0/1/2/3
    ROOT_PROTOCON_CCO_TM_B0 = 45
    ROOT_PROTOCON_CCO_TM_B1 = 46
    ROOT_PROTOCON_CCO_TM_B2 = 47
    ROOT_PROTOCON_CCO_TM_B3 = 48

    ROOT_PROTOCON_CCO_MAX = ROOT_PROTOCON_CCO_TM_B3 + 1

    # 通信性能测试
    ROOT_PERFORMANCE_CHILD = 80
    ROOT_PERFORMANCE_STA_CHILD = 81

    # white noise
    ROOT_PERFORMANCE_STA_WN_B1 = 82
    ROOT_PERFORMANCE_STA_WN_B2 = 83
    # anti-ppm
    ROOT_PERFORMANCE_STA_ANTIPPM_B1 = 84
    ROOT_PERFORMANCE_STA_ANTIPPM_B2 = 85
    # anti-attenuation
    ROOT_PERFORMANCE_STA_ANTIATT_B1 = 86
    ROOT_PERFORMANCE_STA_ANTIATT_B2 = 87
    # anti-narrowband
    ROOT_PERFORMANCE_STA_ANTINARROW_B1 = 88
    ROOT_PERFORMANCE_STA_ANTINARROW_B2 = 89
    # anti-pulse
    ROOT_PERFORMANCE_STA_ANTIPULSE_B1 = 90
    ROOT_PERFORMANCE_STA_ANTIPULSE_B2 = 91
    # psd
    ROOT_PERFORMANCE_STA_PSD_B1 = 92
    ROOT_PERFORMANCE_STA_PSD_B2 = 93
    # sta rate
    ROOT_PERFORMANCE_STA_RATE_B1 = 94
    ROOT_PERFORMANCE_STA_RATE_B2 = 95

    ROOT_PERFORMANCE_STA_MAX = ROOT_PERFORMANCE_STA_RATE_B2 + 1

    ROOT_PERFORMANCE_CCO_CHILD = 100
    # white noise
    ROOT_PERFORMANCE_CCO_WN_B1 = 101
    ROOT_PERFORMANCE_CCO_WN_B2 = 102
    # anti-ppm
    ROOT_PERFORMANCE_CCO_ANTIPPM_B1 = 103
    ROOT_PERFORMANCE_CCO_ANTIPPM_B2 = 104
    # anti-attenuation
    ROOT_PERFORMANCE_CCO_ANTIATT_B1 = 105
    ROOT_PERFORMANCE_CCO_ANTIATT_B2 = 106
    # anti-narrowband
    ROOT_PERFORMANCE_CCO_ANTINARROW_B1 = 107
    ROOT_PERFORMANCE_CCO_ANTINARROW_B2 = 108
    # anti-pulse
    ROOT_PERFORMANCE_CCO_ANTIPULSE_B1 = 109
    ROOT_PERFORMANCE_CCO_ANTIPULSE_B2 = 110
    # psd
    ROOT_PERFORMANCE_CCO_PSD_B1 = 111
    ROOT_PERFORMANCE_CCO_PSD_B2 = 112
    # CCO rate
    ROOT_PERFORMANCE_CCO_RATE_B1 = 113
    ROOT_PERFORMANCE_CCO_RATE_B2 = 114
    ROOT_PERFORMANCE_CCO_MAX = ROOT_PERFORMANCE_CCO_RATE_B2 + 1

    ROOT_OTHER_CHILD = 130
    ROOT_OTHER_RATE = 131
    ROOT_OTHER_MAX = ROOT_OTHER_RATE + 1

    # max
    TREE_MAX = ROOT_OTHER_MAX + 1


# 将编号和项目联系起来
DictCommandInfo = {
    "协议一致性": AllCertCaseValue.ROOT_PROTOCON,
    # STA test case
    "STA测试项": AllCertCaseValue.ROOT_PROTOCON_STA_CHILD,
    "TMI遍历 STA band0": AllCertCaseValue.ROOT_PROTOCON_STA_TMISCAN_B0,
    "TMI遍历 STA band1": AllCertCaseValue.ROOT_PROTOCON_STA_TMISCAN_B1,
    "TMI遍历 STA band2": AllCertCaseValue.ROOT_PROTOCON_STA_TMISCAN_B2,
    "TMI遍历 STA band3": AllCertCaseValue.ROOT_PROTOCON_STA_TMISCAN_B3,
    "ToneMask测试 STA band0": AllCertCaseValue.ROOT_PROTOCON_STA_TM_B0,
    "ToneMask测试 STA band1": AllCertCaseValue.ROOT_PROTOCON_STA_TM_B1,
    "ToneMask测试 STA band2": AllCertCaseValue.ROOT_PROTOCON_STA_TM_B2,
    "ToneMask测试 STA band3": AllCertCaseValue.ROOT_PROTOCON_STA_TM_B3,

    # CCO test case
    "CCO测试项": AllCertCaseValue.ROOT_PROTOCON_CCO_CHILD,
    "TMI遍历 CCO band0": AllCertCaseValue.ROOT_PROTOCON_CCO_TMISCAN_B0,
    "TMI遍历 CCO band1": AllCertCaseValue.ROOT_PROTOCON_CCO_TMISCAN_B1,
    "TMI遍历 CCO band2": AllCertCaseValue.ROOT_PROTOCON_CCO_TMISCAN_B2,
    "TMI遍历 CCO band3": AllCertCaseValue.ROOT_PROTOCON_CCO_TMISCAN_B3,
    "ToneMask测试 CCO band0": AllCertCaseValue.ROOT_PROTOCON_CCO_TM_B0,
    "ToneMask测试 CCO band1": AllCertCaseValue.ROOT_PROTOCON_CCO_TM_B1,
    "ToneMask测试 CCO band2": AllCertCaseValue.ROOT_PROTOCON_CCO_TM_B2,
    "ToneMask测试 CCO band3": AllCertCaseValue.ROOT_PROTOCON_CCO_TM_B3,

    # communication performance
    "通信性能测试": AllCertCaseValue.ROOT_PERFORMANCE_CHILD,
    "STA性能测试项": AllCertCaseValue.ROOT_PERFORMANCE_STA_CHILD,
    "白噪性能 STA band1": AllCertCaseValue.ROOT_PERFORMANCE_STA_WN_B1,
    "白噪性能 STA band2": AllCertCaseValue.ROOT_PERFORMANCE_STA_WN_B2,
    "抗频偏性能 STA band1": AllCertCaseValue.ROOT_PERFORMANCE_STA_ANTIPPM_B1,
    "抗频偏性能 STA band2": AllCertCaseValue.ROOT_PERFORMANCE_STA_ANTIPPM_B2,
    "抗衰减性能 STA band1": AllCertCaseValue.ROOT_PERFORMANCE_STA_ANTIATT_B1,
    "抗衰减性能 STA band2": AllCertCaseValue.ROOT_PERFORMANCE_STA_ANTIATT_B2,
    "抗窄带性能 STA band1": AllCertCaseValue.ROOT_PERFORMANCE_STA_ANTINARROW_B1,
    "抗窄带性能 STA band2": AllCertCaseValue.ROOT_PERFORMANCE_STA_ANTINARROW_B2,
    "抗脉冲性能 STA band1": AllCertCaseValue.ROOT_PERFORMANCE_STA_ANTIPULSE_B1,
    "抗脉冲性能 STA band2": AllCertCaseValue.ROOT_PERFORMANCE_STA_ANTIPULSE_B2,
    "功率频谱密度 STA band1": AllCertCaseValue.ROOT_PERFORMANCE_STA_PSD_B1,
    "功率频谱密度 STA band2": AllCertCaseValue.ROOT_PERFORMANCE_STA_PSD_B2,
    "STA 速率测试 band1": AllCertCaseValue.ROOT_PERFORMANCE_STA_RATE_B1,
    "STA 速率测试 band2": AllCertCaseValue.ROOT_PERFORMANCE_STA_RATE_B2,
    "CCO性能测试项": AllCertCaseValue.ROOT_PERFORMANCE_CCO_CHILD,
    "白噪性能 CCO band1": AllCertCaseValue.ROOT_PERFORMANCE_CCO_WN_B1,
    "白噪性能 CCO band2": AllCertCaseValue.ROOT_PERFORMANCE_CCO_WN_B2,
    "抗频偏性能 CCO band1": AllCertCaseValue.ROOT_PERFORMANCE_CCO_ANTIPPM_B1,
    "抗频偏性能 CCO band2": AllCertCaseValue.ROOT_PERFORMANCE_CCO_ANTIPPM_B2,
    "抗衰减性能 CCO band1": AllCertCaseValue.ROOT_PERFORMANCE_CCO_ANTIATT_B1,
    "抗衰减性能 CCO band2": AllCertCaseValue.ROOT_PERFORMANCE_CCO_ANTIATT_B2,
    "抗窄带性能 CCO band1": AllCertCaseValue.ROOT_PERFORMANCE_CCO_ANTINARROW_B1,
    "抗窄带性能 CCO band2": AllCertCaseValue.ROOT_PERFORMANCE_CCO_ANTINARROW_B2,
    "抗脉冲性能 CCO band1": AllCertCaseValue.ROOT_PERFORMANCE_CCO_ANTIPULSE_B1,
    "抗脉冲性能 CCO band2": AllCertCaseValue.ROOT_PERFORMANCE_CCO_ANTIPULSE_B2,
    "功率频谱密度 CCO band1": AllCertCaseValue.ROOT_PERFORMANCE_CCO_PSD_B1,
    "功率频谱密度 CCO band2": AllCertCaseValue.ROOT_PERFORMANCE_CCO_PSD_B2,
    "CCO 速率测试 band1": AllCertCaseValue.ROOT_PERFORMANCE_CCO_RATE_B1,
    "CCO 速率测试 band2": AllCertCaseValue.ROOT_PERFORMANCE_CCO_RATE_B2,

    # other test case
    "OTHER_TEST": AllCertCaseValue.ROOT_OTHER_CHILD,
    "RATE TEST": AllCertCaseValue.ROOT_OTHER_RATE,
}

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'treewidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(618, 594)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.verticalLayout.addWidget(self.treeWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 618, 23))
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


import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class AllCertCaseValue:
    ROOT_PROTOCON = 0
    # STA 协议一致性所有case
    ROOT_PROTOCON_STA_CHILD = 1
    # sta scan tmi band0/1/2/3
    ROOT_PROTOCON_STA_TMISCAN_B0 = 2
    ROOT_PROTOCON_STA_TMISCAN_B1 = 3
    ROOT_PROTOCON_STA_TMISCAN_B2 = 4
    ROOT_PROTOCON_STA_TMISCAN_B3 = 5
    # sta tonemask band0/1/2/3
    ROOT_PROTOCON_STA_TM_B0 = 6
    ROOT_PROTOCON_STA_TM_B1 = 7
    ROOT_PROTOCON_STA_TM_B2 = 8
    ROOT_PROTOCON_STA_TM_B3 = 9

    ROOT_PROTOCON_STA_MAX = ROOT_PROTOCON_STA_TM_B3 + 1

    # CCO 协议一致性所有case
    ROOT_PROTOCON_CCO_CHILD = 40
    # cco scan tmi band0/1/2/3
    ROOT_PROTOCON_CCO_TMISCAN_B0 = 41
    ROOT_PROTOCON_CCO_TMISCAN_B1 = 42
    ROOT_PROTOCON_CCO_TMISCAN_B2 = 43
    ROOT_PROTOCON_CCO_TMISCAN_B3 = 44
    # sta tonemask band0/1/2/3
    ROOT_PROTOCON_CCO_TM_B0 = 45
    ROOT_PROTOCON_CCO_TM_B1 = 46
    ROOT_PROTOCON_CCO_TM_B2 = 47
    ROOT_PROTOCON_CCO_TM_B3 = 48

    ROOT_PROTOCON_CCO_MAX = ROOT_PROTOCON_CCO_TM_B3 + 1

    # 通信性能测试
    ROOT_PERFORMANCE_CHILD = 80
    ROOT_PERFORMANCE_STA_CHILD = 81

    # white noise
    ROOT_PERFORMANCE_STA_WN_B1 = 82
    ROOT_PERFORMANCE_STA_WN_B2 = 83
    # anti-ppm
    ROOT_PERFORMANCE_STA_ANTIPPM_B1 = 84
    ROOT_PERFORMANCE_STA_ANTIPPM_B2 = 85
    # anti-attenuation
    ROOT_PERFORMANCE_STA_ANTIATT_B1 = 86
    ROOT_PERFORMANCE_STA_ANTIATT_B2 = 87
    # anti-narrowband
    ROOT_PERFORMANCE_STA_ANTINARROW_B1 = 88
    ROOT_PERFORMANCE_STA_ANTINARROW_B2 = 89
    # anti-pulse
    ROOT_PERFORMANCE_STA_ANTIPULSE_B1 = 90
    ROOT_PERFORMANCE_STA_ANTIPULSE_B2 = 91
    # psd
    ROOT_PERFORMANCE_STA_PSD_B1 = 92
    ROOT_PERFORMANCE_STA_PSD_B2 = 93
    # sta rate
    ROOT_PERFORMANCE_STA_RATE_B1 = 94
    ROOT_PERFORMANCE_STA_RATE_B2 = 95

    ROOT_PERFORMANCE_STA_MAX = ROOT_PERFORMANCE_STA_RATE_B2 + 1

    ROOT_PERFORMANCE_CCO_CHILD = 100
    # white noise
    ROOT_PERFORMANCE_CCO_WN_B1 = 101
    ROOT_PERFORMANCE_CCO_WN_B2 = 102
    # anti-ppm
    ROOT_PERFORMANCE_CCO_ANTIPPM_B1 = 103
    ROOT_PERFORMANCE_CCO_ANTIPPM_B2 = 104
    # anti-attenuation
    ROOT_PERFORMANCE_CCO_ANTIATT_B1 = 105
    ROOT_PERFORMANCE_CCO_ANTIATT_B2 = 106
    # anti-narrowband
    ROOT_PERFORMANCE_CCO_ANTINARROW_B1 = 107
    ROOT_PERFORMANCE_CCO_ANTINARROW_B2 = 108
    # anti-pulse
    ROOT_PERFORMANCE_CCO_ANTIPULSE_B1 = 109
    ROOT_PERFORMANCE_CCO_ANTIPULSE_B2 = 110
    # psd
    ROOT_PERFORMANCE_CCO_PSD_B1 = 111
    ROOT_PERFORMANCE_CCO_PSD_B2 = 112
    # CCO rate
    ROOT_PERFORMANCE_CCO_RATE_B1 = 113
    ROOT_PERFORMANCE_CCO_RATE_B2 = 114
    ROOT_PERFORMANCE_CCO_MAX = ROOT_PERFORMANCE_CCO_RATE_B2 + 1

    ROOT_OTHER_CHILD = 130
    ROOT_OTHER_RATE = 131
    ROOT_OTHER_MAX = ROOT_OTHER_RATE + 1

    # max
    TREE_MAX = ROOT_OTHER_MAX + 1


DictCommandInfo = {
    "协议一致性": AllCertCaseValue.ROOT_PROTOCON,
    # STA test case
    "STA测试项": AllCertCaseValue.ROOT_PROTOCON_STA_CHILD,
    "TMI遍历 STA band0": AllCertCaseValue.ROOT_PROTOCON_STA_TMISCAN_B0,
    "TMI遍历 STA band1": AllCertCaseValue.ROOT_PROTOCON_STA_TMISCAN_B1,
    "TMI遍历 STA band2": AllCertCaseValue.ROOT_PROTOCON_STA_TMISCAN_B2,
    "TMI遍历 STA band3": AllCertCaseValue.ROOT_PROTOCON_STA_TMISCAN_B3,
    "ToneMask测试 STA band0": AllCertCaseValue.ROOT_PROTOCON_STA_TM_B0,
    "ToneMask测试 STA band1": AllCertCaseValue.ROOT_PROTOCON_STA_TM_B1,
    "ToneMask测试 STA band2": AllCertCaseValue.ROOT_PROTOCON_STA_TM_B2,
    "ToneMask测试 STA band3": AllCertCaseValue.ROOT_PROTOCON_STA_TM_B3,

    # CCO test case
    "CCO测试项": AllCertCaseValue.ROOT_PROTOCON_CCO_CHILD,
    "TMI遍历 CCO band0": AllCertCaseValue.ROOT_PROTOCON_CCO_TMISCAN_B0,
    "TMI遍历 CCO band1": AllCertCaseValue.ROOT_PROTOCON_CCO_TMISCAN_B1,
    "TMI遍历 CCO band2": AllCertCaseValue.ROOT_PROTOCON_CCO_TMISCAN_B2,
    "TMI遍历 CCO band3": AllCertCaseValue.ROOT_PROTOCON_CCO_TMISCAN_B3,
    "ToneMask测试 CCO band0": AllCertCaseValue.ROOT_PROTOCON_CCO_TM_B0,
    "ToneMask测试 CCO band1": AllCertCaseValue.ROOT_PROTOCON_CCO_TM_B1,
    "ToneMask测试 CCO band2": AllCertCaseValue.ROOT_PROTOCON_CCO_TM_B2,
    "ToneMask测试 CCO band3": AllCertCaseValue.ROOT_PROTOCON_CCO_TM_B3,

    # communication performance
    "通信性能测试": AllCertCaseValue.ROOT_PERFORMANCE_CHILD,
    "STA性能测试项": AllCertCaseValue.ROOT_PERFORMANCE_STA_CHILD,
    "白噪性能 STA band1": AllCertCaseValue.ROOT_PERFORMANCE_STA_WN_B1,
    "白噪性能 STA band2": AllCertCaseValue.ROOT_PERFORMANCE_STA_WN_B2,
    "抗频偏性能 STA band1": AllCertCaseValue.ROOT_PERFORMANCE_STA_ANTIPPM_B1,
    "抗频偏性能 STA band2": AllCertCaseValue.ROOT_PERFORMANCE_STA_ANTIPPM_B2,
    "抗衰减性能 STA band1": AllCertCaseValue.ROOT_PERFORMANCE_STA_ANTIATT_B1,
    "抗衰减性能 STA band2": AllCertCaseValue.ROOT_PERFORMANCE_STA_ANTIATT_B2,
    "抗窄带性能 STA band1": AllCertCaseValue.ROOT_PERFORMANCE_STA_ANTINARROW_B1,
    "抗窄带性能 STA band2": AllCertCaseValue.ROOT_PERFORMANCE_STA_ANTINARROW_B2,
    "抗脉冲性能 STA band1": AllCertCaseValue.ROOT_PERFORMANCE_STA_ANTIPULSE_B1,
    "抗脉冲性能 STA band2": AllCertCaseValue.ROOT_PERFORMANCE_STA_ANTIPULSE_B2,
    "功率频谱密度 STA band1": AllCertCaseValue.ROOT_PERFORMANCE_STA_PSD_B1,
    "功率频谱密度 STA band2": AllCertCaseValue.ROOT_PERFORMANCE_STA_PSD_B2,
    "STA 速率测试 band1": AllCertCaseValue.ROOT_PERFORMANCE_STA_RATE_B1,
    "STA 速率测试 band2": AllCertCaseValue.ROOT_PERFORMANCE_STA_RATE_B2,
    "CCO性能测试项": AllCertCaseValue.ROOT_PERFORMANCE_CCO_CHILD,
    "白噪性能 CCO band1": AllCertCaseValue.ROOT_PERFORMANCE_CCO_WN_B1,
    "白噪性能 CCO band2": AllCertCaseValue.ROOT_PERFORMANCE_CCO_WN_B2,
    "抗频偏性能 CCO band1": AllCertCaseValue.ROOT_PERFORMANCE_CCO_ANTIPPM_B1,
    "抗频偏性能 CCO band2": AllCertCaseValue.ROOT_PERFORMANCE_CCO_ANTIPPM_B2,
    "抗衰减性能 CCO band1": AllCertCaseValue.ROOT_PERFORMANCE_CCO_ANTIATT_B1,
    "抗衰减性能 CCO band2": AllCertCaseValue.ROOT_PERFORMANCE_CCO_ANTIATT_B2,
    "抗窄带性能 CCO band1": AllCertCaseValue.ROOT_PERFORMANCE_CCO_ANTINARROW_B1,
    "抗窄带性能 CCO band2": AllCertCaseValue.ROOT_PERFORMANCE_CCO_ANTINARROW_B2,
    "抗脉冲性能 CCO band1": AllCertCaseValue.ROOT_PERFORMANCE_CCO_ANTIPULSE_B1,
    "抗脉冲性能 CCO band2": AllCertCaseValue.ROOT_PERFORMANCE_CCO_ANTIPULSE_B2,
    "功率频谱密度 CCO band1": AllCertCaseValue.ROOT_PERFORMANCE_CCO_PSD_B1,
    "功率频谱密度 CCO band2": AllCertCaseValue.ROOT_PERFORMANCE_CCO_PSD_B2,
    "CCO 速率测试 band1": AllCertCaseValue.ROOT_PERFORMANCE_CCO_RATE_B1,
    "CCO 速率测试 band2": AllCertCaseValue.ROOT_PERFORMANCE_CCO_RATE_B2,

    # other test case
    "OTHER_TEST": AllCertCaseValue.ROOT_OTHER_CHILD,
    "RATE TEST": AllCertCaseValue.ROOT_OTHER_RATE,
}


class tree(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(tree, self).__init__()
        self.setupUi(self)
        self.AllTestCase = None
        self.intiui()

    def intiui(self):

        # 设置列数
        self.treeWidget.setColumnCount(1)
        # 设置树形控件头部的标题
        self.treeWidget.setHeaderLabels(['测试用例'])
        self.treeWidget.setColumnWidth(0, 120)
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.expandToDepth(0)

        # 设置根节点
        self.AllTestCase = QTreeWidgetItem(self.treeWidget)
        self.AllTestCase.setText(0, '测试项')
        self.AllTestCase.setCheckState(0, Qt.Unchecked)

        # 通过字典获取所有子项
        for value in DictCommandInfo.keys():
            if DictCommandInfo[value] == AllCertCaseValue.ROOT_PROTOCON:
                # 设置子项
                item_protocon = QTreeWidgetItem(self.AllTestCase)
                item_protocon.setText(0, value)
                item_protocon.setCheckState(0, Qt.Unchecked)
            elif DictCommandInfo[value] == AllCertCaseValue.ROOT_PROTOCON_STA_CHILD:
                item_sta_father = QTreeWidgetItem(item_protocon)
                item_sta_father.setText(0, value)
                item_sta_father.setCheckState(0, Qt.Unchecked)
            elif (AllCertCaseValue.ROOT_PROTOCON_STA_CHILD < DictCommandInfo[value] <
                  AllCertCaseValue.ROOT_PROTOCON_STA_MAX):
                item_sta_child = QTreeWidgetItem(item_sta_father)
                item_sta_child.setText(0, value)
                item_sta_child.setCheckState(0, Qt.Unchecked)
            elif DictCommandInfo[value] == AllCertCaseValue.ROOT_PROTOCON_CCO_CHILD:
                item_cco_father = QTreeWidgetItem(item_protocon)
                item_cco_father.setText(0, value)
                item_cco_father.setCheckState(0, Qt.Unchecked)
            elif (AllCertCaseValue.ROOT_PROTOCON_CCO_CHILD < DictCommandInfo[value] <
                  AllCertCaseValue.ROOT_PROTOCON_CCO_MAX):
                item_cco_child = QTreeWidgetItem(item_cco_father)
                item_cco_child.setText(0, value)
                item_cco_child.setCheckState(0, Qt.Unchecked)
            elif DictCommandInfo[value] == AllCertCaseValue.ROOT_PERFORMANCE_CHILD:
                item_prerf_father = QTreeWidgetItem(self.AllTestCase)
                item_prerf_father.setText(0, value)
                item_prerf_father.setCheckState(0, Qt.Unchecked)
            elif DictCommandInfo[value] == AllCertCaseValue.ROOT_PERFORMANCE_STA_CHILD:
                item_prerf_sta_father = QTreeWidgetItem(item_prerf_father)
                item_prerf_sta_father.setText(0, value)
                item_prerf_sta_father.setCheckState(0, Qt.Unchecked)
            elif (AllCertCaseValue.ROOT_PERFORMANCE_STA_CHILD < DictCommandInfo[value] <
                  AllCertCaseValue.ROOT_PERFORMANCE_STA_MAX):
                item_perf_sta_child = QTreeWidgetItem(item_prerf_sta_father)
                item_perf_sta_child.setText(0, value)
                item_perf_sta_child.setCheckState(0, Qt.Unchecked)
            elif DictCommandInfo[value] == AllCertCaseValue.ROOT_PERFORMANCE_CCO_CHILD:
                item_prerf_cco_father = QTreeWidgetItem(item_prerf_father)
                item_prerf_cco_father.setText(0, value)
                item_prerf_cco_father.setCheckState(0, Qt.Unchecked)
            elif (AllCertCaseValue.ROOT_PERFORMANCE_CCO_CHILD < DictCommandInfo[value] <
                  AllCertCaseValue.ROOT_PERFORMANCE_CCO_MAX):
                item_perf_cco_child = QTreeWidgetItem(item_prerf_cco_father)
                item_perf_cco_child.setText(0, value)
                item_perf_cco_child.setCheckState(0, Qt.Unchecked)
            elif DictCommandInfo[value] == AllCertCaseValue.ROOT_OTHER_CHILD:
                item_other_father = QTreeWidgetItem(self.AllTestCase)
                item_other_father.setText(0, value)
                item_other_father.setCheckState(0, Qt.Unchecked)
            elif AllCertCaseValue.ROOT_OTHER_CHILD < DictCommandInfo[value] < \
                    AllCertCaseValue.ROOT_OTHER_MAX:
                item_other_child = QTreeWidgetItem(item_other_father)
                item_other_child.setText(0, value)
                item_other_child.setCheckState(0, Qt.Unchecked)

        # 节点全部展开
        self.treeWidget.expandAll()

        # 节点折叠到0
        self.treeWidget.expandToDepth(0)
        # 链接槽函数
        self.treeWidget.itemChanged.connect(self.handlechanged)

    def handlechanged(self, item, column):
        # 获取选中节点的子节点个数
        count = item.childCount()
        # 如果被选中
        if item.checkState(column) == Qt.Checked:
            # 连同下面子子节点全部设置为选中状态
            for f in range(count):
                if item.child(f).checkState(0) != Qt.Checked:
                    item.child(f).setCheckState(0, Qt.Checked)
        # 如果取消选中
        if item.checkState(column) == Qt.Unchecked:
            # 连同下面子子节点全部设置为取消选中状态
            for f in range(count):
                if item.child(f).checkState != Qt.Unchecked:
                    item.child(f).setCheckState(0, Qt.Unchecked)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = tree()
    myshow.show()
    sys.exit(app.exec_())
