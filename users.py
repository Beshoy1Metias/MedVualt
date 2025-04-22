import json
import os
import bcrypt

USER_DB_PATH = "data/users.json"

def load_users():
    if not os.path.exists(USER_DB_PATH):
        return {}
    with open(USER_DB_PATH, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_DB_PATH, "w") as f:
        json.dump(users, f)

def register_user(username, password):
    users = load_users()
    if username in users:
        return False, "Username already exists."
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    users[username] = hashed.decode()
    save_users(users)
    return True, "User registered successfully."

def login_user(username, password):
    users = load_users()
    if username not in users:
        return False, "User not found."
    hashed = users[username].encode()
    if bcrypt.checkpw(password.encode(), hashed):
        return True, "Login successful!"
    else:
        return False, "Incorrect password."