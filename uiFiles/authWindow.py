from PyQt6 import QtCore, QtGui, QtWidgets
import dbHandler


class CheckThread(QtCore.QThread):
    textSignal = QtCore.pyqtSignal(str)
    nextWindowSignal = QtCore.pyqtSignal(str, str, str, str)

    def thr_login(self, login, password):
        return dbHandler.login(login, password, self.textSignal, self.nextWindowSignal)


class Ui_AuthWindow(object):
    def __init__(self):
        self.checkDbThread = CheckThread()
        self.checkDbThread.textSignal.connect(self.message)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(440, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        Dialog.setFont(font)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(80, 80, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(80, 110, 281, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border: 2px solid rgb(194, 194, 194);\n"
"border-radius: 5px;")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 75 20pt \"Verdana\";\n"
"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 2px solid rgb(194, 194, 194);")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 150, 48, 22))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 180, 281, 31))
        self.lineEdit_2.setStyleSheet("background-color:  rgb(240, 240, 240);\n"
"border: 2px solid rgb(194, 194, 194);\n"
"border-radius: 5px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 240, 281, 31))
        self.pushButton.setStyleSheet("border-radius: 5px; \n"
"font: 75 12pt \"Verdana\";\n"
"color: rgb(255, 255, 255); \n"
"background-color: qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(85, 170, 127, 255), stop:1 rgba(26, 203, 26, 255));")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 290, 281, 24))
        self.pushButton_2.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 255);\n"
"font: 8pt \"Verdana\";\n"
"text-decoration: underline;\n"
"border-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Авторизация"))
        self.label.setText(_translate("Dialog", "Логин"))
        self.label_3.setText(_translate("Dialog", "Войти в дневник"))
        self.label_2.setText(_translate("Dialog", "Пароль"))
        self.pushButton.setText(_translate("Dialog", "Авторизоваться"))
        self.pushButton_2.setText(_translate("Dialog", "Как зарегистрироваться"))

    def auth(self):
        log = self.lineEdit.text()
        passwrd = self.lineEdit_2.text()
        self.checkDbThread.thr_login(log, passwrd)

    def reg(self):
        QtWidgets.QMessageBox.about(QtWidgets.QDialog(), 'Оповещение',
                                    'Создание ученой записи только с разрешения Супер пользователя')

    def message(self, text):
        QtWidgets.QMessageBox.about(QtWidgets.QDialog(), 'Оповещение', text)

