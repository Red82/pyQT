__author__ = 'red'
import  sys
from PyQt4 import  QtGui, QtCore
from ui_example import Ui_Form
class UI(QtGui.QWidget):
    def __init__(self):
        super(UI,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


def main():

    app = QtGui.QApplication(sys.argv)

    ui = UI()
    ui.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
