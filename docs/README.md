# Password Manager

A simple, secure password manager that allows users to generate strong passwords, store them securely, and manage their credentials with encryption.

## Features

- **AES Encryption**: Securely stores passwords using AES encryption.
- **Password Generation**: Generate strong, random passwords with customizable length.
- **Master Password**: A master password is used to access the password manager.
- **Tkinter GUI**: A simple and intuitive graphical user interface built with Tkinter for local use.
- **Web-based API (Optional)**: A web-based version using Flask/Django (coming soon).

## Tech Stack

- **Backend**: Python
- **GUI**: Tkinter (for desktop app)
- **Encryption**: Cryptography (AES encryption)
- **Database**: SQLite (for secure password storage)

## Requirements

Before running the project, ensure you have the following installed:

- Python 3.x
- `cryptography` library for encryption
- `tkinter` library for the GUI (usually comes pre-installed with Python)

You can install the required dependencies with the following:

```bash
pip install cryptography

1. Setup
Clone the repository:
git clone https://github.com/your-username/password-manager.git
cd password-manager

2. Install the required dependencies:
pip install -r requirements.txt

3. Run the application:
For the desktop version with Tkinter: python3 -m app.main