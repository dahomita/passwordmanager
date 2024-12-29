# app/gui.py

import tkinter as tk
from tkinter import messagebox
from app.password_utils import generate_password  # Import the password generation function

def run_gui():
    """
    Run the Tkinter GUI for the password manager.
    """
    # Create the main window
    root = tk.Tk()
    root.title("Password Manager")

    # Set window size
    root.geometry("400x400")

    # Add a label to the window
    label = tk.Label(root, text="Welcome to the Password Manager!", font=("Arial", 16))
    label.pack(pady=20)

    # Function to handle password generation
    def generate_and_display_password():
        # Get the password length from the entry field
        length = int(password_length_entry.get())
        # Generate a password
        new_password = generate_password(length=length)
        # Display the generated password in the label
        generated_password_label.config(text=f"Generated Password: {new_password}")

    # Add an entry for the password length
    password_length_label = tk.Label(root, text="Password Length:")
    password_length_label.pack(pady=5)
    password_length_entry = tk.Entry(root)
    password_length_entry.insert(0, "12")  # Default length
    password_length_entry.pack(pady=5)

    # Add a button to generate the password
    generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
    generate_button.pack(pady=10)

    # Label to display the generated password
    generated_password_label = tk.Label(root, text="Generated Password: None", font=("Arial", 12))
    generated_password_label.pack(pady=20)

    # Add a button to quit the application
    quit_button = tk.Button(root, text="Quit", command=root.quit)
    quit_button.pack(pady=10)

    # Start the GUI loop
    root.mainloop()
