import sqlite3

class Class():
    def __init__(self):
        self.classId
        self.name
        self.price


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
        classdict = {}
        for row in rows:
            classdict[row[0]] = [row[1], row[2]]
            print(row[0] + " - " + row[1] +  " - " + row[2] + '\n')
        
        classes = input("Select the classes that in the Train (1, 2, 3): ")
        classes = classes.split(', ')
        classesdict = {}
        for Class in classes:
            nSeats = int(input("Enter the number of Seats for the class " + classdict[Class][0] + "for the Train: "))
            classesdict[Class] = [classdict[Class], nSeats]
        conn.close()
        return classesdict