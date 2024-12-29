# app/main.py

from app.database import setup_database  # Import the database setup function
from app.gui import run_gui  # Import the GUI function

def main():
    """
    The main entry point for the application.
    - Sets up the database.
    - Runs the GUI for the password manager.
    """
    # Initialize the database (create tables if they don't exist)
    setup_database()

    # Run the GUI application
    run_gui()

if __name__ == "__main__":
    main()
