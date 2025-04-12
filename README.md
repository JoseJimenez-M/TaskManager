# TaskManager

TaskManager is a Python-based task management application designed to help users organize and manage their daily tasks. The app allows users to receive notifications via Telegram, manage tasks, generate reports in Excel/CSV format, and more. It is built using **Tkinter** for the graphical interface, **MySQL** for the database, and the **Telegram Bot API** for notifications.

---

## 📋 TaskManager Overview

TaskManager is a desktop application built with **Tkinter** for the user interface (UI), **MySQL** for database management, and the **Telegram Bot API** for notifications. The app allows administrators to manage tasks, send notifications to users, generate reports, and add new users. Regular users can view their tasks, receive notifications, and track their progress.

### Key Features

#### **For Admin Users:**
- 📝 **Task Management:** Admin users can create, read, update, and delete tasks for users.
- 🧑‍💻 **User Management:** Admins can add, modify, or delete users.
- 💬 **Task Notifications:** Admins can send notifications about pending, upcoming, or overdue tasks to users via Telegram.
- 📊 **Task Reports:** Admins can generate reports in **CSV** or **Excel** format with tasks assigned to users.

#### **For Regular Users:**
- 📅 **View Pending Tasks:** Regular users can view their assigned tasks, along with due dates and task statuses.
- 📲 **Receive Task Notifications:** Users will receive notifications about pending, upcoming, or overdue tasks.
- ✅ **View Completed Tasks:** Users can view the tasks they have completed.

---

## ⚙️ Setup & Installation

### Prerequisites

Before using TaskManager, make sure **Python 3.x** is installed on your computer. If you don't have it, download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Open **Command Prompt** (press `Windows + R`, type `cmd`, and press Enter).
2. Install the required libraries by running the following commands:

```bash
pip install Pillow
pip install bcrypt
pip install tkcalendar
pip install mysql-connector-python
pip install pandas
pip install openpyxl
```
---
### Setting Up the Database
TaskManager uses MySQL to store tasks. Use the following script to create the database and tables:

```
CREATE DATABASE TaskManager;
USE TaskManager;

CREATE TABLE Tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    priority ENUM('High', 'Medium', 'Low'),
    description TEXT,
    state ENUM('On Hold', 'Done'),
    deadline DATE,
    assigned_user VARCHAR(50)
);

CREATE TABLE Users (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(255),
    role INT,
    chat_id VARCHAR(50)
);
```
---
## 📦 Tech Stack
Language: Python

Framework: Tkinter (for UI)

Database: MySQL

Telegram Integration: Telegram Bot API

Libraries: Pillow, bcrypt, tkcalendar, mysql-connector-python, pandas, openpyxl

## 📝 License
This project is licensed under the MIT License. You are free to use, modify, and distribute the code as long as appropriate credit is given.

For commercial use or licensing inquiries, please contact: [jimenez331375@gmail.com]
