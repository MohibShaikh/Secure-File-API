import os
import base64
from cryptography.fernet import Fernet

# Load encryption key from environment variable
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")

# Validate the encryption key
if ENCRYPTION_KEY is None:
    raise ValueError("ENCRYPTION_KEY is missing. Generate and store a valid key.")

try:
    # Decode and verify if the key is correct
    decoded_key = base64.urlsafe_b64decode(ENCRYPTION_KEY)

    if len(decoded_key) != 32:
        raise ValueError("ENCRYPTION_KEY must be exactly 32 bytes when decoded.")

    cipher = Fernet(ENCRYPTION_KEY)  # Ensure correct encoding
except Exception as e:
    raise ValueError(f"Invalid ENCRYPTION_KEY: {e}")


def encrypt_file(file_path):
    """
    Encrypts a file and saves it as a new file.
    """
    try:
        with open(file_path, "rb") as f:
            file_data = f.read()

        encrypted_data = cipher.encrypt(file_data)

        encrypted_file_path = file_path + ".encrypted"  # Save as new file
        with open(encrypted_file_path, "wb") as f:
            f.write(encrypted_data)

        print(f"File encrypted successfully: {encrypted_file_path}")
        return encrypted_file_path
    except Exception as e:
        raise ValueError(f"Failed to encrypt file: {e}")


def decrypt_file(file_path):
    """
    Decrypts an encrypted file and saves the decrypted data to a new file.
    """
    try:
        with open(file_path, "rb") as f:
            encrypted_data = f.read()

        # Check if the file is valid Fernet-encrypted data
        try:
            base64.urlsafe_b64decode(encrypted_data)  # Check base64 validity
        except Exception:
            raise ValueError("File does not appear to be encrypted or is corrupted.")

        decrypted_data = cipher.decrypt(encrypted_data)

        decrypted_file_path = file_path.replace(".encrypted", "") + ".decrypted"
        with open(decrypted_file_path, "wb") as f:
            f.write(decrypted_data)

        print(f"File decrypted successfully: {decrypted_file_path}")
        return decrypted_file_path
    except Exception as e:
        raise ValueError(f"Failed to decrypt file: {e}")


def generate_key():
    """
    Generates a new encryption key using the Fernet algorithm.

    Returns:
        str: A new encryption key.
    """
    key = Fernet.generate_key()
    return key.decode()


