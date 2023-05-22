import tkinter as tk
from tkinter import ttk, messagebox
from Admin import Admin
from tripView import AddTripView, UpdateTripView

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Main App")

        self.container = ttk.Frame(self.root)
        self.container.pack(padx=10, pady=10)

        sign_in_button = ttk.Button(self.container, text="Sign In", command=self.show_sign_in)
        sign_in_button.grid(row=0, column=0, pady=10)

        sign_up_button = ttk.Button(self.container, text="Sign Up", command=self.show_sign_up)
        sign_up_button.grid(row=0, column=1, padx=5, pady=10)

        self.root.mainloop()

    def show_sign_in(self):
        self.root.withdraw()
        sign_in_window = SignInWindow(self.root, self)

    def show_sign_up(self):
        self.root.deiconify()
        sign_up_window = SignUpWindow(self.root, self)



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

        add_train_button = ttk.Button(self.container, text="Add Train")
        add_train_button.grid(row=0, column=0, padx=10, pady=5)

        edit_train_button = ttk.Button(self.container, text="Edit Train")
        edit_train_button.grid(row=1, column=0, padx=10, pady=5)

        add_trip_button = ttk.Button(self.container, text="Add Trip", command= lambda: AddTripView(adminId))
        add_trip_button.grid(row=0, column=1, padx=10, pady=5)

        edit_trip_button = ttk.Button(self.container, text="Edit Trip", command= lambda: UpdateTripView(adminId))
        edit_trip_button.grid(row=1, column=1, padx=10, pady=5)

        edit_info_button = ttk.Button(self.container, text="Edit My Info",command= lambda: EditInfoWindow(self.parent,self.main_app,adminId))
        edit_info_button.grid(row=2, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    main_app = MainApp()
