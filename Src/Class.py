import sqlite3


# conn = sqlite3.connect('db.sqlite3')
# c = conn.cursor()

# c.execute('INSERT INTO Class (ClassName, price) VALUES(?, ?)',("Class A",  700))
# conn.commit()
# c.execute('INSERT INTO Class (ClassName, price) VALUES(?,?)',("Class B",  600))
# conn.commit()
# c.execute('INSERT INTO Class (ClassName, price) VALUES(?,?)',("Class C",  500))
# conn.commit()
# conn.close()

class Class():
    def __init__(self):
        self.classId = None
        self.name = None
        self.price = None


    def addClass(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        class_name = input('Class name: ')
        price = int(input('Price :'))
        cursor.execute(f'SELECT className FROM Class WHERE name = "{class_name}"')
        if cursor.fetchone() == None:
            cursor.execute(f'INSERT INTO Class (className, price) VALUES ("{class_name}", "{price}")')
            conn.commit()
        else:
            print('Class already exists\n')


    def getClasses(self):
        conn = sqlite3.connect('db.sqlite3')  
        cursor = conn.cursor()
        cursor.execute('SELECT classId, className, price FROM Class')
        rows = cursor.fetchall()
        conn.close()
        return rows