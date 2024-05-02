// crypto.js

// Fungsi untuk mengenkripsi teks menggunakan metode Caesar Cipher
function encryptCaesar(text, shift) {
    return text.split('').map(char => {
        const code = char.charCodeAt(0);
        if (code >= 65 && code <= 90) {
            return String.fromCharCode(((code - 65 + shift) % 26) + 65);
        } else if (code >= 97 && code <= 122) {
            return String.fromCharCode(((code - 97 + shift) % 26) + 97);
        }
        return char;
    }).join('');
}

// Fungsi untuk mendekripsi teks yang dienkripsi menggunakan metode Caesar Cipher
function decryptCaesar(encryptedText, shift) {
    return encryptCaesar(encryptedText, (26 - shift) % 26);
}

module.exports = {
    encryptCaesar,
    decryptCaesar
};
