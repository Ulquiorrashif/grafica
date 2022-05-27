'''from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

def application():
    app=QApplication(sys.argv)
    window=QMainWindow()
    window.setWindowTitle("Начало)")
    window.setGeometry(300,300,300,300)
    a=QtWidgets.QLabel(window)
    a.setText("я заебался")

    a.move(125,125)
    window.show()
    sys.exit(app.exec())
if __name__=="__main__":
    application()'''

from PyQt5 import QtCore, QtGui, QtWidgets
import Glafwindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Glafwindow.Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
