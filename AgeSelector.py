__author__ = 'red'
import sys
from PyQt4 import QtGui, QtCore

class AgeSelector(QtGui.QWidget):
    def __init__(self):
        super(AgeSelector,self).__init__()
        self.initUI()

    def initUI(self):
        self.spinbox = QtGui.QSpinBox()
        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.spinbox.setRange(0, 100)
        self.slider.setRange(0, 100)


        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.spinbox)
        layout.addWidget(self.slider)
        self.setLayout(layout)

        #connection settings
        self.connect(self.spinbox, QtCore.SIGNAL("valueChanged(int)"),\
                    self.slider, QtCore.SLOT("setValue(int)"))
        self.connect(self.slider, QtCore.SIGNAL("valueChanged(int)"), \
                    self.spinbox, QtCore.SLOT("setValue(int)"))
        self.connect(self.spinbox, QtCore.SIGNAL("valueChanged(int)"),\
                    self.log_to_console)


    def log_to_console(self, i):
        print i


        self.slider.setValue(27)



def main():

    app = QtGui.QApplication(sys.argv)
    select = AgeSelector()
    select.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()