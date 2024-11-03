import sqlite3


def data():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY AUTOINCREMENT,
     first_name text,
     last_name text,
     class_code text,
     group_name text,
     saz text,
     master_name text)''')

    connection.commit()
    connection.close()


def add_user(first_name, last_name, class_code, group_name, saz, master_name):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO user VALUES(NULL, ?,?,?,?,?,?)",
                   (first_name, last_name, class_code, group_name, saz, master_name))
    connection.commit()
    connection.close()


def delete_user(first_name):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM user WHERE first_name = ?", (first_name,))
    connection.commit()
    connection.close()


def search_user(first_name='', last_name='', class_code='', group_name='', saz='', master_name=''):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user WHERE firs_name=? or last_name=? or class_code=? or group_name=? or saz=? or master_name=?",
                   (first_name, last_name, class_code, group_name, saz, master_name))
    rows = cursor.fetchall()
    for row in rows:
        return row
    connection.close()


def update_user(first_name, last_name, class_code, group_name, saz, master_name):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE user SET first_name=?, last_name=?, class_code=?, group_name=?, saz=?, master_name=?",
                   (first_name, last_name, class_code, group_name, saz, master_name))

    connection.commit()
    connection.close()


def view_users():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user")
    rows = cursor.fetchall()
    for row in rows:
        return row
    connection.close()










