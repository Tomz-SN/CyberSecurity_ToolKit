import secrets

def encryption(message):
    message = message.encode()
    key = secrets.token_bytes(len(message))
    encrypted_text = bytes(i ^ j for i,j in zip(message,key))

    with open("keys.txt", "w") as file:
        file.write(key.hex())
    return encrypted_text
