import time

import encrypt
import fake

confirmation = input("Hey, do you wanna create a encryption sample? [Y/N] ")

if confirmation.lower() == "y" or confirmation.lower() == "yes":
    folder_path = fake.fake()
    print(f"\nWe got this folder path: {folder_path}\n")
    time.sleep(3)
    print("Your files are now created on the desktop.")
    time.sleep(1)
    encryption_confirmation = input("\nDo you wanna encrypt them now? [Y/N] ")
    if encryption_confirmation.lower() == "y" or confirmation.lower() == "yes":
        encrypt.encrypt(folder_path)
    elif encryption_confirmation.lower() == "n" or encryption_confirmation.lower() == "no":
        print("\nOkay. We will stop the program, you will have a new folder generated on your desktop.")
        print("To showcase the encryption process restart the program. Your folder will be reused.")
        time.sleep(3)
        exit()
    else:
        print("Sorry, I wasn't able to understand your input.")
        time.sleep(1)
        print("The application will close now.")
        time.sleep(3)
        exit()
elif confirmation.lower() == "n" or confirmation.lower() == "no":
    print("Okay, have a great day tho!")
    time.sleep(3)
    exit()
else:
    print("Sorry, I wasn't able to understand your input.")
    time.sleep(1)
    print("The application will close now.")
    time.sleep(3)
    exit()
