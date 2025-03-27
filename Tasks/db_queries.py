from tkinter import messagebox
import mysql.connector
from config import db_config


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
