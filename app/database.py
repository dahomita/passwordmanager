# SQLite database interactions

import sqlite3
from app.config import DATABASE_NAME

def connect():
    """Establish a connection to the SQLite database."""
    return sqlite3.connect(DATABASE_NAME)

def setup_database():
    """Create the credentials table if it doesn't exist."""
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()

def add_credential(website, username, password):
    """
    Add a new credential to the database.
    :param website: The website or application name.
    :param username: The username associated with the website.
    :param password: The encrypted password.
    """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO credentials (website, username, password) VALUES (?, ?, ?)",
                   (website, username, password))
    connection.commit()
    connection.close()

def get_credential(website):
    """
    Retrieve a credential by website.
    :param website: The website name to search for.
    :return: A tuple (username, password) if found, otherwise None.
    """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT username, password FROM credentials WHERE website = ?", (website,))
    result = cursor.fetchone()
    connection.close()
    return result

def update_credential(website, username, password):
    """
    Update the username and/or password for a specific website.
    :param website: The website name to update.
    :param username: The new username.
    :param password: The new encrypted password.
    """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE credentials
        SET username = ?, password = ?
        WHERE website = ?
    """, (username, password, website))
    connection.commit()
    connection.close()

def delete_credential(website):
    """
    Delete a credential by website.
    :param website: The website name to delete.
    """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM credentials WHERE website = ?", (website,))
    connection.commit()
    connection.close()

def get_all_credentials():
    """
    Retrieve all stored credentials.
    :return: A list of tuples containing all credentials.
    """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT website, username, password FROM credentials")
    results = cursor.fetchall()
    connection.close()
    return results

