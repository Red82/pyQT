# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/red/pyQT/pyQT/calc_form.ui'
#
# Created: Tue Oct 30 16:01:53 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(QtGui.QWidget):

    #Instance Vars
    st = '' #Stores string for textBrowser
    operation = '' #Current operation
    currentNum = 0
    previousNum = 0
    sol = 0
    buffer = ''


    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(392, 349)
        Form.setWindowTitle("Calculator")
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 368, 326))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_0 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_0.setObjectName(_fromUtf8("pushButton_0"))
        self.gridLayout.addWidget(self.pushButton_0, 5, 0, 1, 1)
        self.pushButton_multiply = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_multiply.setObjectName(_fromUtf8("pushButton_multiply"))
        self.gridLayout.addWidget(self.pushButton_multiply, 3, 3, 1, 1)
        self.pushButton_1 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.gridLayout.addWidget(self.pushButton_1, 4, 0, 1, 1)
        self.pushButton_clear = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_clear.setObjectName(_fromUtf8("pushButton_clear"))
        self.gridLayout.addWidget(self.pushButton_clear, 0, 3, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)
        self.pushButton_8 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout.addWidget(self.pushButton_6, 3, 2, 1, 1)
        self.pushButton_cancel = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.gridLayout.addWidget(self.pushButton_cancel, 1, 3, 1, 1)
        self.pushButton_9 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)
        self.pushButton_divide = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_divide.setObjectName(_fromUtf8("pushButton_divide"))
        self.gridLayout.addWidget(self.pushButton_divide, 2, 3, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1)
        self.pushButton_equal = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_equal.setObjectName(_fromUtf8("pushButton_equal"))
        self.gridLayout.addWidget(self.pushButton_equal, 5, 1, 1, 2)
        self.pushButton_3 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 4, 2, 1, 1)
        self.pushButton_minus = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_minus.setObjectName(_fromUtf8("pushButton_minus"))
        self.gridLayout.addWidget(self.pushButton_minus, 4, 3, 1, 1)
        self.pushButton_plus = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_plus.setObjectName(_fromUtf8("pushButton_plus"))
        self.gridLayout.addWidget(self.pushButton_plus, 5, 3, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout.addWidget(self.pushButton_5, 3, 1, 1, 1)
        self.textBrowser = QtGui.QTextBrowser(self.layoutWidget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 2, 3)

        self.retranslateUi(Form)
        #Connect Numeric Buttons
        QtCore.QObject.connect(self.pushButton_0, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClicked)
        QtCore.QObject.connect(self.pushButton_1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClicked)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClicked)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClicked)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClicked)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClicked)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClicked)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClicked)
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClicked)
        QtCore.QObject.connect(self.pushButton_9, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClicked)
        #Connect Ctr Button
        QtCore.QObject.connect(self.pushButton_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ctrClicked)
        #Connect Cancel Button
        QtCore.QObject.connect(self.pushButton_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), self.CancelClicked)
        #Connect Equal Button
        QtCore.QObject.connect(self.pushButton_equal, QtCore.SIGNAL(_fromUtf8("clicked()")), self.equalButton)
        #Connect Option Buttons
        QtCore.QObject.connect(self.pushButton_plus, QtCore.SIGNAL(_fromUtf8("clicked()")), self.optClicked)
        QtCore.QObject.connect(self.pushButton_minus, QtCore.SIGNAL(_fromUtf8("clicked()")), self.optClicked)
        QtCore.QObject.connect(self.pushButton_multiply, QtCore.SIGNAL(_fromUtf8("clicked()")), self.optClicked)
        QtCore.QObject.connect(self.pushButton_divide, QtCore.SIGNAL(_fromUtf8("clicked()")), self.optClicked)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def buttonClicked(self):
        Ui_Form.st = Ui_Form.st + self.sender().text()
        Ui_Form.buffer = self.sender().text()
        self.textBrowser.setText(Ui_Form.st)
        Ui_Form.currentNum = int(Ui_Form.st)
        print Ui_Form.buffer, Ui_Form.currentNum

    def optClicked(self):
        Ui_Form.previousNum = Ui_Form.currentNum
        Ui_Form.currentNum = 0
        Ui_Form.st = ''
        Ui_Form.operation = self.sender().objectName()

    def ctrClicked(self):
        Ui_Form.currentNum = 0
        Ui_Form.previousNum = 0
        Ui_Form.st = ''
        self.textBrowser.setText('0')

    def CancelClicked(self):
        Ui_Form.st = Ui_Form.st[:-1]
        Ui_Form.currentNum = int(Ui_Form.st)
        self.textBrowser.setText(Ui_Form.st)

    def equalButton(self):
        if Ui_Form.operation == 'pushButton_plus':
            Ui_Form.sol = Ui_Form.previousNum + Ui_Form.currentNum
            print Ui_Form.previousNum, Ui_Form.currentNum, Ui_Form.sol

        if Ui_Form.operation == 'pushButton_minus':
            Ui_Form.sol = Ui_Form.previousNum - Ui_Form.currentNum

        if Ui_Form.operation == 'pushButton_multiply':
            Ui_Form.sol = Ui_Form.previousNum * Ui_Form.currentNum

        if Ui_Form.operation == 'pushButton_divide':
            Ui_Form.sol = Ui_Form.previousNum / Ui_Form.currentNum

        self.sol_str = str(Ui_Form.sol)
        Ui_Form.st = ''
        Ui_Form.currentNum = Ui_Form.sol
        self.textBrowser.setText(self.sol_str)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Calculator", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_0.setText(QtGui.QApplication.translate("Form", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_multiply.setText(QtGui.QApplication.translate("Form", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_1.setText(QtGui.QApplication.translate("Form", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_clear.setText(QtGui.QApplication.translate("Form", "Clr", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("Form", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(QtGui.QApplication.translate("Form", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("Form", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_cancel.setText(QtGui.QApplication.translate("Form", "<--", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setText(QtGui.QApplication.translate("Form", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_divide.setText(QtGui.QApplication.translate("Form", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Form", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_equal.setText(QtGui.QApplication.translate("Form", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_minus.setText(QtGui.QApplication.translate("Form", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_plus.setText(QtGui.QApplication.translate("Form", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("Form", "5", None, QtGui.QApplication.UnicodeUTF8))

