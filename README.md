# 🔐 Cryptography Terminal

A menu-driven Python cybersecurity toolkit that demonstrates **hashing, symmetric encryption, asymmetric encryption, and password security** from the command line.

## 📌 About the Project

The Cryptography Terminal brings several core cryptography concepts together in one program. It started as a File Integrity Checker and grew into a toolkit with a simple menu.

You can compare files using SHA-256 hashes, encrypt messages with AES and RSA, check how strong a password is, and verify passwords using bcrypt hashing.

## ⚙️ Features

- **File Integrity Checker:** Compares two files using SHA-256 hashes to detect any modification. Files are read in binary mode in 1024-byte chunks, so large files are handled efficiently.
- **Symmetric Encryption:** Encrypts and decrypts a message with AES-256-GCM using a random key and nonce.
- **Asymmetric Encryption:** Encrypts with an RSA public key and decrypts with the private key (2048-bit key, OAEP padding with SHA-256).
- **Password Strength Checker:** Rates a password from weak to very strong using `zxcvbn`.
- **Password Verifier:** Hashes a password with `bcrypt` and checks a second entry against the hash.
- **Hidden Password Input:** Passwords are read with `getpass`, so they are not shown on screen.
- **Exception Handling:** Handles missing files using Python's exception handling.

## 🛠️ Technologies Used

- Python 3
- `hashlib` – SHA-256 hashing
- `cryptography` – AES-GCM and RSA encryption
- `secrets` – Secure random keys and nonces
- `bcrypt` – Secure password hashing
- `zxcvbn` – Password strength estimation
- `getpass` – Hidden password input

## 📂 Project Structure

```text
File-Integrity-Checker/
│
├── main.py
├── README.md
├── .gitignore
│
└── modules/
    ├── hashing.py
    ├── encryption.py
    └── password.py
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/File-Integrity-Checker.git
```

### 2. Navigate to the Project Directory

```bash
cd File-Integrity-Checker
```

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install cryptography bcrypt zxcvbn
```

### 5. Run the Program

```bash
python main.py
```

### 6. Choose an Option

Enter a number from the menu and follow the prompts.

## 💻 Sample Output

**Menu**

```text
Welcome to the Cryptography Terminal....
1. File Integrity checker
2. Symmetric Encryption
3. Asymmetric Encryption
4. Password Strength Checker
5. Password Verifier
6. Exit
```

**File Integrity Checker**

```text
Both Files are Unaltered
```

```text
Modification Detected
```

**Symmetric Encryption**

```text
Key            : 8343cab8...
Encrypted text : 107642d2...
```

**Asymmetric Encryption**

```text
Encrypted text : 107642d2...
```

**Password Verifier**

```text
Correct Password, Access Granted..
```

## 🔍 How It Works

**File Integrity Checker**
1. The program accepts the paths of two files.
2. Each file is opened in binary read mode (`rb`) and read in 1024-byte chunks.
3. Each chunk is passed to a SHA-256 hashing object.
4. The final hash values are generated using `hexdigest()`.
5. Both hash values are compared, and the program reports whether the contents match.

**Symmetric Encryption (AES-GCM)**
1. A random 256-bit key and a 12-byte nonce are generated.
2. The message is encrypted, and the nonce is attached to the front of the ciphertext.
3. The ciphertext is decrypted again using the same key to confirm the round trip.

**Asymmetric Encryption (RSA)**
1. A 2048-bit private key and its matching public key are generated.
2. The message is encrypted with the public key using OAEP padding.
3. It is decrypted with the private key.

**Password Tools**
1. `zxcvbn` scores the password from 0 to 4 based on patterns and common words.
2. `bcrypt` adds a random salt and hashes the password.
3. A later attempt is hashed the same way and compared with the stored hash.

## 📚 Concepts Learned

This project helped me understand and apply:

- Cryptographic hashing and SHA-256.
- Symmetric vs asymmetric encryption.
- Keys, nonces, salts and padding.
- Password hashing and strength estimation.
- Python file handling and binary data processing.
- Functions, modular programming and imports.
- Exception handling.
- Basic cybersecurity concepts.

## ⚠️ Limitations

- This is a learning project, not production security software.
- Encryption keys are generated fresh on every run and are not saved, so encrypted messages cannot be decrypted later.
- The file checker compares two files rather than checking a file against a trusted, previously stored hash.
- It does not identify which specific part of a file was modified.
- Matching hashes do not establish the authenticity or safety of a file without a trusted reference.

## 👨‍💻 Author

Tom Sanson (Tomz-SN)

---

*This project was developed as a hands-on learning exercise to explore cryptography and file integrity verification.*
