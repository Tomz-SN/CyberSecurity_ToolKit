import hashlib

def hashed_value(file_url):
    hash_obj = hashlib.sha256()
    with open(file_url, "rb") as file:
        while True:
            chunk = file.read(1024)
            if chunk == b"":
                break
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

def verifier(file1,file2):
    hash1 = hashed_value(file1)
    hash2 = hashed_value(file2)
    if hash1 == hash2:
        print("Both Files are Unaltered")
        return
    return print("Modification Detected")

if __name__ == "__main__":
    file1 = input("Enter URL of First File : ")
    file2 = input("Enter URL of Second File : ")
    verifier(file1,file2)