# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogsystemscan.ui'
#
# Created: Wed Oct  1 11:19:20 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DialogSystemScan(object):
    def setupUi(self, DialogSystemScan):
        DialogSystemScan.setObjectName("DialogSystemScan")
        DialogSystemScan.resize(QtCore.QSize(QtCore.QRect(0,0,400,379).size()).expandedTo(DialogSystemScan.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(DialogSystemScan)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setObjectName("hboxlayout")

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)

        self.label = QtGui.QLabel(DialogSystemScan)
        self.label.setPixmap(QtGui.QPixmap(":/logos/IcepapCfg Icons/IcepapMed.png"))
        self.label.setObjectName("label")
        self.hboxlayout.addWidget(self.label)

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.label_2 = QtGui.QLabel(DialogSystemScan)
        self.label_2.setObjectName("label_2")
        self.vboxlayout.addWidget(self.label_2)

        self.tableLog = QtGui.QTableWidget(DialogSystemScan)

        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(16,16,16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.WindowText,brush)

        brush = QtGui.QBrush(QtGui.QColor(239,235,231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Button,brush)

        brush = QtGui.QBrush(QtGui.QColor(237,237,237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Light,brush)

        brush = QtGui.QBrush(QtGui.QColor(247,245,243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Midlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(119,117,115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Dark,brush)

        brush = QtGui.QBrush(QtGui.QColor(159,157,154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Mid,brush)

        brush = QtGui.QBrush(QtGui.QColor(16,16,16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Text,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.BrightText,brush)

        brush = QtGui.QBrush(QtGui.QColor(16,16,16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.ButtonText,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(239,235,231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Window,brush)

        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Shadow,brush)

        brush = QtGui.QBrush(QtGui.QColor(101,148,235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.HighlightedText,brush)

        brush = QtGui.QBrush(QtGui.QColor(0,0,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Link,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,0,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.LinkVisited,brush)

        brush = QtGui.QBrush(QtGui.QColor(247,245,243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.AlternateBase,brush)

        brush = QtGui.QBrush(QtGui.QColor(16,16,16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.WindowText,brush)

        brush = QtGui.QBrush(QtGui.QColor(239,235,231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Button,brush)

        brush = QtGui.QBrush(QtGui.QColor(237,237,237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Light,brush)

        brush = QtGui.QBrush(QtGui.QColor(247,245,243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Midlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(119,117,115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Dark,brush)

        brush = QtGui.QBrush(QtGui.QColor(159,157,154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Mid,brush)

        brush = QtGui.QBrush(QtGui.QColor(16,16,16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Text,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.BrightText,brush)

        brush = QtGui.QBrush(QtGui.QColor(16,16,16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.ButtonText,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(239,235,231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Window,brush)

        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Shadow,brush)

        brush = QtGui.QBrush(QtGui.QColor(101,148,235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.HighlightedText,brush)

        brush = QtGui.QBrush(QtGui.QColor(0,0,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Link,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,0,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.LinkVisited,brush)

        brush = QtGui.QBrush(QtGui.QColor(247,245,243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.AlternateBase,brush)

        brush = QtGui.QBrush(QtGui.QColor(127,125,123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.WindowText,brush)

        brush = QtGui.QBrush(QtGui.QColor(239,235,231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Button,brush)

        brush = QtGui.QBrush(QtGui.QColor(237,237,237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Light,brush)

        brush = QtGui.QBrush(QtGui.QColor(247,245,243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Midlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(119,117,115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Dark,brush)

        brush = QtGui.QBrush(QtGui.QColor(159,157,154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Mid,brush)

        brush = QtGui.QBrush(QtGui.QColor(51,77,120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Text,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.BrightText,brush)

        brush = QtGui.QBrush(QtGui.QColor(127,125,123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.ButtonText,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(239,235,231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Window,brush)

        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Shadow,brush)

        brush = QtGui.QBrush(QtGui.QColor(84,123,196))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.HighlightedText,brush)

        brush = QtGui.QBrush(QtGui.QColor(0,0,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Link,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,0,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.LinkVisited,brush)

        brush = QtGui.QBrush(QtGui.QColor(247,245,243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.AlternateBase,brush)
        self.tableLog.setPalette(palette)
        self.tableLog.setObjectName("tableLog")
        self.vboxlayout.addWidget(self.tableLog)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setObjectName("hboxlayout1")

        spacerItem2 = QtGui.QSpacerItem(131,31,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem2)

        self.okButton = QtGui.QPushButton(DialogSystemScan)
        self.okButton.setObjectName("okButton")
        self.hboxlayout1.addWidget(self.okButton)
        self.vboxlayout.addLayout(self.hboxlayout1)

        self.retranslateUi(DialogSystemScan)
        QtCore.QObject.connect(self.okButton,QtCore.SIGNAL("clicked()"),DialogSystemScan.accept)
        QtCore.QMetaObject.connectSlotsByName(DialogSystemScan)

    def retranslateUi(self, DialogSystemScan):
        DialogSystemScan.setWindowTitle(QtGui.QApplication.translate("DialogSystemScan", "Icepap System Conflicts", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogSystemScan", "Conflicts", None, QtGui.QApplication.UnicodeUTF8))
        self.tableLog.clear()
        self.tableLog.setColumnCount(3)
        self.tableLog.setRowCount(0)

        headerItem = QtGui.QTableWidgetItem()
        headerItem.setText(QtGui.QApplication.translate("DialogSystemScan", "Object", None, QtGui.QApplication.UnicodeUTF8))
        self.tableLog.setHorizontalHeaderItem(0,headerItem)

        headerItem1 = QtGui.QTableWidgetItem()
        headerItem1.setText(QtGui.QApplication.translate("DialogSystemScan", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.tableLog.setHorizontalHeaderItem(1,headerItem1)

        headerItem2 = QtGui.QTableWidgetItem()
        headerItem2.setText(QtGui.QApplication.translate("DialogSystemScan", "Action", None, QtGui.QApplication.UnicodeUTF8))
        self.tableLog.setHorizontalHeaderItem(2,headerItem2)
        self.okButton.setText(QtGui.QApplication.translate("DialogSystemScan", "OK", None, QtGui.QApplication.UnicodeUTF8))

import icepapcms_rc
