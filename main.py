import sys
from PyQt6.QtWidgets import (
    QApplication,
    QDialog
)
from PyQt6 import QtSql
from uiFiles.authWindow import Ui_AuthWindow
from uiFiles.adminWindow import Ui_AdminWindow
from uiFiles.teacherWindow import Ui_teacher_window_dialog
from uiFiles.studentWindow import Ui_StudentWindow
from uiFiles.welcomeWindow import Ui_welcome_window_dialog
from uiFiles.aboutUsWindow import Ui_about_us_window_dialog


def openNextWindow(login, password, name, role):
    if login == 'а':
        uiAuthWindow.lineEdit.clear()
        uiAuthWindow.lineEdit_2.clear()
        dialogAdminWindow.show()
        dialogAuthWindow.close()
    else:
        if role == 'учитель':
            uiTeacherWindow.select_teacher_info(name)
            uiTeacherWindow.lessonTableModel.setFilter(f'teacher = "{name}"')
            dialogTeacherWindow.show()
            dialogAuthWindow.close()
        else:
            uiStudentWindow.select_student_info(name)
            uiStudentWindow.lessonTableModel.setFilter(f'student = "{name}"')
            dialogStudentWindow.show()
            dialogAuthWindow.close()


def open_about_us_window():
    # dialogWelcomeWindow.close()
    dialogAboutUsWindow.show()


def open_auth_window():
    dialogWelcomeWindow.close()
    dialogAuthWindow.show()


def returnAuthWindow():
    dialogAuthWindow.show()
    dialogAdminWindow.close()
    dialogStudentWindow.close()
    dialogTeacherWindow.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    conn = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    conn.setDatabaseName('db/database.db')
    conn.open()

    # Окно приветствия
    dialogWelcomeWindow = QDialog()
    uiWelcomeWindowDialog = Ui_welcome_window_dialog()
    uiWelcomeWindowDialog.setupUi(dialogWelcomeWindow)
    uiWelcomeWindowDialog.about_us_button.clicked.connect(open_about_us_window)
    uiWelcomeWindowDialog.login_button.clicked.connect(open_auth_window)
    dialogWelcomeWindow.show()

    # Окно О нас
    dialogAboutUsWindow = QDialog()
    uiAboutUsWindow = Ui_about_us_window_dialog()
    uiAboutUsWindow.setupUi(dialogAboutUsWindow)

    # Окно авторизации
    dialogAuthWindow = QDialog()
    uiAuthWindow = Ui_AuthWindow()
    uiAuthWindow.setupUi(dialogAuthWindow)

    # Окно админа
    dialogAdminWindow = QDialog()
    uiAdminWindow = Ui_AdminWindow()
    uiAdminWindow.setupUi(dialogAdminWindow)

    # Окно учителя
    dialogTeacherWindow = QDialog()
    uiTeacherWindow = Ui_teacher_window_dialog()
    uiTeacherWindow.setupUi(dialogTeacherWindow)

    # Окно ученика
    dialogStudentWindow = QDialog()
    uiStudentWindow = Ui_StudentWindow()
    uiStudentWindow.setupUi(dialogStudentWindow)


    # Нажатие кнопки Авторизоваться
    uiAuthWindow.pushButton.clicked.connect(uiAuthWindow.auth)
    # Очищает EditLine'ы
    uiAuthWindow.pushButton.clicked.connect(uiAuthWindow.lineEdit.clear)
    uiAuthWindow.pushButton.clicked.connect(uiAuthWindow.lineEdit_2.clear)
    uiAuthWindow.pushButton_2.clicked.connect(uiAuthWindow.lineEdit.clear)
    uiAuthWindow.pushButton_2.clicked.connect(uiAuthWindow.lineEdit_2.clear)
    # Открытие следующего окна (любого из окон)
    uiAuthWindow.checkDbThread.nextWindowSignal.connect(openNextWindow)
    # Нажатие кнопки Зарегистрироваться
    uiAuthWindow.pushButton_2.clicked.connect(uiAuthWindow.reg)

    # Нажатие кнопки Выйти из админа (Окно админа)
    uiAdminWindow.exitButton.clicked.connect(returnAuthWindow)

    # Нажатие кнопки Выйти из дневника (Окно ученика/ дневник/ родительское)
    uiStudentWindow.pushButton.clicked.connect(returnAuthWindow)

    # Нажатие кнопки Выйти из журнала (Окно учителя)
    uiTeacherWindow.pushButton.clicked.connect(returnAuthWindow)

    sys.exit(app.exec())
