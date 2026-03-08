def encrypt(text, shift):
    result = ""

    for c in text:
        if c.isalpha():
            result += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += c

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


msg = input("Metin gir: ")
shift = 3

enc = encrypt(msg.upper(), shift)
print("Şifreli:", enc)

dec = decrypt(enc, shift)
print("Çözülmüş:", dec)
