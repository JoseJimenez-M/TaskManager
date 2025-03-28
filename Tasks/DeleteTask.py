import tkinter as tk
import globals
from Tasks.db_queries import *
from styles import *

def Delete_task_form():

    def back_to_Menu():
        from Menu.Menu import form_Menu
        root.destroy()
        form_Menu(globals.user_role)

    root = tk.Tk()
    root.title("Delete Task")
    root.attributes('-fullscreen', True)
    root.config(bg=bg_color)

    tasks = get_tasks()

    if not tasks:
        messagebox.showinfo("No tasks", "No task assigned.")
        back_to_Menu()
        return

    style = ttk.Style()


    style.configure("Custom.Treeview",
                    background="#A9C6E5",
                    foreground="#1a1a1f",
                    fieldbackground="#A9C6E5",
                    font=("Poppins", 12))

    style.configure("Custom.Treeview.Heading",
                    font=("Poppins", 18, "bold"),
                    foreground="#A9C6E5"
                    )

    tree = ttk.Treeview(root, columns=("ID", "Title", "Priority", "State","Deadline","assigned_user"), show="headings", height=8,
                        style="Custom.Treeview")

    tree.heading("ID", text="ID")
    tree.heading("Title", text="Title")
    tree.heading("Priority", text="Priority")
    tree.heading("State", text="State")
    tree.heading("Deadline", text="Deadline")
    tree.heading("assigned_user", text="Assigned User")

    tree.column("#1", stretch=tk.NO, width=200)
    tree.column("#2", stretch=tk.NO, width=250)
    tree.column("#3", stretch=tk.NO, width=250)
    tree.column("#4", stretch=tk.NO, width=250)
    tree.column("#5", stretch=tk.NO, width=250)
    tree.column("#6", stretch=tk.NO, width=250)

    tree.tag_configure("even", background="#A9C6E5")
    tree.tag_configure("odd", background="#C8D9EB")

    for index, task in enumerate(tasks):
        tag = "even" if index % 2 == 0 else "odd"
        tree.insert("", "end", values=(task["id"], task["title"], task["priority"], task["state"], task["deadline"], task["assigned_user"]), tags=(tag,))

    tree.pack(pady=(240, 80))

    def delete_task():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Select Task", "Please select a task to delete.")
            return

        task_id = tree.item(selected_item)["values"][0]
        deleteTask(task_id)


    delete_button = tk.Button(root, text="DELETE TASK", command=delete_task, font=("Poppins", 24),
                                bg=red_color, fg=text_color, relief="flat", bd=0,
                                activebackground=red_color, activeforeground=text_color)
    delete_button.pack(pady=10)

    close_button = tk.Button(root, text="Back", command=back_to_Menu, font=("Poppins", 24),
                             bg=accent_color, fg=text_color, relief="flat", bd=0,
                             activebackground=accent_color, activeforeground=text_color)
    close_button.pack(pady=10)

    root.mainloop()
