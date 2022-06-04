# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Glafwindow(1).ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import adduvg
from  AddU import Ui_AddUchenik
from addg import Ui_AddGrupp
class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(806, 536)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 62);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 210, 501, 71))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(1, 226, 178);\n"
"background-color: rgb(208, 178, 9);\n"
"border: 3px solid;\n"
"border-radius: 25 solid ;\n"
"border-color:  rgb(213, 194, 166);}\n"
"QPushButton:pressed{\n"
"background-color: rgb(191, 162, 0);\n"
"border: 3px solid;\n"
"border-radius: 25 solid ;\n"
"border-color:  rgb(213, 194, 166);}\n"
"")
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 310, 501, 71))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setMouseTracking(True)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background-color: rgb(1, 226, 178);\n"
"background-color: rgb(208, 178, 9);\n"
"border: 3px solid;\n"
"border-radius: 25 solid ;\n"
"border-color:  rgb(213, 194, 166);}\n"
"QPushButton:pressed{\n"
"background-color: rgb(191, 162, 0);\n"
"border: 3px solid;\n"
"border-radius: 25 solid ;\n"
"border-color:  rgb(213, 194, 166);}\n"
"")
        self.pushButton_3.setObjectName("pushButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 410, 501, 61))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(1, 226, 178);\n"
"background-color: rgb(208, 178, 9);\n"
"border: 3px solid;\n"
"border-radius: 25 solid ;\n"
"border-color:  rgb(213, 194, 166);}\n"
"QPushButton:pressed{\n"
"background-color: rgb(191, 162, 0);\n"
"border: 3px solid;\n"
"border-radius: 25 solid ;\n"
"border-color:  rgb(213, 194, 166);}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 70, 611, 81))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("border: 3px solid;\n"
"\n"
"border-radius: 25 solid ;\n"
"border-color: White;\n"
"")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.Set)
        self.pushButton_3.clicked.connect(self.Set2)
        self.pushButton_2.clicked.connect(self.Set4)
        self.prov=uic.loadUi('adduvg(1).ui')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setToolTip(_translate("Dialog", "<html><head/><body><p>фыв</p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Добавить ученика"))
        self.pushButton_3.setText(_translate("Dialog", "Добавить группу"))
        self.pushButton_2.setText(_translate("Dialog", "Добавить ученика в группу"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Категории</span></p></body></html>"))

    def Set(self):
        self.window = QtWidgets.QMainWindow()
        self.f = Ui_AddUchenik()
        self.f.setupUi(self.window)
        self.window.show()

    def Set2(self):
        self.window = QtWidgets.QMainWindow()
        self.f = Ui_AddGrupp()
        self.f.setupUi(self.window)
        self.window.show()

    def Set4(self):
        self.prov = adduvg.test()
        #sys.exit(main.app.exec_())
        # self.window = QtWidgets.QMainWindow()
        # self.f = Ui_MainWindow()
        # self.f.setupUi(self.window)
        # self.window.show()

