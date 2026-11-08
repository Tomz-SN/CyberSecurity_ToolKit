import secrets

def encryption(message):
    message = message.encode()
    key = secrets.token_bytes(len(message))