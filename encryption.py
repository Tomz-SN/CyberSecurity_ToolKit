import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def sym_etn_dtn(text):
    key = secrets.token_bytes(32)
    nonce = secrets.token_bytes(12)
    sym_gcm = AESGCM(key)

    cipher_text = nonce + sym_gcm.encrypt(nonce,text.encode(), None)
    plain_text = sym_gcm.decrypt(cipher_text[:12], cipher_text[12:], None)

    return key.hex(), cipher_text.hex(), plain_text.decode()

if __name__ == "__main__":
    text = input("Enter you Message : ")
    print(sym_etn_dtn(text))