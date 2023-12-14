from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_welcome_window_dialog(object):
    def setupUi(self, welcome_window_dialog):
        welcome_window_dialog.setObjectName("welcome_window_dialog")
        welcome_window_dialog.resize(440, 290)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(welcome_window_dialog.sizePolicy().hasHeightForWidth())
        welcome_window_dialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        welcome_window_dialog.setFont(font)
        welcome_window_dialog.setAutoFillBackground(False)
        welcome_window_dialog.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"background-color: rgb(255, 255, 255);")
        self.welcome_label = QtWidgets.QLabel(parent=welcome_window_dialog)
        self.welcome_label.setGeometry(QtCore.QRect(0, 0, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.welcome_label.setFont(font)
        self.welcome_label.setStyleSheet("font: 75 20pt \"Verdana\";\n"
"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 2px solid rgb(194, 194, 194);")
        self.welcome_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.welcome_label.setObjectName("welcome_label")
        self.about_us_button = QtWidgets.QPushButton(parent=welcome_window_dialog)
        self.about_us_button.setGeometry(QtCore.QRect(55, 200, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.about_us_button.setFont(font)
        self.about_us_button.setStyleSheet("border-radius: 5px; \n"
"font: 75 12pt \"Verdana\";\n"
"color: rgb(255, 255, 255); \n"
"background-color: qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(85, 170, 127, 255), stop:1 rgba(26, 203, 26, 255));")
        self.about_us_button.setObjectName("about_us_button")
        self.login_button = QtWidgets.QPushButton(parent=welcome_window_dialog)
        self.login_button.setGeometry(QtCore.QRect(55, 130, 331, 41))
        self.login_button.setStyleSheet("border-radius: 5px; \n"
"font: 75 12pt \"Verdana\";\n"
"color: rgb(255, 255, 255); \n"
"background-color: qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(85, 170, 127, 255), stop:1 rgba(26, 203, 26, 255));")
        self.login_button.setObjectName("login_button")

        self.retranslateUi(welcome_window_dialog)
        QtCore.QMetaObject.connectSlotsByName(welcome_window_dialog)

    def retranslateUi(self, welcome_window_dialog):
        _translate = QtCore.QCoreApplication.translate
        welcome_window_dialog.setWindowTitle(_translate("welcome_window_dialog", "Приветствие"))
        self.welcome_label.setText(_translate("welcome_window_dialog", "Добро пожаловать"))
        self.about_us_button.setText(_translate("welcome_window_dialog", "О нас"))
        self.login_button.setText(_translate("welcome_window_dialog", "Войти в дневник"))

