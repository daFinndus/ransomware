import os
import time

import cryptography.fernet
from cryptography.fernet import Fernet


# Function to get the key from the file, which should be created in the encryption process
def get_key():
    key = "MJ_fXlA75LPFzul9IcJrvIj7z9kvJTpO8hVpzZ5kmXg="

    # Try to open the file where the cryptography key should be stored
    try:
        with open("filekey.key", "rb") as filekey:
            # Save the file content in a variable
            key = filekey.read()

    except FileNotFoundError:
        print("\nSorry, but the file where the key should be stored, doesn't exist. We will proceed with a random key.")
        time.sleep(3)

    return key


# Function to check if a single file is encrypted
def is_encrypted(file_path):
    fernet = Fernet(get_key())

    with open(file_path, "rb") as file:
        try:
            file_content = file.read()
            fernet.decrypt(file_content)
            return True
        except cryptography.fernet.InvalidToken:
            return False


# Function to check if all files are encrypted
def check_status(folder_path):
    files = os.listdir(folder_path)

    encryption_status = all(is_encrypted(os.path.join(folder_path, file)) for file in files)

    return encryption_status


def decrypt(folder_path):
    # Saving the amount of files in a variable
    num_files = 0

    # Check if the folder exists
    if os.path.exists(folder_path):
        # Store all the existing files in the folder in a list
        files = os.listdir(folder_path)

        fernet = Fernet(get_key())

        # Execute the following lines for every file
        for file_name in files:
            num_files += 1

            # Create a path based on the os
            file_path = os.path.join(folder_path, file_name)

            # Write the encrypted content to a variable
            with open(file_path, "rb") as file_encrypted:
                encrypted_content = file_encrypted.read()

            # Decrypt the content and store it in a variable
            decrypted_content = fernet.decrypt(encrypted_content)

            # Rewrite the original file with the decrypted content
            with open(file_path, "wb") as file_decrypted:
                file_decrypted.write(decrypted_content)
    print(f"\nSuccessfully decrypted {num_files} files and stored them in the original folder.")
    time.sleep(1)
    print("The process is complete and will quit now.")
    time.sleep(3)
    quit()
