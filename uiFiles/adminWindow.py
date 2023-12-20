from PyQt6 import QtCore, QtGui, QtWidgets, QtSql


class Ui_AdminWindow(object):
    def addUserRecord(self):
        self.usersTableModel.insertRow(self.usersTableModel.rowCount())

    def deleteUserRecord(self):
        self.usersTableModel.removeRow(self.tableView.currentIndex().row())
        self.usersTableModel.select()

    def saveRecord(self):
        self.usersTableModel.submitAll()

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
        # self.usersTableModel.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnManualSubmit)
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
        self.exitButton.setStyleSheet("border-radius: 5px; \n"
                                      "font: 75 12pt \"Verdana\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 117, 176, 255), stop:1 rgba(0, 170, 255, 255));\n"
                                      "border: 1px solid rgb(0, 0, 0);")
        self.exitButton.setObjectName("exitButton")

        self.saveButton = QtWidgets.QPushButton(parent=adminDialog)
        self.saveButton.setGeometry(QtCore.QRect(480, 10, 151, 31))
        self.saveButton.setStyleSheet("border-radius: 2px; \n"
                                      "font: 75 10pt \"Verdana\";\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "background-color: rgb(240, 240, 240);\n"
                                      "border: 1px solid rgb(0, 0, 0);")
        self.saveButton.setObjectName("saveButton")
        self.saveButton.clicked.connect(self.saveRecord)

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

        self.adminLabel.setText(_translate("adminDialog", "admin"))
        self.exitButton.setText(_translate("adminDialog", "Выйти из ученой записи"))
        self.saveButton.setText(_translate("adminDialog", "Сохранить запись"))

