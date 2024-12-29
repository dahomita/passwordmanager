# app/config.py

import os

# Encryption key (store securely in production)
# In production, you should fetch this from an environment variable or secure storage
ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY', b'thongminhtam')  # Default for development

# Database file (use platform-independent path)
DATABASE_NAME = "password_manager.db"
DATABASE_PATH = os.path.join(os.path.dirname(__file__), DATABASE_NAME)

# Other configuration constants
APP_NAME = "Password Manager"
APP_VERSION = "1.0.0"
