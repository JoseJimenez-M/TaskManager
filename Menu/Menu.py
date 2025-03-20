
import tkinter as tk

def form_Menu():
    root = tk.Tk()
    root.geometry("400x300") 
    root.title("Menu")
    
    label = tk.Label(root, text="Welcome!", font=("Poppins", 16))
    label.pack(pady=50)

    close_button = tk.Button(root, text="Cerrar", command=root.destroy)
    close_button.pack(pady=20)

    root.mainloop() 

