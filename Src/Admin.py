import sqlite3
from Train import Train
from Trip import Trip

class Admin:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.password = ""
        self.adminId = ""

    def signUp(self, name, email, password):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        # Check if email already exists in the Admin table
        cursor.execute('''SELECT email FROM Admin WHERE email = ?''', (email,))
        if cursor.fetchone() is not None:
            conn.close()
            raise ValueError("Email already exists!")

        # Insert a new admin into the Admin table
        cursor.execute('''INSERT INTO Admin (name, email, password) VALUES (?, ?, ?)''', (name, email, password))
        conn.commit()

        # Retrieve the adminId of the newly inserted row
        cursor.execute('''SELECT adminId FROM Admin WHERE email = ?''', (email,))
        admin_id = cursor.fetchone()
        if admin_id is not None:
            self.adminId = admin_id[0]
            conn.close()
            return True
        else:
            conn.close()
            raise ValueError("Error occurred while retrieving adminId.")

    def signIn(self, email, password):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        # Check if email exists in the Admin table
        cursor.execute('''SELECT adminId FROM Admin WHERE email = ?''', (email,))
        admin_id = cursor.fetchone()
        if admin_id is None:
            conn.close()
            return False

        admin_id = admin_id[0]
        # Check if the provided password matches the one in the Admin table
        cursor.execute('''SELECT password FROM Admin WHERE adminId = ?''', (admin_id,))
        stored_password = cursor.fetchone()[0]
        if password != stored_password:
            conn.close()
            raise ValueError("Invalid password.")

        # Retrieve the admin details
        cursor.execute('''SELECT adminId, name, email, password FROM Admin WHERE adminId = ?''', (admin_id,))
        row = cursor.fetchone()
        self.adminId = row[0]
        self.name = row[1]
        self.email = row[2]
        self.password = row[3]

        conn.close()
        return True


    def addTrain(self, name, description, classes):
        train = Train()
        train.name = name
        train.description = description
        train.classes = classes
        train.adminId = self.adminId
        train.addTrain()
        return
    
    def editTrainClass(self,trainId, classId,n_seats=None):
        train = Train(trainId)
        train.classes[classId][1] = n_seats
        train.editTrainClass(classId)
        return  


    def editTrain(self, trainId, name=None, description=None):
        train = Train(trainId)
        if name:
            train.name = name
        if description:
            train.description = description
        train.editTrain()
        return True
    
    def add_trip(self, src, dist, departs, arrives, price):
        trip = Trip()
        trip.src = src
        trip.dist = dist
        trip.departs = departs
        trip.arrives = arrives
        trip.price = price
        trip.add_trip_to_database()

    def update_trip(self, trip_id, src, dist, departs, arrives, price):
        trip = Trip()
        trip.src = src
        trip.dist = dist
        trip.departs = departs
        trip.arrives = arrives
        trip.price = price
        trip.update_trip_to_database(trip_id)

    def update_name(self, name):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute('''UPDATE Admin SET name = ? WHERE adminId = ?''', (name, self.adminId))
        conn.commit()
        conn.close()

    def update_email(self, email):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute('''UPDATE Admin SET email = ? WHERE adminId = ?''', (email, self.adminId))
        conn.commit()
        conn.close()

    def update_password(self, old_password, new_password):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute('''SELECT password FROM Admin WHERE adminId = ?''', (self.adminId,))
        stored_password = cursor.fetchone()
        if stored_password is None or stored_password[0] != old_password:
            conn.close()
            raise ValueError("Invalid old password.")

        cursor.execute('''UPDATE Admin SET password = ? WHERE adminId = ?''', (new_password, self.adminId))
        conn.commit()
        conn.close()
