# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/red/pyQT/pyQT/ui_example.ui'
#
# Created: Mon Oct 29 18:41:21 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(452, 293)
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 431, 271))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.leftText = QtGui.QTextEdit(self.widget)
        self.leftText.setObjectName(_fromUtf8("leftText"))
        self.gridLayout.addWidget(self.leftText, 0, 0, 1, 1)
        self.buttonBack = QtGui.QPushButton(self.widget)
        self.buttonBack.setObjectName(_fromUtf8("buttonBack"))
        self.gridLayout.addWidget(self.buttonBack, 1, 1, 1, 1)
        self.rightText = QtGui.QTextEdit(self.widget)
        self.rightText.setObjectName(_fromUtf8("rightText"))
        self.gridLayout.addWidget(self.rightText, 0, 1, 1, 1)
        self.buttonForward = QtGui.QPushButton(self.widget)
        self.buttonForward.setObjectName(_fromUtf8("buttonForward"))
        self.gridLayout.addWidget(self.buttonForward, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.buttonForward, QtCore.SIGNAL(_fromUtf8("clicked()")), self.leftText.selectAll)
        QtCore.QObject.connect(self.buttonForward, QtCore.SIGNAL(_fromUtf8("clicked()")), self.leftText.cut)
        QtCore.QObject.connect(self.buttonForward, QtCore.SIGNAL(_fromUtf8("clicked()")), self.rightText.clear)
        QtCore.QObject.connect(self.buttonForward, QtCore.SIGNAL(_fromUtf8("clicked()")), self.rightText.paste)
        QtCore.QObject.connect(self.buttonBack, QtCore.SIGNAL(_fromUtf8("clicked()")), self.rightText.selectAll)
        QtCore.QObject.connect(self.buttonBack, QtCore.SIGNAL(_fromUtf8("clicked()")), self.rightText.cut)
        QtCore.QObject.connect(self.buttonBack, QtCore.SIGNAL(_fromUtf8("clicked()")), self.leftText.clear)
        QtCore.QObject.connect(self.buttonBack, QtCore.SIGNAL(_fromUtf8("clicked()")), self.leftText.paste)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonBack.setText(QtGui.QApplication.translate("Form", "<-сюда", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonForward.setText(QtGui.QApplication.translate("Form", "туда ->", None, QtGui.QApplication.UnicodeUTF8))

