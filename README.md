# TaskManager
Be sure you already have python!

0.-To install, press "windows+r", write "cmd" and paste the commands bellow:

1.-Yo, Here Jose, u gonna need install Tkinter to work,  "pip install Pillow"

2.- Also install "pip install bcrypt"

3.-"pip install tkcalendar"

4.-"pip install mysql-connector-python"

-------------------------------- USERS --------------------------------

Temporal Admin:
User: Jose
Password: 123
Role: 1 (admin)

Temporal User:
User: Test
Password: 123
Role: 0 (Normal User)

--------------------------------
Mysql Database Script:

CREATE DATABASE TaskManager;
USE TaskManager;

CREATE TABLE Tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    priority ENUM('High', 'Medium', 'Low'),
    description TEXT,
    state ENUM('On Hold', 'Done'),
    deadline DATE
    assigned_user VARCHAR(50)
);
--------------------------------
Be sure to put your own data in config.py