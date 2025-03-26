import tkinter as tk
from Tasks.CreateTasks import create_task

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
        root.destroy()
        create_task()

    # Contenedor principal (frame)
    frame = tk.Frame(root, bg="#1E1E2E")
    frame.pack(expand=True)

    # Título de bienvenida
    label = tk.Label(frame, text="Welcome!", font=("Poppins", 20, "bold"), bg="#1E1E2E", fg="#FFFFFF")
    label.pack(pady=30)

    # Botón para mostrar todas las tareas
    showTask_button = tk.Button(frame, text="Show All Task", font=("Poppins", 14), fg="#FFFFFF", bg="#4D96FF", bd=0, relief="flat", command=root.destroy)
    showTask_button.pack(pady=10, ipadx=20, ipady=5)
    showTask_button.bind("<Enter>", lambda e: showTask_button.config(bg="#3B7DD8"))
    showTask_button.bind("<Leave>", lambda e: showTask_button.config(bg="#4D96FF"))

    # Botón para completar tareas
    completeTask_button = tk.Button(frame, text="Complete Task", font=("Poppins", 14), fg="#FFFFFF", bg="#4D96FF", bd=0, relief="flat", command=root.destroy)
    completeTask_button.pack(pady=10, ipadx=20, ipady=5)
    completeTask_button.bind("<Enter>", lambda e: completeTask_button.config(bg="#3B7DD8"))
    completeTask_button.bind("<Leave>", lambda e: completeTask_button.config(bg="#4D96FF"))

    # Botón de logout
    close_button = tk.Button(frame, text="Logout", font=("Poppins", 14), fg="#FFFFFF", bg="#F34336", bd=0, relief="flat", command=back_to_login)
    close_button.pack(pady=30, ipadx=20, ipady=5)
    close_button.bind("<Enter>", lambda e: close_button.config(bg="#D9372A"))
    close_button.bind("<Leave>", lambda e: close_button.config(bg="#F34336"))

    # Func Admin (if role == 1)
    if role == 1:
        labelAdmin = tk.Label(frame, text="Admin Functions:", font=("Poppins", 16), bg="#1E1E2E", fg="#FFFFFF")
        labelAdmin.pack(pady=30)

        addUser_button = tk.Button(frame, text="Add User", font=("Poppins", 14), fg="#FFFFFF", bg="#4D96FF", bd=0, relief="flat", command=root.destroy)
        addUser_button.pack(pady=10, ipadx=20, ipady=5)
        addUser_button.bind("<Enter>", lambda e: addUser_button.config(bg="#3B7DD8"))
        addUser_button.bind("<Leave>", lambda e: addUser_button.config(bg="#4D96FF"))

        createTask_button = tk.Button(frame, text="Create Task", font=("Poppins", 14), fg="#FFFFFF", bg="#4D96FF", bd=0, relief="flat", command=createTask)
        createTask_button.pack(pady=10, ipadx=20, ipady=5)
        createTask_button.bind("<Enter>", lambda e: createTask_button.config(bg="#3B7DD8"))
        createTask_button.bind("<Leave>", lambda e: createTask_button.config(bg="#4D96FF"))

        deleteTask_button = tk.Button(frame, text="Delete Task", font=("Poppins", 14), fg="#FFFFFF", bg="#4D96FF", bd=0, relief="flat", command=root.destroy)
        deleteTask_button.pack(pady=10, ipadx=20, ipady=5)
        deleteTask_button.bind("<Enter>", lambda e: deleteTask_button.config(bg="#3B7DD8"))
        deleteTask_button.bind("<Leave>", lambda e: deleteTask_button.config(bg="#4D96FF"))

        updateTask_button = tk.Button(frame, text="Update Task", font=("Poppins", 14), fg="#FFFFFF", bg="#4D96FF", bd=0, relief="flat", command=root.destroy)
        updateTask_button.pack(pady=10, ipadx=20, ipady=5)
        updateTask_button.bind("<Enter>", lambda e: updateTask_button.config(bg="#3B7DD8"))
        updateTask_button.bind("<Leave>", lambda e: updateTask_button.config(bg="#4D96FF"))

    root.mainloop()
