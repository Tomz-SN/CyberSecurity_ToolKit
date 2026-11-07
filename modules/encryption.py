import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

def sym_etn_dtn(text):
    key = secrets.token_bytes(32)
    nonce = secrets.token_bytes(12)
    sym_gcm = AESGCM(key)

    cipher_text = nonce + sym_gcm.encrypt(nonce,text.encode(), None)
    plain_text = sym_gcm.decrypt(cipher_text[:12], cipher_text[12:], None)

    return key.hex(), cipher_text.hex(), plain_text.decode()

def asym_etn_dtn(text):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    cipher_text = public_key.encrypt(
        text.encode(),
        padding.OAEP(
            mgf = padding.MGF1(algorithm=hashes.SHA256()),
            algorithm = hashes.SHA256(),
            label=None
        )
    )
    plain_text = private_key.decrypt(
        cipher_text,
                padding.OAEP(
                    mgf = padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm = hashes.SHA256(),
                    label=None
                )
    )
    return cipher_text.hex(), plain_text.decode()

if __name__ == "__main__":
    text = input("Enter you Message : ")
    print(sym_etn_dtn(text))
    print("---------------------------------------")
    print(asym_etn_dtn(text))