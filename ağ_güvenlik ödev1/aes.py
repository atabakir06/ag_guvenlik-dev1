from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

key = get_random_bytes(16)


def encrypt(text):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(text.encode())

    encrypted = base64.b64encode(cipher.nonce + tag + ciphertext)
    return encrypted.decode()


def decrypt(enc_text):
    data = base64.b64decode(enc_text)

    nonce = data[:16]
    tag = data[16:32]
    ciphertext = data[32:]

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted = cipher.decrypt_and_verify(ciphertext, tag)

    return decrypted.decode()


# Kullanıcıdan veri alma
text = input("Şifrelenecek metni gir: ")

encrypted_text = encrypt(text)
print("Şifreli metin:", encrypted_text)

decrypted_text = decrypt(encrypted_text)
print("Çözülmüş metin:", decrypted_text)
