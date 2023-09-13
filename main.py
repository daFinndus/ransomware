import os
import time

import decrypt
import encrypt
import fake

# Check if the user really wants to execute the application
confirmation = input("Hey, do you wanna create a encryption sample? [y/n] ")

if confirmation.lower() == "y" or confirmation.lower() == "yes":
    # Create a folder to use for the encryption process
    folder_path = fake.fake()

    # Check if all files are encrypted
    if decrypt.check_status(folder_path):
        # Ask if the files should be decrypted
        decryption_confirmation = input("\nWe noticed your files are already encrypted. Do you wanna decrypt them now? [y/n] ")

        if decryption_confirmation.lower() == "y" or decryption_confirmation.lower() == "yes":
            decrypt.decrypt(folder_path)
        elif decryption_confirmation.lower() == "n" or decryption_confirmation.lower() == "no":
            print("Okay. Your files will stay encrypted. Execute the application again to decrypt them!")
            time.sleep(3)
            quit()
        else:
            print("Sorry, I cannot recognize your input. The app will quit now.")
            time.sleep(3)
            quit()
    else:
        # Ask if the files should be encrypted
        encryption_confirmation = input("\nDo you wanna encrypt them now? [y/n] ")

        if encryption_confirmation.lower() == "y" or confirmation.lower() == "yes":
            # Encrypt each file of the certain folder
            encrypt.encrypt(folder_path)
        elif encryption_confirmation.lower() == "n" or encryption_confirmation.lower() == "no":
            print("\nOkay. We will stop the program, you will have a new folder generated on your desktop.")
            print("To showcase the encryption process restart the program. Your folder will be reused.")
            time.sleep(3)
            quit()
        else:
            print("Sorry, I wasn't able to understand your input.")
            time.sleep(1)
            print("The application will close now.")
            time.sleep(3)
            quit()
elif confirmation.lower() == "n" or confirmation.lower() == "no":
    print("Okay, have a great day tho!")
    time.sleep(3)
    quit()
else:
    print("Sorry, I wasn't able to understand your input.")
    time.sleep(1)
    print("The application will close now.")
    time.sleep(3)
    quit()
