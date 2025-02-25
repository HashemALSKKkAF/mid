import os
import sqlite3
import hashlib

# 🚨 Hardcoded secret (Sensitive Data Exposure)
SECRET_KEY = "my_secret_password"

def insecure_sql_login(username, password):
    # 🚨 SQL Injection vulnerability (User input is directly concatenated into SQL query)
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    
    user = cursor.fetchone()
    conn.close()
    
    if user:
        print("Login successful!")
    else:
        print("Invalid credentials.")

def insecure_command_execution(user_input):
    # 🚨 Command Injection (User input is passed directly into OS command)
    os.system(f"echo {user_input}")

def weak_hashing(password):
    # 🚨 Weak hashing algorithm (MD5 is not secure)
    return hashlib.md5(password.encode()).hexdigest()

# Example usage with vulnerable inputs
if __name__ == "__main__":
    print("Testing vulnerable Python script...")

    # Simulating SQL Injection attack
    insecure_sql_login("admin", "' OR '1'='1")  # 🚨 SQL Injection payload

    # Simulating Command Injection
    insecure_command_execution("test; rm -rf /")  # 🚨 Could delete files if run as root

    # Storing password with weak hashing
    hashed_password = weak_hashing("mypassword")
    print(f"Weak hashed password: {hashed_password}")
