import sqlite3


def connectionDb():
    try:
        connection = sqlite3.connect('db/database.db')
        # print('----------------------------\nСоединение с БД установленно\n----------------------------')
        return connection
    except sqlite3.Error as er:
        pass
        # print(er)


def login(log, passwrd, textSignal, nextWindowSignal):
    connection = connectionDb()
    cursor = connection.cursor()


    cursor.execute(f'SELECT login, password, name, role  FROM users WHERE login="{log}";')
    value = cursor.fetchall()

    if value != [] and value[0][1] == passwrd:
        # textSignal.emit('Успешная авторизация')
        nextWindowSignal.emit(value[0][0], value[0][1],value[0][2], value[0][3])
    else:
        textSignal.emit('Проверьте правильность введенных данных')

    connection.close()



