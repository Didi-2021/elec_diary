from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_about_us_window_dialog(object):


    def setupUi(self, about_us_window_dialog):
        about_us_window_dialog.setObjectName("about_us_window_dialog")
        about_us_window_dialog.resize(780, 577)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(about_us_window_dialog.sizePolicy().hasHeightForWidth())
        about_us_window_dialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        about_us_window_dialog.setFont(font)
        about_us_window_dialog.setAutoFillBackground(False)
        about_us_window_dialog.setStyleSheet("font: 75 \"Verdana\";\n"
"background-color: rgb(255, 255, 255);")
        self.title_label = QtWidgets.QLabel(parent=about_us_window_dialog)
        self.title_label.setGeometry(QtCore.QRect(0, 0, 781, 131))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("font: 75 14pt \"Verdana\";\n"
"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 2px solid rgb(194, 194, 194);")
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.image_label = QtWidgets.QLabel(parent=about_us_window_dialog)
        self.image_label.setGeometry(QtCore.QRect(40, 150, 271, 201))
        self.image_label.setStyleSheet("border: 1px solid;\n"
"border-color: rgb(85, 170, 255);")
        self.image_label.setText("")
        self.image_label.setPixmap(QtGui.QPixmap('image.jpg'))
        # self.image_label.setPixmap(QtGui.QPixmap('../images/image.jpg'))
        self.image_label.setObjectName("image_label")
        self.label_1 = QtWidgets.QLabel(parent=about_us_window_dialog)
        self.label_1.setGeometry(QtCore.QRect(400, 140, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(parent=about_us_window_dialog)
        self.label_2.setGeometry(QtCore.QRect(400, 200, 361, 81))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=about_us_window_dialog)
        self.label_3.setGeometry(QtCore.QRect(400, 290, 361, 91))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=about_us_window_dialog)
        self.label_4.setGeometry(QtCore.QRect(400, 390, 361, 81))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(parent=about_us_window_dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 370, 301, 191))
        # self.label_6.setGeometry(QtCore.QRect(40, 160, 301, 191))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(parent=about_us_window_dialog)
        self.label_5.setGeometry(QtCore.QRect(400, 480, 361, 81))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(about_us_window_dialog)
        QtCore.QMetaObject.connectSlotsByName(about_us_window_dialog)

    def retranslateUi(self, about_us_window_dialog):
        _translate = QtCore.QCoreApplication.translate
        about_us_window_dialog.setWindowTitle(_translate("about_us_window_dialog", "О нас"))
        self.title_label.setText(_translate("about_us_window_dialog", "Муниципальное казенное общеобразовательное\n"
"учреждение муниципального образования\n"
"\"Городской округ закрытое административно-территориальное\n"
"образование Знаменск Астраханской области\"\n"
"\"Средняя общеобразовательная школа № 233\""))
        self.label_1.setText(_translate("about_us_window_dialog", "Дата создания образовательной организации:\n"
"    31.08.1961"))
        self.label_2.setText(_translate("about_us_window_dialog", "Тип образовательной организации:\n"
"    • начальная общеобразовательная школа\n"
"    • основная общеобразовательная школа\n"
"    • средняя общеобразовательная школа"))
        self.label_3.setText(_translate("about_us_window_dialog", "Юридический адрес:\n"
"      416550, Российская Федерация, Южный\n"
"      федеральный округ,Астраханская обл.,\n"
"      г. Знаменск, ул. Королева, дом 6, корпус А"))
        self.label_4.setText(_translate("about_us_window_dialog", "Режим работы:\n"
"    • 1-9 классы 5-дневная рабочая неделя;\n"
"    • 10-11 классы - 6-дневная рабочая неделя"))
        self.label_6.setText(_translate("about_us_window_dialog", "Контактный телефон:\n"
"    • 8(85140)2-33-41 (директор школы)\n"
"    • 8(85140)2-35-57 (завучи)\n"
"\n"
"Факс:\n"
"    • (851)402 33 41\n"
"\n"
"Адрес электронной почты:\n"
"    • 8514023341@platforma.school\n"
"\n"
"Адрес официального сайта:\n"
"    • https://30znam-soh233.edusite.ru"))
        self.label_5.setText(_translate("about_us_window_dialog", "График работы канцелярии:\n"
"    понедельник - пятница: 8.00-16.30\n"
"    перерыв: 12.00-12.30\n"
"    выходные дни: суббота, воскресенье\n"
"   "))

