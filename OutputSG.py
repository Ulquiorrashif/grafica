from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel

import sqlite3

class OutputStudentNewG(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(611, 315)
        Dialog.setStyleSheet("background-color: rgb(135, 206, 250);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(20, 10, 581, 51))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("border: 3px solid;\n"
"\n"
"border-radius: 25 solid ;\n"
"border-color: White;\n"
"")
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(25, 90, 561, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Dialog)
        self.output()
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))

    def output(self):
        self.label.setText("Список переведённых студентов")
        self.label.setAlignment(Qt.AlignCenter)

        con = sqlite3.connect('uni.db')
        cur = con.cursor()
        allList = cur.execute("""SELECT students.user_FIO, redact_group.group_DO, redact_group.group_POSLE, group_faculty FROM redact_group 
                                INNER JOIN students ON redact_group.user_id = students.user_id
                                INNER JOIN groups ON redact_group.group_DO = groups.group_title""").fetchall()
        list2 = cur.execute("""SELECT group_faculty FROM redact_group 
                                INNER JOIN groups ON redact_group.group_POSLE = groups.group_title""").fetchall()
        for i in range(len(allList)):
            allList = [allList[i]+list2[i]]
        print(allList)
             
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(len(allList))
        self.tableWidget.setHorizontalHeaderLabels(["ФИО студента", "Предыдущая группа", "Текущая группа", "Предыдущее направление", "Текущее направление"])

        for i in range(len(allList)):
            for j in range(5):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(allList[i][j])))
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.resizeColumnsToContents()
