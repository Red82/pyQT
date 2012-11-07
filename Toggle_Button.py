__author__ = 'red'
import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.colr = QtGui.QColor(0,0,0)

        self.redb = QtGui.QPushButton('Red', self)
        self.redb.setCheckable(True)
        self.redb.move(10,10)

        self.redb.clicked[bool].connect(self.setColor)

        self.greenb = QtGui.QPushButton('Green', self)
        self.greenb.setCheckable(True)
        self.greenb.move(10, 60)

        self.greenb.clicked[bool].connect(self.setColor)

        self.blueb = QtGui.QPushButton('Blue', self)
        self.blueb.setCheckable(True)
        self.blueb.move(10, 110)

        self.blueb.clicked[bool].connect(self.setColor)

        self.square = QtGui.QFrame(self)
        self.square.setGeometry(100,20,100,100)
        self.square.setStyleSheet("QWidget "
                                  "{ background-color: %s}"
                                    %self.colr.name())

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Toggle Buttons')
        self.show()

    def setColor(self, pressed):

        source = self.sender()

        if pressed:
            val = 255
        else: val = 0

        if source.text() == "Red":
            self.colr.setRed(val)
        elif source.text() == "Green":
            self.colr.setGreen(val)
        else:
            self.colr.setBlue(val)

        self.square.setStyleSheet("QFrame { background-color: %s}"
                                  %self.colr.name())


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
