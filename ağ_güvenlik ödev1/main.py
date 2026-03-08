import aes
import caesar

print("1 - AES Şifreleme")
print("2 - Caesar Şifreleme")

secim = input("Seçim yap: ")

text = input("Metni gir: ")

if secim == "1":

    encrypted = aes.encrypt(text)
    print("Şifreli:", encrypted)

    decrypted = aes.decrypt(encrypted)
    print("Çözülmüş:", decrypted)

elif secim == "2":

    shift = int(input("Kaydırma sayısı: "))

    encrypted = caesar.encrypt(text, shift)
    print("Şifreli:", encrypted)

    decrypted = caesar.decrypt(encrypted, shift)
    print("Çözülmüş:", decrypted)

else:
    print("Geçersiz seçim")
    