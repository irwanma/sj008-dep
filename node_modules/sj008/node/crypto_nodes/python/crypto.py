# crypto.py

# Fungsi untuk mengenkripsi teks menggunakan metode Caesar Cipher
def encrypt_caesar(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - 97 + shift_amount) % 26 + 97)
            else:
                encrypted_text += chr((ord(char) - 65 + shift_amount) % 26 + 65)
        else:
            encrypted_text += char
    return encrypted_text

# Fungsi untuk mendekripsi teks yang dienkripsi menggunakan metode Caesar Cipher
def decrypt_caesar(encrypted_text, shift):
    return encrypt_caesar(encrypted_text, -shift)
