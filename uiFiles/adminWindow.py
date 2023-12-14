from PyQt6 import QtCore, QtGui, QtWidgets, QtSql


class Ui_AdminWindow(object):
    conn = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    conn.setDatabaseName('db/database.db')

    def addUserRecord(self):
        self.usersTableModel.insertRow(self.usersTableModel.rowCount())

    def deleteUserRecord(self):
        self.usersTableModel.removeRow(self.tableView.currentIndex().row())
        self.usersTableModel.select()

    def addLessonRecord(self):
        self.lessonTableModel.insertRow(self.lessonTableModel.rowCount())

    def deleteLessonRecord(self):
        self.lessonTableModel.removeRow(self.tableView_2.currentIndex().row())
        self.lessonTableModel.select()

    def setupUi(self, adminDialog):
        adminDialog.setObjectName("adminDialog")
        adminDialog.resize(900, 417)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(adminDialog.sizePolicy().hasHeightForWidth())
        adminDialog.setSizePolicy(sizePolicy)
        self.adminTabWidget = QtWidgets.QTabWidget(parent=adminDialog)
        self.adminTabWidget.setGeometry(QtCore.QRect(20, 60, 861, 341))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.adminTabWidget.setFont(font)
        self.adminTabWidget.setStyleSheet("font: 75 10pt \"Verdana\";")
        self.adminTabWidget.setObjectName("adminTabWidget")


###############################################################################################
        self.usersTab = QtWidgets.QWidget()
        self.usersTab.setObjectName("usersTab")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.usersTab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 811, 291))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.deleteUserButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.deleteUserButton.setStyleSheet("border-radius: 2px; \n"
                                               "font: 75 10pt \"Verdana\";\n"
                                               "color: rgb(0, 0, 0);\n"
                                               "background-color: rgb(240, 240, 240);\n"
                                               "border: 1px solid rgb(0, 0, 0);")
        self.deleteUserButton.setObjectName("deleteUserButton")
        self.deleteUserButton.clicked.connect(self.deleteUserRecord)
        self.gridLayout.addWidget(self.deleteUserButton, 2, 0, 1, 1)
        self.usersTableModel = QtSql.QSqlTableModel(parent=self.gridLayoutWidget)
        self.usersTableModel.setTable('users')
        self.usersTableModel.setSort(0, QtCore.Qt.SortOrder.AscendingOrder)
        self.usersTableModel.select()
        self.usersTableModel.setHeaderData(0, QtCore.Qt.Orientation.Horizontal, 'Логин')
        self.usersTableModel.setHeaderData(1, QtCore.Qt.Orientation.Horizontal, 'Пароль')
        self.usersTableModel.setHeaderData(2, QtCore.Qt.Orientation.Horizontal, 'Имя учителя (ребенка)')
        self.usersTableModel.setHeaderData(3, QtCore.Qt.Orientation.Horizontal, 'Группа')
        self.tableView = QtWidgets.QTableView(parent=self.gridLayoutWidget)
        self.tableView.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
        self.tableView.setObjectName("tableView")
        self.tableView.setModel(self.usersTableModel)
        self.tableView.setColumnWidth(0, 164)
        self.tableView.setColumnWidth(1, 163)
        self.tableView.setColumnWidth(2, 163)
        self.tableView.setColumnWidth(3, 163)
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)
        self.addUserButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.addUserButton.setStyleSheet("border-radius: 2px; \n"
                                            "font: 75 10pt \"Verdana\";\n"
                                            "color: rgb(0, 0, 0);\n"
                                            "background-color: rgb(240, 240, 240);\n"
                                            "border: 1px solid rgb(0, 0, 0);")
        self.addUserButton.setObjectName("addUserButton")
        self.addUserButton.clicked.connect(self.addUserRecord)
        self.gridLayout.addWidget(self.addUserButton, 1, 0, 1, 1)
        self.adminTabWidget.addTab(self.usersTab, "")
