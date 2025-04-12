import tkinter as tk
from tkinter import ttk, messagebox
from styles import *
import requests
from Login.auth import load_users
from Tasks.db_queries import *
from Keys import TELEGRAM_BOT_TOKEN
import globals

def send_telegram_message(chat_id, message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        print(f"Error sending message: {response.status_code}, {response.text}")


def notify_users_about_tasks(task_list, title):
    users = load_users()
    user_tasks = {}

    for task in task_list:
        user = task["assigned_user"]
        if user not in user_tasks:
            user_tasks[user] = []
        user_tasks[user].append(task)

    for username, tasks in user_tasks.items():
        chat_id = users.get(username, {}).get("chat_id")
        if chat_id:
            message = f"{title} for {username}:"
            for task in tasks:
                message += f"• {task['title']} (Due: {task['deadline']})\n"
            send_telegram_message(chat_id, message)
        else:
            print(f"Error: No chat_id found for user: {username}")
            messagebox.showerror("Error", f"No chat_id found for user: {username}")
            return

def notify_user_new_task(username, title, deadline):
    users = load_users()
    chat_id = users.get(username, {}).get("chat_id")
    if chat_id:
        message = f"You have a new task assigned: {title} (Due: {deadline})"
        send_telegram_message(chat_id, message)
        return
    else:
        print(f"Error: No chat_id found for user: {username}")
        messagebox.showerror("Error", f"No chat_id found for user: {username}")
        return

def notifications_form():
    def back_to_Menu():
        from Menu.Menu import form_Menu
        root.destroy()
        form_Menu(globals.user_role)

    def send_upcoming_tasks():
        selected_user = user_var.get()
        if not selected_user:
            messagebox.showerror("Error", "Please select a user")
            return
        tasks = get_user_upcoming_tasks(selected_user)
        if tasks:
            notify_users_about_tasks(tasks, "Upcoming Tasks")
            messagebox.showinfo("Sent", f"Upcoming tasks sent to {selected_user}")
            return
        else:
            messagebox.showinfo("No Tasks", f"No upcoming tasks for {selected_user}")
            return

    def send_overdue_tasks():
        selected_user = user_var.get()
        if not selected_user:
            messagebox.showerror("Error", "Please select a user")
            return
        tasks = get_user_due_tasks(selected_user)
        if tasks:
            notify_users_about_tasks(tasks, "Overdue Tasks")
            messagebox.showinfo("Sent", f"Overdue tasks sent to {selected_user}")
            return
        else:
            messagebox.showinfo("No Tasks", f"No overdue tasks for {selected_user}")
            return

    users = load_users()
    user_names = list(users.keys())

    root = tk.Tk()
    root.title("Task Notifications")
    root.geometry("800x600")
    #root.attributes('-fullscreen', True)
    root.config(bg=bg_color)

    frame = tk.Frame(root, bg="#1E1E2E")
    frame.pack(expand=True)

    label = tk.Label(frame, text="Select User", font=title_font, bg=bg_color, fg=text_color)
    label.pack(pady=20)

    user_var = tk.StringVar()
    user_dropdown = ttk.Combobox(frame, textvariable=user_var, values=user_names, font=general_font)
    user_dropdown.pack(pady=10, ipadx=20, ipady=5)

    upcoming_button = tk.Button(frame, text="Upcoming Tasks", font=general_font, fg=text_color, bg=accent_color, bd=0,
                                 relief="flat", command=send_upcoming_tasks)
    upcoming_button.pack(pady=10, ipadx=20, ipady=5)

    overdue_button = tk.Button(frame, text="Overdue Tasks", font=general_font, fg=text_color, bg=accent_color, bd=0,
                                relief="flat", command=send_overdue_tasks)
    overdue_button.pack(pady=10, ipadx=20, ipady=5)

    back_button = tk.Button(frame, text="Back to Menu", font=general_font, fg=text_color, bg=accent_color, bd=0,
                             relief="flat", command=back_to_Menu)
    back_button.pack(pady=40, ipadx=20, ipady=5)

    root.mainloop()
