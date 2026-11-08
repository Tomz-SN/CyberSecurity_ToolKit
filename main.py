from modules.encryption import encryption, decryption
from modules.password import pw_strength
import pwinput

# Menu for user to select option

def menu():
    print("________________________________________\n")
    print("WELCOME TO CYBERSECURITY TOOL KIT\n\n1. Message Encryption\n2. Message Decryption\n3. Password Strength Checker\n4. Exit")
    print("________________________________________")
    return

# Menu repeats till user give choice as 4

while True:
        menu()
        choice = input("\nEnter your Choice to continue : ")
        if choice == "1":
            text = input("\nEnter you Message : ")
            print(f"Encrypted Message : {encryption(text)}")
            continue
        elif choice == "2":
            text = input("\nEnter Encrypted Text : ")
            key = input("Enter Key : ")
            print(f"Original Message : {decryption(key,text)}")
            continue
        elif choice == "3":
            password = pwinput.pwinput(prompt = "\nEnter Password : ", mask ="*")
            print(pw_strength(password))
            continue
        elif choice == "4":
            break
        else:
            print("Wrong Choice....")
            continue

