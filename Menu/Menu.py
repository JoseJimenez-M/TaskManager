import tkinter as tk
from styles import *

def form_Menu(role):
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.title("Menu")
    root.config(bg="#1E1E2E")

    # Función para regresar al login
    def back_to_login():
        root.destroy()
        from Login.login import ModernLogin
        ModernLogin()

    # Función para crear tarea
    def createTask():
        from Tasks.CreateTasks import create_task
        root.destroy()
        create_task()

    def completeTask():
        from Tasks.CompleteTask import complete_task_form
        root.destroy()
        complete_task_form()

    def showAllTasks():
        from Tasks.showAllTasks import showAllTask_form
        root.destroy()
        showAllTask_form()

    # Contenedor principal (frame)
    frame = tk.Frame(root, bg="#1E1E2E")
    frame.pack(expand=True)

    # Título de bienvenida
    label = tk.Label(frame, text="Welcome!", font=title_font, bg=bg_color, fg=text_color)
    label.pack(pady=30)

    # Botón para mostrar todas las tareas
    showTask_button = tk.Button(frame, text="Show All Task", font=general_font, fg=text_color, bg=accent_color, bd=0, relief="flat", command=showAllTasks)
    showTask_button.pack(pady=10, ipadx=20, ipady=5)
    showTask_button.bind("<Enter>", lambda e: showTask_button.config(bg="#3B7DD8"))
    showTask_button.bind("<Leave>", lambda e: showTask_button.config(bg=accent_color))

    # Botón para completar tareas
    completeTask_button = tk.Button(frame, text="Complete Task", font=general_font, fg=text_color, bg=accent_color, bd=0, relief="flat", command=completeTask)
    completeTask_button.pack(pady=10, ipadx=20, ipady=5)
    completeTask_button.bind("<Enter>", lambda e: completeTask_button.config(bg="#3B7DD8"))
    completeTask_button.bind("<Leave>", lambda e: completeTask_button.config(bg=accent_color))

    # Botón de logout
    close_button = tk.Button(frame, text="Logout", font=general_font, fg=text_color, bg=red_color, bd=0, relief="flat", command=back_to_login)
    close_button.pack(pady=30, ipadx=20, ipady=5)
    close_button.bind("<Enter>", lambda e: close_button.config(bg="#D9372A"))
    close_button.bind("<Leave>", lambda e: close_button.config(bg=red_color))

    # Func Admin (if role == 1)
    if role == 1:
        labelAdmin = tk.Label(frame, text="Admin Functions:", font=("Poppins", 16), bg=bg_color, fg=text_color)
        labelAdmin.pack(pady=30)

        addUser_button = tk.Button(frame, text="Add User", font=general_font, fg=text_color, bg=accent_color, bd=0, relief="flat", command=root.destroy)
        addUser_button.pack(pady=10, ipadx=20, ipady=5)
        addUser_button.bind("<Enter>", lambda e: addUser_button.config(bg="#3B7DD8"))
        addUser_button.bind("<Leave>", lambda e: addUser_button.config(bg=accent_color))

        createTask_button = tk.Button(frame, text="Create Task", font=general_font, fg=text_color, bg=accent_color, bd=0, relief="flat", command=createTask)
        createTask_button.pack(pady=10, ipadx=20, ipady=5)
        createTask_button.bind("<Enter>", lambda e: createTask_button.config(bg="#3B7DD8"))
        createTask_button.bind("<Leave>", lambda e: createTask_button.config(bg=accent_color))

        deleteTask_button = tk.Button(frame, text="Delete Task", font=general_font, fg=text_color, bg=accent_color, bd=0, relief="flat", command=root.destroy)
        deleteTask_button.pack(pady=10, ipadx=20, ipady=5)
        deleteTask_button.bind("<Enter>", lambda e: deleteTask_button.config(bg="#3B7DD8"))
        deleteTask_button.bind("<Leave>", lambda e: deleteTask_button.config(bg=accent_color))

        updateTask_button = tk.Button(frame, text="Update Task", font=general_font, fg=text_color, bg=accent_color, bd=0, relief="flat", command=root.destroy)
        updateTask_button.pack(pady=10, ipadx=20, ipady=5)
        updateTask_button.bind("<Enter>", lambda e: updateTask_button.config(bg="#3B7DD8"))
        updateTask_button.bind("<Leave>", lambda e: updateTask_button.config(bg=accent_color))

    root.mainloop()
