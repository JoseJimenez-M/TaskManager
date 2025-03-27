import tkinter as tk
from tkinter import ttk
from styles import *
import globals
from Tasks.db_queries import *


def showAllTask_form():
    def back_to_Menu():
        from Menu.Menu import form_Menu
        root.destroy()
        form_Menu(globals.user_role)

    def on_task_select(event):
        selected_item = tree.selection()
        if not selected_item:
            return

        task_id = tree.item(selected_item)["values"][0]
        description = get_task_description(task_id)

        description_text.config(state=tk.NORMAL)
        description_text.delete("1.0", tk.END)
        description_text.insert(tk.END, description)
        description_text.config(state=tk.DISABLED)

    root = tk.Tk()
    root.title("Show All Tasks")
    root.attributes('-fullscreen', True)
    root.config(bg=bg_color)

    if globals.user_role == 1:
        tasks = get_tasks()
    else:
        tasks = get_user_tasks(globals.user_name)

    if not tasks:
        messagebox.showinfo("No tasks", "There are no tasks available.")
        back_to_Menu()
        return

    style = ttk.Style()
    style.configure("Custom.Treeview", background="#A9C6E5", foreground="#1a1a1f", fieldbackground="#A9C6E5",
                    font=("Poppins", 12))
    style.configure("Custom.Treeview.Heading", font=("Poppins", 18, "bold"), foreground="#A9C6E5")

    tree = ttk.Treeview(root, columns=("ID", "Title", "Priority", "State", "assigned_user"), show="headings", height=8,
                        style="Custom.Treeview")
    tree.heading("ID", text="ID")
    tree.heading("Title", text="Title")
    tree.heading("Priority", text="Priority")
    tree.heading("State", text="State")
    tree.heading("assigned_user", text="Assigned User")

    tree.column("#1", stretch=tk.NO, width=150)
    tree.column("#2", stretch=tk.NO, width=250)
    tree.column("#3", stretch=tk.NO, width=200)
    tree.column("#4", stretch=tk.NO, width=200)
    tree.column("#5", stretch=tk.NO, width=250)

    tree.tag_configure("even", background="#A9C6E5")
    tree.tag_configure("odd", background="#C8D9EB")

    for index, task in enumerate(tasks):
        tag = "even" if index % 2 == 0 else "odd"
        tree.insert("", "end",
                    values=(task["id"], task["title"], task["priority"], task["state"], task["assigned_user"]),
                    tags=(tag,))

    tree.pack(pady=(100, 20))
    tree.bind("<<TreeviewSelect>>", on_task_select)

    description_label = tk.Label(root, text="Task Description:", font=("Poppins", 14), bg=bg_color, fg=text_color)
    description_label.pack(pady=(10, 5))

    description_text = tk.Text(root, height=5, width=80, font=("Poppins", 12), wrap="word", bg="#F0F0F0", fg="#1a1a1f")
    description_text.config(state=tk.DISABLED)
    description_text.pack(pady=(5, 20))

    close_button = tk.Button(root, text="Back", command=back_to_Menu, font=("Poppins", 14),
                             bg=red_color, fg=text_color, relief="flat", bd=0,
                             activebackground=red_color, activeforeground=text_color)
    close_button.pack(pady=10)

    root.mainloop()
