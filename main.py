import sys
from PyQt6.QtWidgets import (
    QApplication,
    QDialog
)
from uiFiles.authWindow import Ui_AuthWindow
from uiFiles.adminWindow import Ui_AdminWindow
from uiFiles.teacherWindow import Ui_TeacherWindow
from uiFiles.studentWindow import Ui_StudentWindow
import dbHandler


def openNextWindow(login):
    if login == 'admin':
        uiAuthWindow.message('Вошел Admin')

        uiAuthWindow.loginLineEdit.clear()
        uiAuthWindow.passwordLineEdit.clear()

        dialogAuthWindow.close()
        dialogAdminWindow.show()

    else:
        connection = dbHandler.connectionDb()
        cursor = connection.cursor()

        cursor.execute(f'''
        SELECT teacher_name FROM users a INNER JOIN teachers b ON a.teacher_id = b.teacher_id WHERE a.login = "{login}"
        ;''')
        value = cursor.fetchall()

        if value != []:
            uiAuthWindow.message('Вошел учитель')

            dialogAuthWindow.close()
            dialogTeacherWindow.show()


        else:
            uiAuthWindow.message('Вошел Родитель')

            dialogAuthWindow.close()
            dialogStudentWindow.show()


def returnAuthWindow():
    uiAuthWindow.message('Возвращаемся в окно авторизации')
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
    uiTeacherWindow = Ui_TeacherWindow()
    uiTeacherWindow.setupUi(dialogTeacherWindow)

    # Окно ученика
    dialogStudentWindow = QDialog()
    uiStudentWindow = Ui_StudentWindow()
    uiStudentWindow.setupUi(dialogStudentWindow)


    # Нажатие кнопки Авторизоваться
    uiAuthWindow.authButton.clicked.connect(uiAuthWindow.auth)
    # Очищает EditLine'ы
    uiAuthWindow.authButton.clicked.connect(uiAuthWindow.loginLineEdit.clear)
    uiAuthWindow.authButton.clicked.connect(uiAuthWindow.passwordLineEdit.clear)
    # Открытие следующего окна (любого из окон)
    uiAuthWindow.checkDbThread.nextWindowSignal.connect(openNextWindow)
    # Нажатие кнопки Зарегистрироваться
    uiAuthWindow.registerButton.clicked.connect(uiAuthWindow.reg)
    # Очищает EditLine'ы
    uiAuthWindow.registerButton.clicked.connect(uiAuthWindow.loginLineEdit.clear)
    uiAuthWindow.registerButton.clicked.connect(uiAuthWindow.passwordLineEdit.clear)
    # Нажатие кнопки Выйти из админа (Окно админа)
    uiAdminWindow.exitButton.clicked.connect(returnAuthWindow)
    # Нажатие кнопки Выйти из дневника (Окно ученика/ дневник/ родительское)
    uiStudentWindow.pushButton.clicked.connect(returnAuthWindow)
    # Нажатие кнопки Выйти из журнала (Окно учителя)
    uiTeacherWindow.pushButton.clicked.connect(returnAuthWindow)









    sys.exit(app.exec())
