import tkinter as tk
from tkinter import messagebox
from Menu.Menu import form_Menu
from auth import create_user
from styles import *
import globals

def create_user_form():
    def back_to_menu():
        from Menu.Menu import form_Menu
        root.destroy()
        form_Menu(globals.user_role)

    def submit_user():
        username = username_entry.get().strip()
        password = password_entry.get().strip()
        role = role_combobox.get()

        if role == "admin":
            role = 1
        else:
            role = 0

        if not username or not password:
            messagebox.showwarning("Incomplete Data", "Please fill in all fields.")
            return

        try:
            create_user(username, password, role)
            messagebox.showinfo("Success", "User created successfully.")
            back_to_menu()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.title("Add User")
    root.config(bg="#1E1E2E")

    frame = tk.Frame(root, bg=bg_color)
    frame.pack(pady=30)

    def create_label(text):
        return tk.Label(frame, text=text, font=("Poppins", 12, "bold"), fg=text_color, bg=bg_color)

    def create_entry(show=""):
        return tk.Entry(frame, font=("Poppins", 12), bg="white", fg="black", relief="flat", show=show)

    create_label("Username:").grid(row=0, column=0, sticky="w", pady=5)
    username_entry = create_entry()
    username_entry.grid(row=0, column=1, pady=5, padx=10)

    create_label("Password:").grid(row=1, column=0, sticky="w", pady=5)
    password_entry = create_entry(show="*")
    password_entry.grid(row=1, column=1, pady=5, padx=10)

    create_label("Role:").grid(row=2, column=0, sticky="w", pady=5)
    role_combobox = ttk.Combobox(frame, values=["Admin", "User"], font=("Poppins", 12))
    role_combobox.grid(row=2, column=1, pady=5, padx=10)
    role_combobox.current(0)

    def create_button(text, command, bg=accent_color):
        return tk.Button(frame, text=text, command=command, font=("Poppins", 14), bg=bg, fg=text_color,
                         relief="flat", bd=0, activebackground=red_color, activeforeground=text_color)

    create_button("Create User", submit_user).grid(row=3, column=0, columnspan=2, pady=15, ipadx=20, ipady=5)
    create_button("Back to Menu", back_to_menu, bg=red_color).grid(row=4, column=0, columnspan=2, pady=5, ipadx=20, ipady=5)

    root.mainloop()
