from PyQt5 import QtCore, QtGui, QtWidgets
from OutputG import OutputGroups
from OutputS import OutputStudent
from OutputSG import OutputStudentNewG
from KartochkaS import KartochkaS

class Ui_Output():
    def setupUi(self, Dialog):
        Dialog.setObjectName("Добавление")
        Dialog.resize(806, 536)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 62);")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 210, 641, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton.setFont(font)
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
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setAutoRepeatInterval(100)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setMouseTracking(True)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
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
        self.pushButton_4.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_4.setAutoRepeatInterval(100)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setMouseTracking(True)
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
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setAutoRepeatInterval(100)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(18)
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
        self.pushButton_3.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_3.setAutoRepeatInterval(100)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 60, 639, 111))
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.Set)
        self.pushButton_2.clicked.connect(self.Set2)
        self.pushButton_4.clicked.connect(self.Set4)
        self.pushButton_3.clicked.connect(self.Set3)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Просмотр"))
        self.pushButton.setToolTip(_translate("Dialog", "<html><head/><body><p>фыв</p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Список студентов"))
        self.pushButton_2.setText(_translate("Dialog", "Список групп"))
        self.pushButton_4.setText(_translate("Dialog", "Список переведенных студентов"))
        self.pushButton_3.setText(_translate("Dialog", "Карточка студента"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color:#ffffff;\">Категории</span></p></body></html>"))


    def Set(self):  # Список студентов
        self.window=QtWidgets.QMainWindow()
        self.f= OutputStudent()
        self.f.setupUi(self.window)
        self.window.show()
    def Set2(self):  # Список групп
        self.window=QtWidgets.QMainWindow()
        self.f=OutputGroups()
        self.f.setupUi(self.window)
        self.window.show()
    def Set3(self):  # Карточка студента
        self.window=QtWidgets.QMainWindow()
        self.f=KartochkaS()
        self.f.setupUi(self.window)
        self.window.show()
    def Set4(self):  # Переведённые студенты
        self.window=QtWidgets.QMainWindow()
        self.f=OutputStudentNewG()
        self.f.setupUi(self.window)
        self.window.show()

        
