from modules.hashing import verifier
from modules.encryption import sym_etn_dtn, asym_etn_dtn
from modules.password import hashed_pw, pw_strength, verify_pw
from getpass import getpass


def menu():
    print("Welcome to the Cryptography Terminal....\n1. File Integrity checker\n2. Symmetric Encryption\n3. Asymmetric Encryption\n4. Password Strength Checker\n5. Password Verifier\n6. Exit")
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
            sym_etn_dtn(text)
            continue
        elif choice == "3":
            text = input("Enter you Message : ")
            asym_etn_dtn(text)
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

