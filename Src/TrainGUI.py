import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3
from Train import Train 
from Class import Class
from Admin import Admin

def enter_seats(class_name, root = None):
    seats = tk.simpledialog.askinteger("Enter Seats", f"Enter the number of seats for {class_name}", parent=root)
    return seats

class AddTrain:
    def __init__(self, parent, adminId):
        self.admin = Admin(adminId)
        self.root = tk.Toplevel(parent)
        self.root.title("Add Train")
        self.root.geometry('1000x600+280+100')
        self.root.configure(bg="black")

        self.name_label = tk.Label(self.root, text="Name:", bg="black", fg="white")
        self.name_label.pack(pady=10)

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5)

        self.details_label = tk.Label(self.root, text="Details:", bg="black", fg="white")
        self.details_label.pack(pady=10)

        self.details_entry = tk.Entry(self.root)
        self.details_entry.pack(pady=5)

        self.class_label = tk.Label(self.root, text="Classes:", bg="black", fg="white")
        self.class_label.pack(pady=10)

        self.class_listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE, bg="black", fg="white")
        self.class_listbox.pack(pady=5)

        self.add_train_button = tk.Button(self.root, text="Add Train", bg="red", fg="white", command=self.add_train)
        self.add_train_button.pack(pady=10)

        self.populate_class_list()
        self.root.mainloop()

    def populate_class_list(self):
        classes = Class()
        classes = classes.getClasses()
        for class_data in classes:
            self.class_listbox.insert(tk.END, f"{class_data[1]} (${class_data[2]})")

    def add_train(self):
        name = self.name_entry.get()
        details = self.details_entry.get()
        selected_indices = self.class_listbox.curselection()

        if not name or not details or not selected_indices:
            messagebox.showerror("Error", "Please enter all required information")
            return

        classes = Class()
        classes = classes.getClasses()
        selected_classes = [classes[i] for i in selected_indices]

        classes = {}

        for class_data in selected_classes:
            class_id = class_data[0]
            class_name = class_data[1]
            class_price = class_data[2]

            n_seats = enter_seats(class_name, self.root)

            classes[class_id] = [class_name, class_price, n_seats]

        success = self.admin.add_train(name, details, classes)

        if success:
            messagebox.showinfo("Success", "Train added successfully")
            self.name_entry.delete(0, tk.END)
            self.details_entry.delete(0, tk.END)
            self.class_listbox.selection_clear(0, tk.END)
        else:
            messagebox.showerror("Error", "Error adding train")

class EditTrain:
    def __init__(self, adminId):
        self.admin = Admin(adminId)
        selected_train_index = self.select_train()
        while selected_train_index == -1:
            selected_train_index = self.select_train()

        if selected_train_index == None:
            return

        self.train = Train(selected_train_index)

        edit_choice = self.choose_edit_option()
        
        if edit_choice == None:
            return

        while edit_choice != 1 and edit_choice != 2 and edit_choice != None:
            messagebox.showerror("Error", "Your selected index does not exist")
            edit_choice = self.choose_edit_option()

        if edit_choice == 1:
            self.edit_train_details()
        elif edit_choice == 2:
            self.edit_train_classes()

    def select_train(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute('SELECT trainId, name FROM Train')
        rows = cursor.fetchall()
        conn.close()

        train_names = [f"{row[0]} - {row[1]}" for row in rows]
        prompt = "\n".join(train_names)
        selected_index = simpledialog.askinteger("Select Train", f"Select a train:\n{prompt}", minvalue=1,)
        if selected_index == None:
            return None
        
        for ids in rows:
            if selected_index == int(ids[0]):
                return selected_index
                
        messagebox.showerror("Error", "Your selected index does not exist")
        return -1

    def choose_edit_option(self):
        return simpledialog.askinteger("Edit Train", "What would you like to edit?\n\n1. Train Details\n2. Train Classes")

    def edit_train_details(self):
        new_name = simpledialog.askstring("Edit Train Details", "Enter new train name:", initialvalue=self.train.name)
        new_details = simpledialog.askstring("Edit Train Details", "Enter new train details:", initialvalue=self.train.description)

        if new_name and new_details:
            self.train.name = new_name
            self.train.description = new_details
            self.admin.update_train(self.train.trainId, self.train.name, self.train.description)
            messagebox.showinfo("Success", "Train details edited successfully")
        else:
            messagebox.showerror("Error", "Please enter valid train details")

    def edit_train_classes(self):
        selected_class_index = self.select_train_class()
        while selected_class_index == -1:
            selected_class_index = self.select_train_class()
        
        if selected_class_index == None:
            return

        new_seats = enter_seats(self.train.classes[selected_class_index][0])
        if new_seats is None:
            return

        self.admin.update_train_class(self.train.trainId, selected_class_index, new_seats)
        messagebox.showinfo("Success", "Train class edited successfully")

    def select_train_class(self):
        class_names = [f"{class_id} - {self.train.classes[class_id][0]} Number of Seats: {self.train.classes[class_id][2]}" for class_id in self.train.classes]
        prompt = "\n".join(class_names)
        selected_index = simpledialog.askinteger("Select Train Class", f"Select a class to edit:\n{prompt}", minvalue=1,)
        if selected_index == None:
            return None
        for ids in self.train.classes:
            if selected_index == int(ids):
                return selected_index
                
        messagebox.showerror("Error", "Your selected index does not exist")
        return -1



