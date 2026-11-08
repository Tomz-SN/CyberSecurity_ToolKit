# Cybersecurity Toolkit

A Python-based cybersecurity toolkit that combines XOR-based message encryption and decryption along with password strength validation.

## Key Features

### 1. Message Encryption
- Generates a random encryption key using Python's `secrets` module.
- Uses the bitwise XOR operation to encrypt messages.
- Converts encrypted data into hexadecimal representation.
- Automatically saves the generated key in a separate text file.

### 2. Message Decryption
- Accepts an encrypted message and its corresponding key.
- Converts hexadecimal values back into bytes.
- Reverses the XOR operation to recover the original message.

### 3. Password Strength Checker
- Evaluates password strength using the `zxcvbn` library.
- Assigns a strength score from 0 to 4.
- Provides feedback based on the estimated password strength.

## Project Structure

```text
Cybersecurity-Toolkit/
│
├── main.py
│
├── modules/
│   ├── encryption.py
│   └── password.py
│
├── keys.txt
│
└── README.md
```

## How It Works

### Message Encryption

1. The user enters a message.
2. The message is converted into bytes.
3. A random key of equal byte length is generated.
4. The message bytes and key bytes undergo a bitwise XOR operation.
5. The encrypted result is converted into hexadecimal format.
6. The generated key is saved in `keys.txt`.
7. The encrypted message is displayed in the terminal.

### Message Decryption

1. The user provides the encrypted message.
2. The corresponding encryption key is entered.
3. Both hexadecimal strings are converted back into bytes.
4. The XOR operation is performed using the same key.
5. The resulting bytes are decoded to recover the original message.

### Password Strength Assessment

1. The user enters a password.
2. The password is evaluated using `zxcvbn`.
3. The library returns a score between 0 and 4.
4. The application displays feedback based on the score.

### Note

1. Install libraries zxcvbn,pwinput
2. Do decrypt the message key can be found at 'keys.txt'
3. 'keys.txt' file is in write mode, so after next use of encryption function, the previous key is deleted. 

## Project Information

**Project Name:** Cybersecurity Toolkit  
**Programming Language:** Python only
**AI-Usage** : For debugging and also for creating 'README.md' Base structure. VS-code Copilot
**Concepts Learned** : Source : https://youtu.be/kb_scuDUHls

**Developed as a Python-based cybersecurity project for First Year CS hackathon.**
