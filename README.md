# 🔐 File Integrity Checker

A Python-based cybersecurity tool that uses **SHA-256 cryptographic hashing** to verify file integrity and detect unauthorized modifications.

## 📌 About the Project

The File Integrity Checker is a simple cybersecurity project designed to identify changes between two files by comparing their SHA-256 hash values.

Every file generates a unique hash based on its contents. Even a small modification to a file generally produces a completely different hash.

This project reads files in binary mode, processes them in chunks, generates SHA-256 hashes, and compares the results to determine whether the files have identical contents.

## ⚙️ Features

- **SHA-256 Hashing:** Generates SHA-256 hash values using Python's built-in `hashlib` library.
- **Chunk-Based Reading:** Reads files in 1024-byte chunks to handle large files efficiently.
- **File Integrity Verification:** Compares the hash values of two files.
- **Modification Detection:** Identifies differences between files.
- **Binary File Support:** Supports different file types through binary reading mode.
- **Exception Handling:** Handles missing files using Python's exception handling.

## 🛠️ Technologies Used

- Python 3
- `hashlib` – Cryptographic hashing
- File Handling – Reading files in binary mode
- Exception Handling – Handling file-related errors

## 📂 Project Structure

```text
File-Integrity-Checker/
│
├── main.py
├── README.md
├── .gitignore
│
└── sample_files/
    ├── original.txt
    └── modified.txt
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

### 3. Run the Program

```bash
python main.py
```

### 4. Enter File Paths

When prompted, provide the paths of the two files you want to compare.

Example:

```text
Enter path of First File: sample_files/original.txt
Enter path of Second File: sample_files/modified.txt
```

## 💻 Sample Output

**Case 1: Identical Files**

```text
Both Files are Unaltered
```

**Case 2: Modified Files**

```text
Modification Detected
```

## 🔍 How It Works

1. The program accepts the paths of two files.
2. Each file is opened in binary read mode (`rb`).
3. The contents are read in chunks of 1024 bytes.
4. Each chunk is passed to a SHA-256 hashing object.
5. The final hash values are generated using `hexdigest()`.
6. Both hash values are compared.
7. The program reports whether the file contents match or differ.

## 📚 Concepts Learned

This project helped me understand and apply:

- Cryptographic hashing and SHA-256.
- Python file handling.
- Binary data processing.
- Functions and modular programming.
- Loops and conditional statements.
- Exception handling.
- Basic cybersecurity concepts.

## ⚠️ Limitations

- The tool compares two files rather than checking a file against a trusted, previously stored hash.
- It does not identify which specific part of a file was modified.
- Matching hashes do not establish the authenticity or safety of a file without a trusted reference.


## 👨‍💻 Author

 Tom Sanson (Tomz-SN)

Computer Science Engineering Student

Interested in Python, Programming and Cybersecurity.

---

*This project was developed as a hands-on learning exercise to explore cryptographic hashing and file integrity verification.*
