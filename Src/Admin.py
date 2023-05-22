import sqlite3
from Train import Train
from Trip import Trip

class Admin:
    def __init__(self, admin_id=None):
        self.name = ""
        self.email = ""
        self.password = ""
        self.adminId = ""
        if admin_id is not None:
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            cursor.execute("SELECT adminId, name, email, password FROM admin WHERE adminId=?", (admin_id,))
            row = cursor.fetchone()
            if row:
                self.adminId = row[0]
                self.name = row[1]
                self.email = row[2]
                self.password = row[3]
            conn.close()

    def sign_up(self, name, email, password):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        # Check if email already exists in the Admin table
        cursor.execute('''SELECT email FROM Admin WHERE email = ?''', (email,))
        if cursor.fetchone():
            conn.close()
            raise ValueError("Email already exists!")

        # Insert a new admin into the Admin table
        cursor.execute('''INSERT INTO Admin (name, email, password) VALUES (?, ?, ?)''', (name, email, password))
        conn.commit()

        # Retrieve the adminId of the newly inserted row
        cursor.execute('''SELECT adminId FROM Admin WHERE email = ?''', (email,))
        admin_id = cursor.fetchone()
        if admin_id:
            self.adminId = admin_id[0]
            conn.close()
            return True
        else:
            conn.close()
            raise ValueError("Error occurred while retrieving adminId.")

    def sign_in(self, email, password):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        # Check if email exists in the Admin table
        cursor.execute('''SELECT adminId FROM Admin WHERE email = ?''', (email,))
        admin_id = cursor.fetchone()
        if not admin_id:
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
        if row:
            self.adminId = row[0]
            self.name = row[1]
            self.email = row[2]
            self.password = row[3]
        conn.close()
        return True

    def add_train(self, name, description, classes):
        train = Train()
        train.name = name
        train.description = description
        train.classes = classes
        train.adminId = self.adminId
        return train.addTrain()

    def update_train_class(self, trainId, classId, n_seats=None):
        train = Train(trainId)
        train.classes[classId][2] = n_seats
        train.editTrainClass(classId)
        return True

    def update_train(self, trainId, name=None, description=None):
        train = Train(trainId)
        if name:
            train.name = name
        if description:
            train.description = description
        train.editTrain()
        return True

    def add_trip(self, src, dest, departs, arrives, price, trainID):
        trip = Trip()
        trip.src = src
        trip.dest = dest
        trip.departs = departs
        trip.arrives = arrives
        trip.price = price
        trip.trainId = trainID
        trip.add_trip_to_database(self.adminId)

    def update_trip(self, trip_id, src=None, dest=None, departs=None, arrives=None, price=None, trainId=None):
        trip = Trip(trip_id)
        if src:
            trip.src = src
        if dest:
            trip.dest = dest
        if departs:
            trip.departs = departs
        if arrives:
            trip.arrives = arrives
        if price:
            trip.price = price
        if trainId:
            trip.trainId = trainId
        trip.update_trip_to_database()

    def update_name(self, name):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute('''UPDATE Admin SET name = ? WHERE adminId = ?''', (name, self.adminId))
        conn.commit()
        conn.close()
        return True 
    
    def update_email(self, email):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute('''UPDATE Admin SET email = ? WHERE adminId = ?''', (email, self.adminId))
        conn.commit()
        conn.close()
        return True
    
    def update_password(self, new_password):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute('''UPDATE Admin SET password = ? WHERE adminId = ?''', (new_password, self.adminId))
        conn.commit()
        conn.close()
        return True
    
    def update_admin(self,email,name,new_password):
        if self.update_email(email):
                if self.update_name(name):
                    if self.update_password(new_password):
                        return True
        return False