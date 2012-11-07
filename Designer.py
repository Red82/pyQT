__author__ = 'red'
import sys, form1
from PyQt4 import QtGui, QtCore

def main():

    app = QtGui.QApplication(sys.argv)
    u = form1.Ui_MainWindow()
    mw = QtGui.QMainWindow()
    u.setupUi(mw)
    mw.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()