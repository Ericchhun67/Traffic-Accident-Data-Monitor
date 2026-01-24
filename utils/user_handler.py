# utils/user_handler.py
"""
user_handler.py
------------------------------------
Handles user authentication and account management for
Traffic & Accident Data Monitor.

Functions:
    - register_user()
    - login_user()
    - reset_password()
    - get_user_by_email()
"""

import os
import sys
import sqlite3
from contextlib import closing


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.db_handler import DB_PATH 


def register_user(username, email, password):
    """Registers a new user into the database."""
    try:
        with closing(sqlite3.connect(DB_PATH)) as conn:
            cursor = conn.cursor()

            # Check if email already exists
            cursor.execute("SELECT id FROM users WHERE username = ? or email = ? ", (username, email))
            if cursor.fetchone():
                return {"status": "fail", "message": "Username or email already taken."}

            cursor.execute("""
                INSERT INTO users (username, email, password)
                VALUES (?, ?, ?)
            """, (username, email, password))
            conn.commit()

        print(f"[INFO] User '{username}' registered successfully.")
        return {"status": "success", "message": f"User {username} registered successfully."}

    except Exception as e:
        print(f"[ERROR] Registration failed: {e}")
        return {"status": "fail", "message": f"Registration failed: {e}"}



def login_user(username, password):
    """Authenticates a user by checking their email and password."""
    try:
        with closing(sqlite3.connect(DB_PATH)) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT username, password FROM users
                WHERE username = ?
            """, (username,))
            result = cursor.fetchone()

            if not result:
                return {"status": "fail", "message": "Username not found."}

            stored_username, stored_password = result

            if password == stored_password:
                print(f"[INFO] User '{stored_username}' logged in successfully.")
                return {"status": "success", "username": stored_username}
            else:
                return {"status": "fail", "message": "Incorrect password."}

    except Exception as e:
        print(f"[ERROR] Login failed: {e}")
        return {"status": "fail", "message": f"Login failed: {e}"}


def get_user_by_email(email):
    """Fetches a user's record using their email address."""
    try:
        with closing(sqlite3.connect(DB_PATH)) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, username, email FROM users WHERE email = ?
            """, (email,))
            result = cursor.fetchone()

            if result:
                return {"id": result[0], "username": result[1], "email": result[2]}
            return None

    except Exception as e:
        print(f"[ERROR] Failed to fetch user by email: {e}")
        return None


def logout_user(session):
    """ logs out the user by clearing their session data and returning the 
        user to the login page.
    """
    try:
        session.pop('user', None)
        print("[INFO] User logged out successfully.")
        return {"status": "success", "message": "User logged out successfully."}
    except Exception as e:
        print(f"Error: logout failed: {e}")
        return {"status": "fail", "message": f"logout failed: {e}"}


def reset_password(email):
    """ Resets users password given their email address. """
    try:
        with closing(sqlite3.connect(DB_PATH)) as conn:
            cursor = conn.cursor()
            # check if email exists
            cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
            user = cursor.fetchone()
            
            if not user:
                return {"status": "fail", "message": "Email not found. "}
            
            print(f"[INFO] Password reset link sent to {email} (simulated).")
            return {"status": "success", "message": f"Password reset link sent to email."}
    except Exception as e:
        print(f"[Error] password reset failed: try again {e}")
        return {"status": "fail", "message": f"password reset failed: {e}"}
    
    
    