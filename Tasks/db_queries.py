from tkinter import messagebox
import mysql.connector
from config import db_config
from datetime import datetime, timedelta


def connect_db():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Connection Error!: {err}")
        return None


def save_task(title, priority, description, state, deadline, assigned_user):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()

            # SQL para insertar la tarea con el nombre del usuario asignado
            sql = "INSERT INTO Tasks (title, priority, description, state, deadline, assigned_user) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (title, priority, description, state, deadline, assigned_user)
            cursor.execute(sql, values)
            conn.commit()
            messagebox.showinfo("Done", "Task saved successfully!")
        except mysql.connector.Error as err:
            messagebox.showinfo("Error!", "Error: " + str(err))
        finally:
            cursor.close()
            conn.close()


def get_tasks():
    conn = connect_db()
    tasks = []
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Tasks")
            tasks = cursor.fetchall()
        except mysql.connector.Error as err:
            messagebox.showinfo("There is something wrong!", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()
    return tasks

def get_user_tasks(user_name):
    conn = connect_db()
    tasks = []
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Tasks WHERE assigned_user = %s", (user_name,))
            tasks = cursor.fetchall()
        except mysql.connector.Error as err:
            messagebox.showinfo("There is something wrong!", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()
    return tasks

def get_user_tasks_DONE(user_name):
    conn = connect_db()
    tasks = []
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Tasks WHERE assigned_user = %s AND state != 'Done'", (user_name,))
            tasks = cursor.fetchall()
        except mysql.connector.Error as err:
            messagebox.showinfo("There is something wrong!", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()
    return tasks

def get_task_description(task_id):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT description FROM Tasks WHERE id = %s"
            cursor.execute(query, (task_id,))
            result = cursor.fetchone()
            return result["description"] if result else "No description available."
        except mysql.connector.Error as err:
            print(f"Error fetching task description: {err}")
            return "Error fetching description."
        finally:
            cursor.close()
            conn.close()
    return "Database connection error."

def change_ToDone(task_id):
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

def update_task_query(task_id, title, priority, description, state, deadline, assigned_user):
    try:
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            update_query = """
                UPDATE Tasks
                SET title = %s, priority = %s, description = %s, state = %s, deadline = %s, assigned_user = %s
                WHERE id = %s
            """
            cursor.execute(update_query, (title, priority, description, state, deadline, assigned_user, task_id))
            conn.commit()
            cursor.close()
            conn.close()
            return True
    except mysql.connector.Error as err:
        print(f"Error updating task: {err}")
        return False

def deleteTask(task_id):
    try:
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            deleteQuery = "DELETE FROM tasks WHERE id = %s"

            cursor.execute(deleteQuery, (task_id,))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Done", "Task deleted successfully!")
            return True
    except mysql.connector.Error as err:
        messagebox.showinfo("UhUh", f"Error: {err}")
        return False

def get_user_due_tasks(user_name):
    conn = connect_db()
    tasks = []
    today = datetime.now().date()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Tasks WHERE deadline < %s AND state != 'Done' AND assigned_user = %s", (today, user_name))
            tasks = cursor.fetchall()
        finally:
            cursor.close()
            conn.close()
    return tasks


def get_user_upcoming_tasks(user_name):
    conn = connect_db()
    tasks = []
    today = datetime.now().date()
    tomorrow = today + timedelta(days=1)
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Tasks WHERE deadline BETWEEN %s AND %s AND state != 'Done' AND assigned_user = %s", (today, tomorrow, user_name))
            tasks = cursor.fetchall()
        finally:
            cursor.close()
            conn.close()
    return tasks



