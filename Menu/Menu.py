import tkinter as tk

from Report.Report import create_Report
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

    def updateTasks():
        from Tasks.updateTask import update_task_form
        root.destroy()
        update_task_form()

    def deleteTasks():
        from Tasks.DeleteTask import Delete_task_form
        root.destroy()
        Delete_task_form()

    def createUser():
        from Login.createUser import create_user_form
        root.destroy()
        create_user_form()

    def manageNotifications():
        from Notifications.Notifications import notifications_form
        root.destroy()
        notifications_form()

    def generateReport():
        from Report.Report import create_Report
        create_Report()


    # Contenedor principal (frame)
    frame = tk.Frame(root, bg="#1E1E2E")
    frame.pack(expand=True)

    # Título de bienvenida
    label = tk.Label(frame, text="Welcome!", font=title_font, bg=bg_color, fg=text_color)
    label.pack(pady=30)

    # Botón para mostrar todas las tareas
    showTask_button = tk.Button(frame, text="Show All Task (On hold and Done)", font=general_font, fg=text_color, bg=accent_color, bd=0, relief="flat", command=showAllTasks)
    showTask_button.pack(pady=10, ipadx=20, ipady=5)
    showTask_button.bind("<Enter>", lambda e: showTask_button.config(bg="#3B7DD8"))
    showTask_button.bind("<Leave>", lambda e: showTask_button.config(bg=accent_color))

    # Botón para completar tareas
    completeTask_button = tk.Button(frame, text="Complete Task (To do)", font=general_font, fg=text_color, bg=accent_color, bd=0, relief="flat", command=completeTask)
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

        addUser_button = tk.Button(frame, text="Add User", font=general_font, fg=text_color, bg=accent_color, bd=0, relief="flat", command=createUser)
        addUser_button.pack(pady=10, ipadx=20, ipady=5)
        addUser_button.bind("<Enter>", lambda e: addUser_button.config(bg="#3B7DD8"))
        addUser_button.bind("<Leave>", lambda e: addUser_button.config(bg=accent_color))

        createTask_button = tk.Button(frame, text="Create Task", font=general_font, fg=text_color, bg=accent_color, bd=0, relief="flat", command=createTask)
        createTask_button.pack(pady=10, ipadx=20, ipady=5)
        createTask_button.bind("<Enter>", lambda e: createTask_button.config(bg="#3B7DD8"))
        createTask_button.bind("<Leave>", lambda e: createTask_button.config(bg=accent_color))

        deleteTask_button = tk.Button(frame, text="Delete Task", font=general_font, fg=text_color, bg=accent_color, bd=0, relief="flat", command=deleteTasks)
        deleteTask_button.pack(pady=10, ipadx=20, ipady=5)
        deleteTask_button.bind("<Enter>", lambda e: deleteTask_button.config(bg="#3B7DD8"))
        deleteTask_button.bind("<Leave>", lambda e: deleteTask_button.config(bg=accent_color))

        updateTask_button = tk.Button(frame, text="Update Task", font=general_font, fg=text_color, bg=accent_color, bd=0, relief="flat", command=updateTasks)
        updateTask_button.pack(pady=10, ipadx=20, ipady=5)
        updateTask_button.bind("<Enter>", lambda e: updateTask_button.config(bg="#3B7DD8"))
        updateTask_button.bind("<Leave>", lambda e: updateTask_button.config(bg=accent_color))

        ##Last buttons, Notifications and Report
        ManageNotifications_button = tk.Button(frame, text="Manage Notifications", font=general_font, fg=text_color, bg=accent_color,
                                      bd=0, relief="flat", command=manageNotifications)
        ManageNotifications_button.pack(pady=10, ipadx=20, ipady=5)
        ManageNotifications_button.bind("<Enter>", lambda e: updateTask_button.config(bg="#3B7DD8"))
        ManageNotifications_button.bind("<Leave>", lambda e: updateTask_button.config(bg=accent_color))

        generateReport_button = tk.Button(frame, text="Generate Report", font=general_font, fg=text_color, bg=accent_color,
                                      bd=0, relief="flat", command=create_Report)
        generateReport_button.pack(pady=10, ipadx=20, ipady=5)
        generateReport_button.bind("<Enter>", lambda e: updateTask_button.config(bg="#3B7DD8"))
        generateReport_button.bind("<Leave>", lambda e: updateTask_button.config(bg=accent_color))
    root.mainloop()
