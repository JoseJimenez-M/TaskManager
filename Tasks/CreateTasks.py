import tkinter as tk
from tkinter import ttk

###RANDOM INFO, ONLY FOR TEST
def create_task():
    root = tk.Tk()
    root.title("Add Task")
    root.geometry("400x350")

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
    status_combobox = ttk.Combobox(root, values=["Hiauts", "Done"])
    status_combobox.pack(padx=10, pady=2)
    status_combobox.current(0)  # Hiatus as Default

    ttk.Label(root, text="For:").pack(anchor="w", padx=10, pady=2)
    assigned_entry = ttk.Entry(root, width=40)
    assigned_entry.pack(padx=10, pady=2)


    save_button = ttk.Button(root, text="Save Task", command=root.destroy)
    save_button.pack(pady=10)

    root.mainloop()