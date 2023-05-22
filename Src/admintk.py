import tkinter as tk
from tkinter import ttk, messagebox
from Admin import Admin
from tripView import AddTripView, UpdateTripView, TripsView
from TrainGUI import AddTrain, EditTrain

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Main App")

        # Set the style for the application
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Configure style for specific elements
        self.style.configure("TButton",
                             padding=10,
                             relief="flat",
                             font=("Helvetica", 12),
                             background="#007bff",
                             foreground="white")
        self.style.map("TButton",
                       background=[("active", "#0056b3")],
                       foreground=[("active", "white")])

        self.style.configure("TLabel",
                             padding=5,
                             font=("Helvetica", 12),
                             foreground="#333333")

        self.style.configure("TEntry",
                             padding=5,
                             font=("Helvetica", 12))

        # Create the home page
        self.create_home_page()

        self.root.mainloop()

    def create_home_page(self):
        home_frame = ttk.Frame(self.root)
        home_frame.pack(padx=10, pady=10)

        # Add a header
        header_label = ttk.Label(home_frame,
                                 text="Welcome to Your App",
                                 style="Header.TLabel")
        header_label.pack(pady=20)



        # Add descriptive text
        description_label = ttk.Label(home_frame,
                                      text="Train Reservation system using sql and python gui created by tkinter",
                                      style="Description.TLabel")
        description_label.pack(pady=20)

        # Add a sign in button
        sign_in_button = ttk.Button(home_frame,
                                    text="Sign In",
                                    command=self.show_sign_in,
                                    style="TButton")
        sign_in_button.pack(pady=10)

        # Add a sign up button
        sign_up_button = ttk.Button(home_frame,
                                    text="Sign Up",
                                    command=self.show_sign_up,
                                    style="TButton")
        sign_up_button.pack()

        # Apply custom styles for header and description labels
        self.style.configure("Header.TLabel",
                             font=("Helvetica", 20, "bold"),
                             foreground="#333333")

        self.style.configure("Description.TLabel",
                             font=("Helvetica", 14),
                             foreground="#555555")

    def show_sign_in(self):
        self.root.deiconify()
        sign_in_window = SignInWindow(self.root, self)

    def show_sign_up(self):
        self.root.deiconify()
        sign_up_window = SignUpWindow(self.root, self)

import tkinter as tk
from tkinter import ttk, messagebox
from Admin import Admin

