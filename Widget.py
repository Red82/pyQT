__author__ = 'red'
'''
Issleduem CheckBox
'''
import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.cb_1 = QtGui.QCheckBox('Tutorial', self)
        self.cb_1.move(20, 20)
        self.cb_1.toggle()
        self.cb_1.stateChanged.connect(self.change_Title)

        self.cb_2 = QtGui.QCheckBox('Libraries', self)
        self.cb_2.move(120, 20)
        self.cb_2.toggle()
        self.cb_2.stateChanged.connect(self.change_Geometri)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.show()

    def change_Title(self, c):

        if c == QtCore.Qt.Checked:
            self.setWindowTitle('This is a new program')
        else:
            self.setWindowTitle(' :) ')

    def change_Geometri(self, c):
        if c == QtCore.Qt.Checked:
            self.setGeometry(100, 100, 250, 150)
        else:
            self.setGeometry(300, 300, 250, 150)

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
