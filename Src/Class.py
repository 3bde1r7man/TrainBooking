import sqlite3

def addClass():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    class_name = input('Class name: ')
    cursor.execute(f'SELECT name FROM Class WHERE name = "{class_name}"')
    if cursor.fetchone() == None:
        cursor.execute(f'INSERT INTO Class (name) VALUES ("{class_name}")')
        conn.commit()
    else:
        print('Class already exists')