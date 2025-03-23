
import tkinter as tk


def form_Menu(role):
    root = tk.Tk()
    root.geometry("400x300") 
    root.title("Menu")

    def back_to_login():
        root.destroy()
        from Login.login import ModernLogin
        ModernLogin()

    label = tk.Label(root, text="Welcome!", font=("Poppins", 16))
    label.pack(pady=50)

    showTask_button = tk.Button(root, text="Show All Task", command=root.destroy)
    showTask_button.place(relx=0.90, rely=0.30, anchor="se")

    completeTask_button = tk.Button(root, text="Complete Task", command=root.destroy)
    completeTask_button.place(relx=0.90, rely=0.50, anchor="se")

    close_button = tk.Button(root, text="Logout", command=back_to_login,)
    close_button.place(relx=0.90, rely=0.90, anchor="se")

    if role == 1:
        labelAdmin = tk.Label(root, text="Admin Functions:", font=("Poppins", 16))
        labelAdmin.pack(pady=30)

        addUser_button = tk.Button(root, text="Add User", command=root.destroy)
        addUser_button.place(relx=0.30, rely=0.30, anchor="se")

        createTask_button = tk.Button(root, text="Create Task", command=root.destroy)
        createTask_button.place(relx=0.30, rely=0.50, anchor="se")

        deleteTask_button = tk.Button(root, text="Delete Task", command=root.destroy)
        deleteTask_button.place(relx=0.30, rely=0.70, anchor="se")

        updateTask_button = tk.Button(root, text="Delete Task", command=root.destroy)
        updateTask_button.place(relx=0.30, rely=0.70, anchor="se")

    root.mainloop()



