# Module to create some fake files to encrypt

import os
import random
import string

import time


# Function to create a fake folder
def fake():
    # Define the path to the desktop and the folder name
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    folder_name = "College"

    # Combine the paths to create the full path to the folder
    folder_path = os.path.join(desktop_path, folder_name)

    # Create folder if it's not existing yet
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Generate and create random files
    num_files = random.randint(9, 15)

    if not os.listdir(folder_path):
        for i in range(num_files):
            # Generate a random file name
            random_file_name = ''.join(random.choices(string.ascii_letters, k=6)) + ".txt"

            # Create a random file in the folder
            file_path = os.path.join(folder_path, random_file_name)
            with open(file_path, "w") as file:
                file.write("This is a random file.")

        if num_files > 0:
            print(f"\n{num_files} random files have been successfully created in {folder_path} and filled with random content.")
    else:
        print("\nFolder is already filled.")

    print("Fake folder creation is completed.")
    time.sleep(3)
    return folder_path  # Return the folder path after creation
