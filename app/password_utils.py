from cryptography.fernet import Fernet

# Generate a Fernet key
def generate_fernet_key():
    key = Fernet.generate_key()
    return key

# Example of encrypting and decrypting data
def encrypt_data(data, key):
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data, key):
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data).decode()
    return decrypted_data

# Generate a key and use it
key = generate_fernet_key()
print(f"Generated Key: {key}")

# Encrypt and decrypt an example password
password = "my_secure_password"
encrypted_password = encrypt_data(password, key)
decrypted_password = decrypt_data(encrypted_password, key)

print(f"Encrypted Password: {encrypted_password}")
print(f"Decrypted Password: {decrypted_password}")

# app/password_utils.py

import random
import string

def generate_password(length=12, include_special_chars=True):
    """
    Generates a random password.
    
    :param length: The length of the password (default is 12).
    :param include_special_chars: Whether to include special characters in the password (default is True).
    :return: A randomly generated password string.
    """
    characters = string.ascii_letters + string.digits  # Letters (uppercase + lowercase) and digits
    
    if include_special_chars:
        characters += string.punctuation  # Add special characters
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password
