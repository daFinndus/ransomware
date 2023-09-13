import os
import time

from cryptography.fernet import Fernet


# Function to encrypt the files in a folder
def encrypt(folder_path):
    # Saving the amount of files in a variable
    num_files = 0

    # Generate a random key
    key = Fernet.generate_key()

    # Save the encryption key in a file
    with open("filekey.key", "wb") as filekey:
        filekey.write(key)

    # Read the encryption key from the file
    with open("filekey.key", "rb") as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    # Check if the folder exists
    if os.path.exists(folder_path):
        files = os.listdir(folder_path)

        for file_name in files:
            num_files += 1

            # Get the full path of the file within the folder
            file_path = os.path.join(folder_path, file_name)

            with open(file_path, "rb") as file_user:
                original = file_user.read()

            encrypted = fernet.encrypt(original)

            with open(file_path, "wb") as file_encrypted:
                file_encrypted.write(encrypted)
    else:
        print("It seems like the folder isn't there anymore. Please restart the application.")
        time.sleep(3)
        quit()

    print(f"\nDetected an amount of {num_files} files and encrypted every single one of them.")
    print(f"Encryption completed for files in '{folder_path}'.")
    time.sleep(3)

    return key