###############################################################################################
###############################################################################################
        self.lessonsTab = QtWidgets.QWidget()
        self.lessonsTab.setObjectName("lessonsTab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=self.lessonsTab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 811, 291))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.deleteLessonButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
        self.deleteLessonButton.setStyleSheet("border-radius: 2px; \n"
                                            "font: 75 10pt \"Verdana\";\n"
                                            "color: rgb(0, 0, 0);\n"
                                            "background-color: rgb(240, 240, 240);\n"
                                            "border: 1px solid rgb(0, 0, 0);")
        self.deleteLessonButton.setObjectName("deleteLessonButton")
        self.deleteLessonButton.clicked.connect(self.deleteLessonRecord)
        self.gridLayout_2.addWidget(self.deleteLessonButton, 2, 0, 1, 1)
        self.lessonTableModel = QtSql.QSqlTableModel(parent=self.gridLayoutWidget_2)
        self.lessonTableModel.setTable('lessons')
        self.lessonTableModel.setSort(0, QtCore.Qt.SortOrder.AscendingOrder)
        self.lessonTableModel.select()
        self.lessonTableModel.setHeaderData(0, QtCore.Qt.Orientation.Horizontal, 'Дата')
        self.lessonTableModel.setHeaderData(1, QtCore.Qt.Orientation.Horizontal, 'Ученик')
        self.lessonTableModel.setHeaderData(2, QtCore.Qt.Orientation.Horizontal, 'Класс')
        self.lessonTableModel.setHeaderData(3, QtCore.Qt.Orientation.Horizontal, 'Родитель')
        self.lessonTableModel.setHeaderData(4, QtCore.Qt.Orientation.Horizontal, 'Учитель')
        self.lessonTableModel.setHeaderData(5, QtCore.Qt.Orientation.Horizontal, 'Предмет')
        self.lessonTableModel.setHeaderData(6, QtCore.Qt.Orientation.Horizontal, 'Оценка')
        self.lessonTableModel.setHeaderData(7, QtCore.Qt.Orientation.Horizontal, 'Тема занятия')
        self.lessonTableModel.setHeaderData(8, QtCore.Qt.Orientation.Horizontal, 'Домашнее задание')
        self.tableView_2 = QtWidgets.QTableView(parent=self.gridLayoutWidget_2)
        self.tableView_2.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
        self.tableView_2.setObjectName("tableView_2")
        self.tableView_2.setModel(self.lessonTableModel)
        self.tableView_2.setGeometry(QtCore.QRect(0, 0, 150, 100))
        # self.tableView_2.setColumnWidth(0, 164)
        # self.tableView_2.setColumnWidth(1, 163)
        self.tableView_2.setColumnWidth(2, 50)
        self.tableView_2.setColumnWidth(3, 180)
        # self.tableView_2.setColumnWidth(4, 163)
        self.tableView_2.setColumnWidth(5, 180)
        self.tableView_2.setColumnWidth(6, 60)
        self.tableView_2.setColumnWidth(7, 500)
        self.tableView_2.setColumnWidth(8, 500)
        self.gridLayout_2.addWidget(self.tableView_2, 0, 0, 1, 1)
        self.addLessonButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
        self.addLessonButton.setStyleSheet("border-radius: 2px; \n"
                                         "font: 75 10pt \"Verdana\";\n"
                                         "color: rgb(0, 0, 0);\n"
                                         "background-color: rgb(240, 240, 240);\n"
                                         "border: 1px solid rgb(0, 0, 0);")
        self.addLessonButton.setObjectName("addLessonButton")
        self.addLessonButton.clicked.connect(self.addLessonRecord)
        self.gridLayout_2.addWidget(self.addLessonButton, 1, 0, 1, 1)
        self.adminTabWidget.addTab(self.lessonsTab, "")
###############################################################################################

        self.adminLabel = QtWidgets.QLabel(parent=adminDialog)
        self.adminLabel.setGeometry(QtCore.QRect(30, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.adminLabel.setFont(font)
        self.adminLabel.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 117, 176, 255), stop:1 rgba(0, 170, 255, 255));\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border: 1px solid rgb(0, 0, 0);\n"
                                      "border-radius: 5px;\n"
                                      "font: 12pt \"Verdana\";")
        self.adminLabel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.adminLabel.setLineWidth(1)
        self.adminLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.adminLabel.setObjectName("adminLabel")
        self.exitButton = QtWidgets.QPushButton(parent=adminDialog)
        self.exitButton.setGeometry(QtCore.QRect(660, 10, 221, 31))
        # self.exitButton.setGeometry(QtCore.QRect(360, 10, 221, 31))
        self.exitButton.setStyleSheet("border-radius: 5px; \n"
                                      "font: 75 12pt \"Verdana\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 117, 176, 255), stop:1 rgba(0, 170, 255, 255));\n"
                                      "border: 1px solid rgb(0, 0, 0);")
        self.exitButton.setObjectName("exitButton")

        self.retranslateUi(adminDialog)
        self.adminTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(adminDialog)

    def retranslateUi(self, adminDialog):
        _translate = QtCore.QCoreApplication.translate
        adminDialog.setWindowTitle(_translate("adminDialog", "Администратор"))
        self.deleteUserButton.setText(_translate("adminDialog", "Удалить пользователя"))
        self.addUserButton.setText(_translate("adminDialog", "Добавить пользователя"))
        self.adminTabWidget.setTabText(self.adminTabWidget.indexOf(self.usersTab),
                                       _translate("adminDialog", "Пользователи"))

        self.deleteLessonButton.setText(_translate("adminDialog", "Удалить Запись"))
        self.addLessonButton.setText(_translate("adminDialog", "Добавить Запись"))
        self.adminTabWidget.setTabText(self.adminTabWidget.indexOf(self.lessonsTab),
                                       _translate("adminDialog", "Занятия"))

        self.adminLabel.setText(_translate("adminDialog", "admin"))
        self.exitButton.setText(_translate("adminDialog", "Выйти из ученой записи"))

