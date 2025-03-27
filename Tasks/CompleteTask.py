import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import globals
from Tasks.db_queries import get_user_tasks
from Tasks.db_queries import connect_db


def complete_task_form():

    def back_to_Menu():
        from Menu.Menu import form_Menu
        root.destroy()
        form_Menu(globals.user_role)

    root = tk.Tk()
    root.title("Complete Task")
    root.attributes('-fullscreen', True)

    tasks = get_user_tasks(globals.user_name)

    if not tasks:
        messagebox.showinfo("No tasks", "You have no tasks assigned.")
        back_to_Menu()
        return

    tree = ttk.Treeview(root, columns=("ID", "Title", "Priority", "State"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Title", text="Title")
    tree.heading("Priority", text="Priority")
    tree.heading("State", text="State")

    for task in tasks:
        tree.insert("", "end", values=(task["id"], task["title"], task["priority"], task["state"]))

    tree.pack(pady=20)

    def complete_task():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Select Task", "Please select a task to complete.")
            return

        task_id = tree.item(selected_item)["values"][0]

        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("UPDATE Tasks SET state = 'Done' WHERE id = %s", (task_id,))
                conn.commit()
                messagebox.showinfo("Task Completed", "Task marked as completed.")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error completing task: {err}")
            finally:
                cursor.close()
                conn.close()


    complete_button = ttk.Button(root, text="Complete Task", command=complete_task)
    complete_button.pack(pady=10)

    close_button = ttk.Button(root, text="Back", command=back_to_Menu)
    close_button.pack(pady=10)

    root.mainloop()
