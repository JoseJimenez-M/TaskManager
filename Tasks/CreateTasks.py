import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import globals
from Login import auth
from styles import *
from Notifications.Notifications import notify_user_new_task


def create_task():
    def back_to_Menu():
        from Menu.Menu import form_Menu
        root.destroy()
        form_Menu(globals.user_role)

    def save():
        from Tasks.db_queries import save_task
        title = title_entry.get()
        priority = priority_combobox.get()
        description = description_text.get("1.0", tk.END).strip()
        state = status_combobox.get()
        deadline = deadline_entry.get_date().strftime('%Y-%m-%d')
        assigned_user = assigned_user_combobox.get()

        save_task(title, priority, description, state, deadline, assigned_user)
        notify_user_new_task(assigned_user,title,deadline)

    root = tk.Tk()
    root.title("Add Task")
    root.attributes('-fullscreen', True)
    root.config(bg=bg_color)

    frame = tk.Frame(root, bg=bg_color)
    frame.pack(pady=40)

    def create_label(text):
        return ttk.Label(frame, text=text, foreground=text_color, background=bg_color, font=("Poppins", 12, "bold"))

    def create_entry(width=40):
        return tk.Entry(frame, width=width, font=("Poppins", 12), bg=entry_bg_color, fg=entry_fg_color, insertbackground="white", relief="flat")

    create_label("Title:").grid(row=0, column=0, sticky="w", pady=5)
    title_entry = create_entry()
    title_entry.grid(row=0, column=1, pady=5, padx=10)

    create_label("Priority:").grid(row=1, column=0, sticky="w", pady=5)
    priority_combobox = ttk.Combobox(frame, values=["High", "Medium", "Low"], font=("Poppins", 12))
    priority_combobox.grid(row=1, column=1, pady=5, padx=10)
    priority_combobox.current(1)  # Medium Default

    create_label("Description:").grid(row=2, column=0, sticky="w", pady=5)
    description_text = tk.Text(frame, height=4, width=40, font=("Poppins", 12), bg=entry_bg_color, fg=entry_fg_color, relief="flat")
    description_text.grid(row=2, column=1, pady=5, padx=10)

    create_label("State:").grid(row=3, column=0, sticky="w", pady=5)
    status_combobox = ttk.Combobox(frame, values=["On Hold", "Done"], font=("Poppins", 12))
    status_combobox.grid(row=3, column=1, pady=5, padx=10)
    status_combobox.current(0)  # On hold as Default

    create_label("Deadline:").grid(row=4, column=0, sticky="w", pady=5)
    deadline_entry = DateEntry(frame, width=12, background=accent_color, foreground="white", borderwidth=2, font=("Poppins", 12))
    deadline_entry.grid(row=4, column=1, pady=5, padx=10)

    users = auth.load_users()
    user_names = list(users.keys())

    create_label("Assign to User:").grid(row=5, column=0, sticky="w", pady=5)
    assigned_user_combobox = ttk.Combobox(frame, values=user_names, font=("Poppins", 12))
    assigned_user_combobox.grid(row=5, column=1, pady=5, padx=10)

    def create_button(text, command, bg_color=accent_color):
        btn = tk.Button(frame, text=text, command=command, font=("Poppins", 14),
                        bg=bg_color, fg=text_color, relief="flat", bd=0,
                        activebackground=button_hover, activeforeground=text_color)
        return btn

    save_button = create_button("Save Task", save)
    save_button.grid(row=6, column=0, columnspan=2, pady=15, ipadx=20, ipady=5)

    cancel_button = create_button("Menu", back_to_Menu, bg_color="#F34336")  # Rojo para cancelar
    cancel_button.grid(row=7, column=0, columnspan=2, pady=5, ipadx=20, ipady=5)

    root.mainloop()
