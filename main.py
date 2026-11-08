from modules.hashing import verifier
from modules.encryption import encryption, decryption
from modules.password import hashed_pw, pw_strength, verify_pw
from getpass import getpass


def menu():
    print("________________________________________\n")
    print("WELCOME TO CYBERSECURITY TOOL KIT\n\n1. File Integrity checker\n2. Message Encryption\n3. Message Decryption\n4. Password Strength Checker\n5. Password Verifier\n6. Exit")
    print("________________________________________")
    return

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter your Choice to continue : ")
        if choice == "1":
            file1 = input("Enter URL of First File : ")
            file2 = input("Enter URL of Second File : ")
            verifier(file1,file2)
            continue
        elif choice == "2":
            text = input("Enter you Message : ")
            print(f"Encrypted Message : {encryption(text)}")
            continue
        elif choice == "3":
            text = input("Enter Encrypted Text : ")
            key = input("Enter Key : ")
            print(f"Original Message : {decryption(key,text)}")
            continue
        elif choice == "4":
            password = getpass("Enter Password : ")
            print(pw_strength(password))
            continue
        elif choice == "5":
            password = getpass("Enter Password : ")
            pw_attempt = getpass("Re-enter the password : ")
            print(verify_pw(pw_attempt,hashed_pw(password)))
            continue
        elif choice == "6":
            break
        else:
            print("Wrong Choice....")
            continue

