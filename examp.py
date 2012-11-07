__author__ = 'red'
import sys
from PyQt4 import QtCore, QtGui

class userInterface(QtGui.QWidget):
    def __init__(self):
        super(userInterface,self).__init__()
        self.initUT()

    def initUT(self):

        self.frame = QtGui.QFrame()
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)

        self.grid = QtGui.QGridLayout()
        self.grid.addWidget(self.frame)

        self.label = QtGui.QLabel("Metka", self.frame)
        self.grid.addWidget(self.label, 0,0)

        self.edit = QtGui.QLineEdit("Vinni Pux",self.frame)
        self.grid.addWidget(self.edit, 0,1)

        self.radio_groop = QtGui.QGroupBox("Vibor iz dvux:", self.frame)
        self.radio_lay = QtGui.QVBoxLayout(self.radio_groop)

        self.rad1 = QtGui.QRadioButton("First", self.radio_groop)
        self.rad2 = QtGui.QRadioButton("Second", self.radio_groop)

        self.rad1.setChecked(True)
        self.radio_lay.addWidget(self.rad1)
        self.radio_lay.addWidget(self.rad2)

        self.grid.addWidget(self.radio_groop, 1,0,3,1)

        self.combo = QtGui.QComboBox(self.frame)
        self.combo.addItem("Pjatachok")
        self.combo.setEditable(True)
        self.grid.addWidget(self.combo,1,1)

        self.spin = QtGui.QSpinBox(self.frame)
        self.spin.setRange(0,10)
        self.spin.setValue(5)
        self.grid.addWidget(self.spin, 2,1)

        self.check = QtGui.QCheckBox("Pometka",self.frame)
        self.check.setChecked(True)
        self.grid.addWidget(self.check,3,1)

        self.progress = QtGui.QProgressBar(self.frame)
        self.progress.setRange(0,100)
        self.progress.setValue(50)
        self.grid.addWidget(self.progress, 4,0,1,2)

        self.btn_layout = QtGui.QHBoxLayout()
        self.btn1 = QtGui.QPushButton("Ok", self.frame)
        self.btn2 = QtGui.QPushButton("Cancel", self.frame)
        self.btn_layout.addWidget(self.btn1)
        self.btn_layout.addWidget(self.btn2)
        self.grid.addLayout(self.btn_layout, 5,0,1,2)


        self.setLayout(self.grid)

def main():

    app = QtGui.QApplication(sys.argv)
    ui = userInterface()
    ui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