class SignInWindow:
    def __init__(self, parent, main_app):
        self.parent = parent
        self.main_app = main_app

        self.sign_in_window = tk.Toplevel(parent)
        self.sign_in_window.title("Sign In")

        self.container = ttk.Frame(self.sign_in_window)
        self.container.pack(padx=10, pady=10)

        email_label = ttk.Label(self.container, text="Email")
        email_label.grid(row=0, column=0, sticky="w", pady=5)
        self.email_entry = ttk.Entry(self.container)
        self.email_entry.grid(row=0, column=1, pady=5)

        password_label = ttk.Label(self.container, text="Password")
        password_label.grid(row=1, column=0, sticky="w", pady=5)
        self.password_entry = ttk.Entry(self.container, show="*")
        self.password_entry.grid(row=1, column=1, pady=5)

        sign_in_button = ttk.Button(self.container, text="Sign In", command=self.handle_sign_in)
        sign_in_button.grid(row=2, columnspan=2, pady=10)

    def handle_sign_in(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        admin = Admin()
        try:
            success = admin.sign_in(email, password)
            if success:
                messagebox.showinfo("Success", "Sign in successful!")
                self.show_main_menu(admin.adminId)
            else:
                messagebox.showerror("Error", "Invalid email or password.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        self.sign_in_window.destroy()

    def show_main_menu(self, adminId):
        main_menu_window = MainMenuWindow(self.parent, self.main_app, adminId)


class SignUpWindow:
    def __init__(self, parent, main_app):
        self.parent = parent
        self.main_app = main_app

        self.sign_up_window = tk.Toplevel(parent)
        self.sign_up_window.title("Sign Up")

        self.container = ttk.Frame(self.sign_up_window)
        self.container.pack(padx=10, pady=10)

        name_label = ttk.Label(self.container, text="Name")
        name_label.grid(row=0, column=0, sticky="w", pady=5)
        self.name_entry = ttk.Entry(self.container)
        self.name_entry.grid(row=0, column=1, pady=5)

        email_label = ttk.Label(self.container, text="Email")
        email_label.grid(row=1, column=0, sticky="w", pady=5)
        self.email_entry = ttk.Entry(self.container)
        self.email_entry.grid(row=1, column=1, pady=5)

        password_label = ttk.Label(self.container, text="Password")
        password_label.grid(row=2, column=0, sticky="w", pady=5)
        self.password_entry = ttk.Entry(self.container, show="*")
        self.password_entry.grid(row=2, column=1, pady=5)

        sign_up_button = ttk.Button(self.container, text="Sign Up", command=self.handle_sign_up)
        sign_up_button.grid(row=4, columnspan=2, pady=10)

    def handle_sign_up(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        admin = Admin()
        try:
            success = admin.sign_up(name, email, password)
            if success:
                messagebox.showinfo("Success", "Sign up successful!")
            else:
                messagebox.showerror("Error", "Sign up failed.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

        self.sign_up_window.destroy()

class EditInfoWindow:
    def __init__(self, parent, main_app,admin_id):
        self.parent = parent
        self.main_app = main_app
        self.admin = Admin(admin_id)

        self.edit_info_window = tk.Toplevel(parent)
        self.edit_info_window.title("Edit Info")

        self.container = ttk.Frame(self.edit_info_window)
        self.container.pack(padx=10, pady=10)

        name_label = ttk.Label(self.container, text="Name")
        name_label.grid(row=0, column=0, sticky="w", pady=5)
        self.name_entry = ttk.Entry(self.container)
        self.name_entry.grid(row=0, column=1, pady=5)
        self.name_entry.insert(tk.END, self.admin.name)

        email_label = ttk.Label(self.container, text="Email")
        email_label.grid(row=1, column=0, sticky="w", pady=5)
        self.email_entry = ttk.Entry(self.container)
        self.email_entry.grid(row=1, column=1, pady=5)
        self.email_entry.insert(tk.END, self.admin.email) 

        password_label = ttk.Label(self.container, text="Password")
        password_label.grid(row=2, column=0, sticky="w", pady=5)
        self.password_entry = ttk.Entry(self.container, show="*")
        self.password_entry.grid(row=2, column=1, pady=5)
        self.password_entry.insert(tk.END, self.admin.password) 

        update_button = ttk.Button(self.container, text="Update", command=self.handle_update)
        update_button.grid(row=3, columnspan=2, pady=10)

    def handle_update(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        success = self.admin.update_admin(email, name, password)
        if success:
            messagebox.showinfo("Success", "Info updated successfully!")
        else:
            messagebox.showerror("Error", "Error updating admin")

        self.edit_info_window.destroy()        

class MainMenuWindow:
    def __init__(self, parent, main_app, adminId):
        self.parent = parent
        self.main_app = main_app

        self.main_menu_window = tk.Toplevel(parent)
        self.main_menu_window.title("Main Menu")

        self.container = ttk.Frame(self.main_menu_window)
        self.container.pack(padx=10, pady=10)

        add_train_button = ttk.Button(self.container, text="Add Train", command= lambda : AddTrain(self.parent, adminId))
        add_train_button.grid(row=0, column=0, padx=10, pady=5)

        edit_train_button = ttk.Button(self.container, text="Edit Train", command= lambda : EditTrain(adminId))
        edit_train_button.grid(row=1, column=0, padx=10, pady=5)

        add_trip_button = ttk.Button(self.container, text="Add Trip", command= lambda: AddTripView(adminId))
        add_trip_button.grid(row=0, column=1, padx=10, pady=5)

        edit_trip_button = ttk.Button(self.container, text="Edit Trip", command= lambda:TripsView(adminId))
        edit_trip_button.grid(row=1, column=1, padx=10, pady=5)

        edit_info_button = ttk.Button(self.container, text="Edit My Info",command= lambda: EditInfoWindow(self.parent,self.main_app,adminId))
        edit_info_button.grid(row=2, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    main_app = MainApp()
