from PyQt6 import QtCore, QtWidgets
import dbHandler


class CheckThread(QtCore.QThread):
    textSignal = QtCore.pyqtSignal(str)
    nextWindowSignal = QtCore.pyqtSignal(str)


    def thr_login(self, name, password):
        return dbHandler.login(name, password, self.textSignal, self.nextWindowSignal)
    #


class Ui_AuthWindow(object):
    def __init__(self):
        self.checkDbThread = CheckThread()
        self.checkDbThread.textSignal.connect(self.message)

    def setupUi(self, Dialog):
        Dialog = Dialog
        Dialog.setObjectName("AuthorizationWindow")
        Dialog.resize(420, 220)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setAutoFillBackground(True)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 30, 341, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.loginLineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.loginLineEdit.setObjectName("loginLineEdit")
        self.gridLayout.addWidget(self.loginLineEdit, 0, 1, 1, 1)
        self.passwordLineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.gridLayout.addWidget(self.passwordLineEdit, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.authButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.authButton.setObjectName("authButton")
        self.verticalLayout.addWidget(self.authButton)
        self.registerButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.registerButton.setObjectName("registerButton")
        self.verticalLayout.addWidget(self.registerButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Авторизация"))
        self.label.setText(_translate("Dialog", "Логин"))
        self.label_2.setText(_translate("Dialog", "Пароль"))
        self.authButton.setText(_translate("Dialog", "Авторизоваться"))
        self.registerButton.setText(_translate("Dialog", "Зарегистрироваться"))

    def auth(self):
        log = self.loginLineEdit.text()
        passwrd = self.passwordLineEdit.text()
        self.checkDbThread.thr_login(log, passwrd)

    def reg(self):
        QtWidgets.QMessageBox.about(QtWidgets.QDialog(), 'Оповещение', 'Создание ученой записи только с разрешения Супер пользователя')

    def message(self, text):
        QtWidgets.QMessageBox.about(QtWidgets.QDialog(), 'Оповещение', text)














