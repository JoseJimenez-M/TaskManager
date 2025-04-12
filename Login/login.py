import tkinter as tk
import auth
import globals
from tkinter import ttk, messagebox
from Menu.Menu import form_Menu
from globals import user_role
from styles import *

class ModernLogin:
    def __init__(self):
        self.window = tk.Tk()
        self.window.attributes('-fullscreen', True)
        self.window.title("Modern Login")
        self.window.configure(bg="#1E1E2E")

        ## General styles
        self.general_font = general_font
        self.bg_color = bg_color
        self.text_color = text_color
        self.accent_color = accent_color
        self.red_color = red_color

        ## Main frame
        self.frame = tk.Frame(self.window, bg=self.bg_color, padx=20, pady=20)
        self.frame.pack(expand=True)

        ## Title
        self.title = tk.Label(self.frame, text="Login", font=("Poppins", 28, "bold"), fg=self.text_color, bg=self.bg_color)
        self.title.pack(pady=10)

        ## User field
        self.label_user = tk.Label(self.frame, text="User:", font=self.general_font, fg=self.text_color, bg=self.bg_color)
        self.label_user.pack(anchor="w")
        
        self.entry_user = tk.Entry(self.frame, font=self.general_font, bd=0, relief="solid", bg="#2B2B3C", fg="white", insertbackground="white")
        self.entry_user.pack(fill="x", padx=10, pady=5, ipady=5)

        ## Password field
        self.label_password = tk.Label(self.frame, text="Password:", font=self.general_font, fg=self.text_color, bg=self.bg_color)
        self.label_password.pack(anchor="w")
        
        self.entry_password = tk.Entry(self.frame, font=self.general_font, bd=0, relief="solid", bg="#2B2B3C", fg="white", insertbackground="white", show="*")
        self.entry_password.pack(fill="x", padx=10, pady=5, ipady=5)

        ## Submit button with hover effect
        self.button_submit = tk.Button(self.frame, text="Submit", font=("Poppins", 14, "bold"), fg="white", bg=self.accent_color, bd=0, relief="flat", command=self.TryLog)
        self.button_submit.pack(pady=20, ipadx=20, ipady=5)

        self.button_submit.bind("<Enter>", lambda e: self.button_submit.config(bg="#3B7DD8"))
        self.button_submit.bind("<Leave>", lambda e: self.button_submit.config(bg=self.accent_color))

        ## Close
        self.button_close = tk.Button(self.frame, text="Close", font=("Poppins", 10, "bold"), fg="white",bg=self.red_color, bd=0, relief="flat", command=self.window.destroy)
        self.button_close.pack(pady=20, ipadx=20, ipady=5)

        auth.exist_file()

        self.window.mainloop()

    def TryLog(self):
        name = self.entry_user.get()
        password = self.entry_password.get()

        # Validate
        if auth.validate_user(name, password):
            role = auth.get_user_role(name)

            globals.user_role = role
            globals.user_name = self.entry_user.get()
            globals.user_role = user_role

            if role == 1:
                messagebox.showinfo("Access Granted", "Welcome Admin!")
            else:
                messagebox.showinfo("Access Granted", "Welcome User!")

             # Open Main and close login
            
            self.window.destroy()
            form_Menu(role)

        else:
            messagebox.showerror("Access Denied", "Incorrect Username or Password!")


if __name__ == "__main__":
    ModernLogin()

