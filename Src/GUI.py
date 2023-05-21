import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3
from Train import Train 
from Class import Class

# Create the main Tkinter window

class TrainManagerGUI:
    def __init__(self, adminId = 1):
        self.adminId = adminId
        self.root = tk.Tk()
        self.root.title("Train Manager")
        self.root.geometry("450x450")
        self.name_entry = None
        self.details_entry = None
        self.class_listbox = None
        
        self.add_train_button = tk.Button(self.root, text="Add Train", command=self.addTrain)
        self.add_train_button.pack()
        
        self.edit_train_button = tk.Button(self.root, text="Edit Train", command=self.edit_train)
        self.edit_train_button.pack()
        
    def populate_class_list(self):
        classes = Class()
        classes = classes.getClasses()
        for class_data in classes:
            self.class_listbox.insert(tk.END, f"{class_data[1]} (${class_data[2]})")

    def addTrain(self):
        self.root = tk.Tk()
        self.root.title("add Train")
        self.root.geometry("450x450")
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()
        
        self.details_label = tk.Label(self.root, text="Details:")
        self.details_label.pack()
        self.details_entry = tk.Entry(self.root)
        self.details_entry.pack()
        
        self.class_label = tk.Label(self.root, text="Classes:")
        self.class_label.pack()
        self.class_listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE)
        self.class_listbox.pack()

        self.add_train_button = tk.Button(self.root, text="Add Train", command=self.add_train)
        self.add_train_button.pack()

        self.populate_class_list()

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
        
        train = Train()
        train.name = name
        train.description = details
        train.adminId = self.adminId
        
        for class_data in selected_classes:
            class_id = class_data[0]
            class_name = class_data[1]
            class_price = class_data[2]
            
            n_seats = self.enter_seats(class_name)
            
            train.classes[class_id] = [class_name, class_price, n_seats]
        
        train.addTrain()
        messagebox.showinfo("Success", "Train added successfully")
        self.name_entry.delete(0, tk.END)
        self.details_entry.delete(0, tk.END)
        self.class_listbox.selection_clear(0, tk.END)
        
    def enter_seats(self, class_name):
        seats = tk.simpledialog.askinteger("Enter Seats", f"Enter the number of seats for {class_name}")
        return seats

    def edit_train(self):
        selected_train_index = self.select_train()
        if selected_train_index is None:
            return

        selected_train = Train(selected_train_index)

        edit_choice = self.choose_edit_option()

        if edit_choice == 1:
            self.edit_train_details(selected_train)
        elif edit_choice == 2:
            self.edit_train_classes(selected_train)

    def select_train(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute('SELECT trainId, name FROM Train')
        rows = cursor.fetchall()
        conn.close()

        train_names = [f"{row[0]} - {row[1]}" for row in rows]
        prompt = "\n".join(train_names)
        selected_index = simpledialog.askinteger("Select Train", f"Select a train:\n{prompt}", minvalue=1, maxvalue=len(train_names))
        if selected_index is None:
            return None

        return int(rows[selected_index - 1][0])

    def choose_edit_option(self):
        return tk.simpledialog.askinteger("Edit Train", "What would you like to edit?\n\n1. Train Details\n2. Train Classes")

    def edit_train_details(self, train):
        new_name = tk.simpledialog.askstring("Edit Train Details", "Enter new train name:", initialvalue=train.name)
        new_details = tk.simpledialog.askstring("Edit Train Details", "Enter new train details:", initialvalue=train.description)

        if new_name and new_details:
            train.name = new_name
            train.description = new_details
            train.editTrain()
            tk.messagebox.showinfo("Success", "Train details edited successfully")
        else:
            tk.messagebox.showerror("Error", "Please enter valid train details")

    def edit_train_classes(self, train):
        selected_class_index = self.select_train_class(train)
        if selected_class_index is None:
            return

        new_seats = self.enter_seats(train.classes[selected_class_index][0])
        if new_seats is None:
            return

        train.classes[selected_class_index][2] = new_seats
        train.editTrainClass(selected_class_index)
        tk.messagebox.showinfo("Success", "Train class edited successfully")

    def select_train_class(self, train):
        class_names = [f"{class_id} - {train.classes[class_id][0]} Number of Seats: {train.classes[class_id][2]}" for class_id in train.classes]
        prompt = "\n".join(class_names)
        selected_index = tk.simpledialog.askinteger("Select Train Class", f"Select a class to edit:\n{prompt}", minvalue=1, maxvalue=len(class_names))
        if selected_index is None:
            return None

        return selected_index

    def enter_seats(self, class_name):
        return tk.simpledialog.askinteger("Enter Seats", f"Enter the number of seats for {class_name}")
        
    def run(self):
        self.root.mainloop()



gui = TrainManagerGUI()
gui.run()




