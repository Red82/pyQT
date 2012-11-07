__author__ = 'red'
import sys
from PyQt4 import QtGui, QtCore
from calculator import Ui_Form

class Calc(QtGui.QWidget):
    def __init__(self):
        super(Calc,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


def main():

    app = QtGui.QApplication(sys.argv)
    clc = Calc()
    clc.setMinimumSize(392, 349)
    clc.setMaximumSize(392, 349)
    clc.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
