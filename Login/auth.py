import bcrypt
import json
import os

USERS_FILE = os.path.join(os.path.dirname(__file__), "users.json")

# Chech or create(if doesn't exist)
def exist_file():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w') as file:
            json.dump({}, file)

# Create hash
def create_user(username, password, role):
    users = load_users()

    if username in users:
        raise ValueError("User already exist")
    
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())  # hash
    users[username] = {
        "password": hashed_password.decode('utf-8'),
        "role": role,
        "chat_id": None
    }  
    save_users(users)

# Load User from file
def load_users():
    if not os.path.exists(USERS_FILE):
        return {} 
    with open(USERS_FILE, 'r') as file:
        return json.load(file)

# Save users
def save_users(users):
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file, indent=2)

# Verify user and password
def validate_user(username, password):
    users = load_users()
    if username not in users:
        return False
    stored_hash = users[username]["password"].encode()
    return bcrypt.checkpw(password.encode(), stored_hash)

## 0 Regular, 1 -> Admin
def get_user_role(username):
    users = load_users()
    if username in users:
        return users[username]["role"]
    return None  # None if user doesnt exist
