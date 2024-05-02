# main.py

from crypto import encrypt_caesar, decrypt_caesar

# Contoh penggunaan fungsi enkripsi dan dekripsi dengan Caesar Cipher
plaintext = 'Hello, World!'
shift = 3
encrypted_text = encrypt_caesar(plaintext, shift)
decrypted_text = decrypt_caesar(encrypted_text, shift)

print('Plaintext:', plaintext)
print('Encrypted Text:', encrypted_text)
print('Decrypted Text:', decrypted_text)
