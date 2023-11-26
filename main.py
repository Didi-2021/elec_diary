import sys
from PyQt6.QtWidgets import (
    QApplication,
    QDialog
)
from uiFiles.authWindow import Ui_AuthWindow
import dbHandler


def openNextWindow(login):
    if login == 'admin':
        uiAuthWindow.message('Вошел Admin')
    else:
        connection = dbHandler.connectionDb()
        cursor = connection.cursor()

        cursor.execute(f'''
        SELECT teacher_name FROM users a INNER JOIN teachers b ON a.teacher_id = b.teacher_id WHERE a.login = "{login}"
        ;''')
        value = cursor.fetchall()

        if value != []:
            uiAuthWindow.message('Вошел учитель')
        else:
            uiAuthWindow.message('Вошел Родитель')



def openAdminWindow():
    print('open Admin Window')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialogAuthWindow = QDialog()
    uiAuthWindow = Ui_AuthWindow()
    uiAuthWindow.setupUi(dialogAuthWindow)

    dialogAuthWindow.show()

    uiAuthWindow.authButton.clicked.connect(uiAuthWindow.auth)
    uiAuthWindow.checkDbThread.nextWindowSignal.connect(openNextWindow)
    uiAuthWindow.registerButton.clicked.connect(uiAuthWindow.reg)

    sys.exit(app.exec())
