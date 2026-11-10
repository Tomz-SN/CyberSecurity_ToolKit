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
if __name__ == "__main__":
    while True:
        
            menu()
            choice = input("\nEnter your Choice to continue : ").strip()

            if choice == "1":
                text = input("\nEnter you Message : ")
                try:
                    if not text.strip():
                        print("Message Should Not be empty")
                    else:
                        print(f"Encrypted Message : {encryption(text)}")
                except:
                    print("Encryption Failed")

            elif choice == "2":
                text = input("\nEnter Encrypted Text : ").strip()
                key = input("Enter Key : ").strip()
                try:
                    if not key or not text:
                        print("Both Key and Text should not be empty")
                    elif len(key) != len(text):
                        print("Entered Key and Encrypted Text length are different")
                    else:
                        print(f"Original Message : {decryption(key,text)}")
                except:
                    print("Decryption Failed...Incorrect key or Encrypted text is altered")

            elif choice == "3":
                password = pwinput.pwinput(prompt = "\nEnter Password : ", mask ="*")
                if not password:
                    print("Password Cannot be empty")
                else:
                    print(pw_strength(password))

            elif choice == "4":
                print("Exiting the program...")
                break

            else:
                print("Wrong Choice....")

