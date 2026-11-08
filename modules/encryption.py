import secrets

def encryption(message):
    message = message.encode()
    key = secrets.token_bytes(len(message))
    encrypted_text = bytes(i ^ j for i,j in zip(message,key))

    with open("keys.txt", "w") as file:
        file.write(key.hex())
    return encrypted_text.hex()

def decryption(key,encrypted_text):
    key = bytes.fromhex(key)
    encrypted_text = bytes.fromhex(encrypted_text)
    message = bytes(x ^ y for x,y in zip(key,encrypted_text))
    return message.decode() 
