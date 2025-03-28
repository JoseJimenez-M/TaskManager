import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from Login import auth
from Tasks.db_queries import *
import globals
from styles import *

def update_task_form():
    def back_to_Menu():
        from Menu.Menu import form_Menu
        root.destroy()
        form_Menu(globals.user_role)

    def on_task_select(event):
        selected_item = tree.selection()
        if not selected_item:
            return

        task_values = tree.item(selected_item)["values"]
        if not task_values:
            return

        task_id, title, priority, state, deadline, assigned_user = task_values

        #Title
        title_entry.delete(0, tk.END)
        title_entry.insert(0, title)

        # Prio,State
        priority_combobox.set(priority)
        status_combobox.set(state)

        try:
            from datetime import datetime
            deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
            deadline_entry.set_date(deadline_date)
        except ValueError:
            print("Date error!:", deadline)

        description = get_task_description(task_id)
        description_text.delete("1.0", tk.END)
        if description:
            description_text.insert("1.0", description)
        else:
            print("Description not exist")
        if assigned_user in assigned_user_combobox["values"]:
            assigned_user_combobox.set(assigned_user)
        else:
            print("User not in the list:", assigned_user)

    root = tk.Tk()
    root.title("Update Task")
    root.attributes('-fullscreen', True)
    root.config(bg=bg_color)

    tree_frame = tk.Frame(root, bg=bg_color)
    tree_frame.pack(fill="x", pady=10)

    form_frame = tk.Frame(root, bg=bg_color)
    form_frame.pack(pady=20)

    tasks = get_tasks()

    if not tasks:
        messagebox.showinfo("No tasks", "You have no tasks assigned.")
        back_to_Menu()
        return

    tree = ttk.Treeview(tree_frame, columns=("ID", "Title", "Priority", "State", "Deadline", "Assigned User"), show="headings", height=8)
    tree.heading("ID", text="ID")
    tree.heading("Title", text="Title")
    tree.heading("Priority", text="Priority")
    tree.heading("State", text="State")
    tree.heading("Deadline", text="Deadline")
    tree.heading("Assigned User", text="Assigned User")

    for task in tasks:
        tree.insert("", "end", values=(task["id"], task["title"], task["priority"], task["state"], task["deadline"], task["assigned_user"]))

    tree.pack(pady=10)
    tree.bind("<<TreeviewSelect>>", on_task_select)

    def create_label(text, row):
        label = ttk.Label(form_frame, text=text, foreground=text_color, background=bg_color, font=("Poppins", 12, "bold"))
        label.grid(row=row, column=0, sticky="w", pady=5, padx=10)

    def create_entry(row):
        entry = tk.Entry(form_frame, width=40, font=("Poppins", 12), bg=entry_bg_color, fg=entry_fg_color, insertbackground="white", relief="flat")
        entry.grid(row=row, column=1, pady=5, padx=10, ipadx=10, ipady=5)
        return entry

    create_label("Title:", 0)
    title_entry = create_entry(0)

    create_label("Priority:", 1)
    priority_combobox = ttk.Combobox(form_frame, values=["High", "Medium", "Low"], font=("Poppins", 12))
    priority_combobox.grid(row=1, column=1, pady=5, padx=10, ipadx=10, ipady=5)

    create_label("Description:", 2)
    description_text = tk.Text(form_frame, height=4, width=40, font=("Poppins", 12), bg=entry_bg_color, fg=entry_fg_color, relief="flat")
    description_text.grid(row=2, column=1, pady=5, padx=10, ipadx=10, ipady=5)

    create_label("State:", 3)
    status_combobox = ttk.Combobox(form_frame, values=["On Hold", "Done"], font=("Poppins", 12))
    status_combobox.grid(row=3, column=1, pady=5, padx=10, ipadx=10, ipady=5)

    create_label("Deadline:", 4)
    deadline_entry = DateEntry(form_frame, width=12, background=accent_color, foreground="white", borderwidth=2, font=("Poppins", 12))
    deadline_entry.grid(row=4, column=1, pady=5, padx=10, ipadx=10, ipady=5)

    users = auth.load_users()
    user_names = list(users.keys())

    create_label("Assign to User:", 5)
    assigned_user_combobox = ttk.Combobox(form_frame, values=user_names, font=("Poppins", 12))
    assigned_user_combobox.grid(row=5, column=1, pady=5, padx=10, ipadx=10, ipady=5)

    def update_task():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Select Task", "Please select a task to update.")
            return

        task_id = tree.item(selected_item)["values"][0]
        title = title_entry.get()
        priority = priority_combobox.get()
        description = description_text.get("1.0", tk.END).strip()
        state = status_combobox.get()
        deadline = deadline_entry.get_date()
        assigned_user = assigned_user_combobox.get()

        if not title or not priority or not description or not state or not deadline or not assigned_user:
            messagebox.showwarning("Incomplete Data", "Please fill in all fields.")
            return

        if update_task_query(task_id, title, priority, description, state, deadline, assigned_user):
            messagebox.showinfo("Task Updated", "The task has been updated successfully.")
            back_to_Menu()

    button_frame = tk.Frame(form_frame, bg=bg_color)
    button_frame.grid(row=0, column=2, rowspan=6, padx=20, sticky="n")

    def create_button(text, command, bg_color=accent_color):
        btn = tk.Button(button_frame, text=text, command=command, font=("Poppins", 14), bg=bg_color, fg=text_color, relief="flat", bd=0,
                        activebackground=button_hover, activeforeground=text_color)
        btn.pack(pady=10, ipadx=20, ipady=5, fill="x")
        return btn

    create_button("Save Task", update_task)
    create_button("Menu", back_to_Menu, bg_color=red_color)

    root.mainloop()
