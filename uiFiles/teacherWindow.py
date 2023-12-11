from PyQt6 import QtCore, QtGui, QtWidgets, QtSql
import dbHandler


class Ui_teacher_window_dialog(object):

    def addLessonRecord(self):
        self.lessonTableModel.insertRow(self.lessonTableModel.rowCount())

    def deleteLessonRecord(self):
        self.lessonTableModel.removeRow(self.tableView.currentIndex().row())
        self.lessonTableModel.select()
    def setupUi(self, teacher_window_dialog):
        teacher_window_dialog.setObjectName("teacher_window_dialog")
        teacher_window_dialog.resize(961, 561)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(teacher_window_dialog.sizePolicy().hasHeightForWidth())
        teacher_window_dialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        teacher_window_dialog.setFont(font)
        teacher_window_dialog.setStyleSheet("font: 12pt \"Verdana\";")
        self.pushButton = QtWidgets.QPushButton(parent=teacher_window_dialog)
        self.pushButton.setGeometry(QtCore.QRect(740, 15, 191, 31))
        self.pushButton.setStyleSheet("border-radius: 5px; \n"
                                      "font: 75 12pt \"Verdana\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 117, 176, 255), stop:1 rgba(0, 170, 255, 255));\n"
                                      "border: 1px solid rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.class_frame = QtWidgets.QFrame(parent=teacher_window_dialog)
        self.class_frame.setGeometry(QtCore.QRect(460, 95, 141, 31))
        self.class_frame.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.class_frame.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 117, 176, 255), stop:1 rgba(0, 170, 255, 255));\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border: 1px solid rgb(0, 0, 0);\n"
                                       "border-radius: 5px;")
        self.class_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.class_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.class_frame.setObjectName("class_frame")
        self.class_label = QtWidgets.QLabel(parent=self.class_frame)
        self.class_label.setGeometry(QtCore.QRect(6, 5, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.class_label.setFont(font)
        self.class_label.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 117, 176, 255), stop:1 rgba(0, 170, 255, 255));\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border: 1px qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 117, 176, 255), stop:1 rgba(0, 170, 255, 255));\n"
                                       "")
        self.class_label.setObjectName("class_label")
        self.class_combobox = QtWidgets.QComboBox(parent=self.class_frame)
        self.class_combobox.setGeometry(QtCore.QRect(60, 5, 71, 22))
        self.class_combobox.setObjectName("class_combobox")
        self.class_combobox.activated.connect(self.set_class_filter)
        self.teacher_name = QtWidgets.QLabel(parent=teacher_window_dialog)
        self.teacher_name.setGeometry(QtCore.QRect(30, 15, 411, 31))
        self.teacher_name.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 117, 176, 255), stop:1 rgba(0, 170, 255, 255));\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border: 1px solid rgb(0, 0, 0);\n"
                                        "border-radius: 5px;")
        self.teacher_name.setObjectName("teacher_name")
        self.subject_frame = QtWidgets.QFrame(parent=teacher_window_dialog)
        self.subject_frame.setGeometry(QtCore.QRect(30, 55, 411, 31))
        self.subject_frame.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.subject_frame.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 117, 176, 255), stop:1 rgba(0, 170, 255, 255));\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border: 1px solid rgb(0, 0, 0);\n"
                                         "border-radius: 5px;")
        self.subject_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.subject_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.subject_frame.setObjectName("subject_frame")
        self.subject_label = QtWidgets.QLabel(parent=self.subject_frame)
        self.subject_label.setGeometry(QtCore.QRect(10, 5, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.subject_label.setFont(font)
        self.subject_label.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 117, 176, 255), stop:1 rgba(0, 170, 255, 255));\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border: 1px qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 117, 176, 255), stop:1 rgba(0, 170, 255, 255));\n"
                                         "")
        self.subject_label.setObjectName("subject_label")
        self.subject_combobox = QtWidgets.QComboBox(parent=self.subject_frame)
        self.subject_combobox.setGeometry(QtCore.QRect(90, 5, 311, 22))
        self.subject_combobox.setObjectName("subject_combobox")
        self.subject_combobox.activated.connect(self.set_subject_filter)
        self.dateEdit = QtWidgets.QDateEdit(QtCore.QDate(2023, 12, 1), parent=teacher_window_dialog)
        self.dateEdit.setGeometry(QtCore.QRect(460, 55, 141, 31))
        self.dateEdit.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.dateEdit.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.PreventContextMenu)
        self.dateEdit.setAcceptDrops(False)
        self.dateEdit.setStyleSheet("border-radius: 5px; \n"
                                    "color: rgb(255, 255, 255);\n"
                                    "background-color: qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 117, 176, 255), stop:1 rgba(0, 170, 255, 255));\n"
                                    "border: 1px solid rgb(0, 0, 0);")
        self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.Section.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(0)
        self.dateEdit.setTimeSpec(QtCore.Qt.TimeSpec.LocalTime)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.dateChanged.connect(self.set_date_filter)
        self.student_frame = QtWidgets.QFrame(parent=teacher_window_dialog)
        self.student_frame.setGeometry(QtCore.QRect(30, 95, 411, 31))
        self.student_frame.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.student_frame.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 117, 176, 255), stop:1 rgba(0, 170, 255, 255));\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border: 1px solid rgb(0, 0, 0);\n"
                                         "border-radius: 5px;")
        self.student_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.student_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.student_frame.setObjectName("student_frame")
        self.student_label = QtWidgets.QLabel(parent=self.student_frame)
        self.student_label.setGeometry(QtCore.QRect(10, 5, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.student_label.setFont(font)
        self.student_label.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 117, 176, 255), stop:1 rgba(0, 170, 255, 255));\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border: 1px qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 117, 176, 255), stop:1 rgba(0, 170, 255, 255));\n"
                                         "")
        self.student_label.setObjectName("student_label")
        self.student_combobox = QtWidgets.QComboBox(parent=self.student_frame)
        self.student_combobox.setGeometry(QtCore.QRect(90, 5, 311, 22))
        self.student_combobox.setObjectName("student_combobox")
        self.student_combobox.activated.connect(self.set_student_filter)

        self.log_table_widget = QtWidgets.QTableWidget(parent=teacher_window_dialog)
        self.log_table_widget.setGeometry(QtCore.QRect(30, 140, 901, 391))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.log_table_widget.setFont(font)
        self.log_table_widget.setStyleSheet("font: 75 10pt \"Verdana\";")
        self.log_table_widget.setObjectName("log_table_widget")
        self.lessonTableModel = QtSql.QSqlTableModel(parent=self.log_table_widget)
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
        self.tableView = QtWidgets.QTableView(parent=self.log_table_widget)
        self.tableView.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
        self.tableView.setObjectName("tableView")
        self.tableView.setModel(self.lessonTableModel)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 901, 391))
        self.tableView.setColumnWidth(2, 100)
        self.tableView.setColumnWidth(3, 190)
        self.tableView.setColumnWidth(5, 190)
        self.tableView.setColumnWidth(6, 100)

        self.deleteLessonButton = QtWidgets.QPushButton(parent=teacher_window_dialog)
        self.deleteLessonButton.setGeometry(QtCore.QRect(740, 95, 191, 31))
        self.deleteLessonButton.setStyleSheet("border-radius: 2px; \n"
                                              "font: 75 10pt \"Verdana\";\n"
                                              "color: rgb(0, 0, 0);\n"
                                              "background-color: rgb(240, 240, 240);\n"
                                              "border: 1px solid rgb(0, 0, 0);")
        self.deleteLessonButton.setObjectName("deleteLessonButton")
        self.deleteLessonButton.clicked.connect(self.deleteLessonRecord)

        self.addLessonButton = QtWidgets.QPushButton(parent=teacher_window_dialog)
        self.addLessonButton.setGeometry(QtCore.QRect(740, 55, 191, 31))
        self.addLessonButton.setStyleSheet("border-radius: 2px; \n"
                                              "font: 75 10pt \"Verdana\";\n"
                                              "color: rgb(0, 0, 0);\n"
                                              "background-color: rgb(240, 240, 240);\n"
                                              "border: 1px solid rgb(0, 0, 0);")
        self.addLessonButton.setObjectName("addLessonButton")
        self.addLessonButton.clicked.connect(self.addLessonRecord)

        self.clearFilterButton = QtWidgets.QPushButton(parent=teacher_window_dialog)
        self.clearFilterButton.setGeometry(QtCore.QRect(460, 15, 141, 31))
        self.clearFilterButton.setStyleSheet("border-radius: 2px; \n"
                                              "font: 75 10pt \"Verdana\";\n"
                                              "color: rgb(0, 0, 0);\n"
                                              "background-color: rgb(240, 240, 240);\n"
                                              "border: 1px solid rgb(0, 0, 0);")
        self.clearFilterButton.setObjectName("clearFilterButton")
        self.clearFilterButton.clicked.connect(self.clearFilter)

        self.retranslateUi(teacher_window_dialog)
        QtCore.QMetaObject.connectSlotsByName(teacher_window_dialog)

    def retranslateUi(self, teacher_window_dialog):
        _translate = QtCore.QCoreApplication.translate
        teacher_window_dialog.setWindowTitle(_translate("teacher_window_dialog", "Учитель"))
        self.pushButton.setText(_translate("teacher_window_dialog", "Сменить профиль"))
        self.class_label.setText(_translate("teacher_window_dialog", "Класс"))
        self.teacher_name.setText(_translate("teacher_window_dialog", "ФИО учителя"))
        self.subject_label.setText(_translate("teacher_window_dialog", "Предмет"))
        self.student_label.setText(_translate("teacher_window_dialog", "Ученик"))

        self.deleteLessonButton.setText(_translate("teacher_window_dialog", "Удалить Запись"))
        self.addLessonButton.setText(_translate("teacher_window_dialog", "Добавить Запись"))
        self.clearFilterButton.setText(_translate("teacher_window_dialog", "Сбросить фильтр"))

    def select_teacher_info(self, name):
        connection = dbHandler.connectionDb()
        cursor = connection.cursor()

        teacher_subjects = []
        teacher_students = []
        teacher_classes = []

        cursor.execute(f'''
            SELECT DISTINCT subject
            FROM lessons
            WHERE teacher = "{name}"
        ;''')
        value = cursor.fetchall()
        for i in value:
            teacher_subjects.append(i[0])

        cursor.execute(f'''
                    SELECT DISTINCT student
                    FROM lessons
                    WHERE teacher = "{name}"
                ;''')
        value = cursor.fetchall()
        for i in value:
            teacher_students.append(i[0])

        cursor.execute(f'''
                            SELECT DISTINCT class
                            FROM lessons
                            WHERE teacher = "{name}"
                        ;''')
        value = cursor.fetchall()
        for i in value:
            teacher_classes.append(i[0])

        self.teacher_name.setText(name)
        self.subject_combobox.addItems(teacher_subjects)
        self.student_combobox.addItems(teacher_students)
        self.class_combobox.addItems(teacher_classes)

    def clearFilter(self):
        self.lessonTableModel.setFilter(f'teacher = "{self.teacher_name.text()}"')
        self.lessonTableModel.select()

    def set_date_filter(self):
        self.lessonTableModel.setFilter(f'''
            teacher = "{self.teacher_name.text()}"
            AND date = "{self.dateEdit.date().toPyDate()}"
            ''')
        self.lessonTableModel.select()

    def set_subject_filter(self):
        self.lessonTableModel.setFilter(f'''
            teacher = "{self.teacher_name.text()}"
            AND subject = "{self.subject_combobox.currentText()}"
            ''')
        self.lessonTableModel.select()

    def set_student_filter(self):
        self.lessonTableModel.setFilter(f'''
            teacher = "{self.teacher_name.text()}"
            AND student = "{self.student_combobox.currentText()}"
            ''')
        self.lessonTableModel.select()

    def set_class_filter(self):
        self.lessonTableModel.setFilter(f'''
            teacher = "{self.teacher_name.text()}"
            AND class = "{self.class_combobox.currentText()}"
            ''')
        self.lessonTableModel.select()

    # def show_table(self):
    #     current_name = self.teacher_name.text()
    #     current_subject = self.subject_combobox.currentText()
    #     current_student = self.student_combobox.currentText()
    #     current_class = self.class_combobox.currentText()
    #     current_date = self.dateEdit.date().toPyDate()
    #
    #     self.lessonTableModel.setFilter(f'''teacher = "{current_name}"'
    #                                     AND subject = "{current_subject}"'
    #                                     AND student = "{current_student}"'
    #                                     AND class = "{current_class}"'
    #                                     AND date = "{current_date}"''')
    #     self.lessonTableModel.select()
