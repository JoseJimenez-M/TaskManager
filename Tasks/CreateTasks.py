import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import globals


###RANDOM INFO, ONLY FOR TEST
def create_task():

    def back_to_Menu():
        from Menu.Menu import form_Menu
        root.destroy()
        form_Menu(globals.user_role)

    root = tk.Tk()
    root.title("Add Task")
    root.attributes('-fullscreen', True)

    # Etiquetas y Entradas
    ttk.Label(root, text="Title:").pack(anchor="w", padx=10, pady=2)
    title_entry = ttk.Entry(root, width=40)
    title_entry.pack(padx=10, pady=2)

    ttk.Label(root, text="Prio:").pack(anchor="w", padx=10, pady=2)
    priority_combobox = ttk.Combobox(root, values=["High", "Medium", "Low"])
    priority_combobox.pack(padx=10, pady=2)
    priority_combobox.current(1)  # Medium Default

    ttk.Label(root, text="Description:").pack(anchor="w", padx=10, pady=2)
    description_text = tk.Text(root, height=4, width=40)
    description_text.pack(padx=10, pady=2)

    ttk.Label(root, text="State:").pack(anchor="w", padx=10, pady=2)
    status_combobox = ttk.Combobox(root, values=["On Hold", "Done"])
    status_combobox.pack(padx=10, pady=2)
    status_combobox.current(0)  # On hold as Default

    ttk.Label(root, text="Deadline:").pack(anchor="w", padx=10, pady=2)
    deadline_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
    deadline_entry.pack(padx=10, pady=2)

    save_button = ttk.Button(root, text="Save Task", command=root.destroy)
    save_button.pack(pady=10)

    cancel_button = ttk.Button(root, text="Cancel", command=back_to_Menu)
    cancel_button.pack(pady=10)

    root.mainloop()