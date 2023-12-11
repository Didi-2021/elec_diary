import sys, os
from PyQt6.QtWidgets import (
    QApplication,
    QDialog
)
from PyQt6 import QtSql, QtCore
from uiFiles.authWindow import Ui_AuthWindow
from uiFiles.adminWindow import Ui_AdminWindow
from uiFiles.teacherWindow import Ui_teacher_window_dialog
from uiFiles.studentWindow import Ui_StudentWindow
import dbHandler

# basedir = os.path.dirname(__file__)

def openNextWindow(login, password, name, role):
    if login == 'а':
        # uiAuthWindow.message('Вошел Админ')

        uiAuthWindow.lineEdit.clear()
        uiAuthWindow.lineEdit_2.clear()

        dialogAuthWindow.close()
        dialogAdminWindow.show()

    else:
        # connection = dbHandler.connectionDb()
        # cursor = connection.cursor()
        #
        # cursor.execute(f'''
        #     SELECT login, password, name
        #     FROM users
        #     WHERE login = "{login}"
        # ;''')
        # value = cursor.fetchall()

        if role == 'учитель':
            # uiAuthWindow.message('Вошел учитель')

            dialogAuthWindow.close()
            uiTeacherWindow.select_teacher_info(name)
            uiTeacherWindow.lessonTableModel.setFilter(f'teacher = "{name}"')

            dialogTeacherWindow.show()

        else:
            # uiAuthWindow.message('Вошел Родитель')

            dialogAuthWindow.close()
            uiStudentWindow.select_student_info(name)
            uiStudentWindow.lessonTableModel.setFilter(f'student = "{name}"')

            dialogStudentWindow.show()


def returnAuthWindow():
    # uiAuthWindow.message('Возвращаемся в окно авторизации')
    dialogAdminWindow.close()
    dialogStudentWindow.close()
    dialogTeacherWindow.close()
    dialogAuthWindow.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Окно авторизации
    dialogAuthWindow = QDialog()
    uiAuthWindow = Ui_AuthWindow()
    uiAuthWindow.setupUi(dialogAuthWindow)
    dialogAuthWindow.show()

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
