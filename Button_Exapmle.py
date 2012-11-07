__author__ = 'red'
import sys
from PyQt4 import QtGui

class AnyWidget(QtGui.QWidget):
    def __init__(self,*args):
        QtGui.QWidget.__init__(self,*args)
        button = QtGui.QPushButton(u"Button",self)
        button_2 = QtGui.QPushButton(u"Button2",self)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(button_2)
        self.setLayout(layout)



if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    aw = AnyWidget()
    aw.show()
    sys.exit(app.exec_())
