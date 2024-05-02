// index.js

const { encryptCaesar, decryptCaesar } = require('./crypto');

// Contoh penggunaan fungsi enkripsi dan dekripsi dengan Caesar Cipher
const plaintext = 'Hello, World!';
const shift = 3;
const encryptedText = encryptCaesar(plaintext, shift);
const decryptedText = decryptCaesar(encryptedText, shift);

console.log('Plaintext:', plaintext);
console.log('Encrypted Text:', encryptedText);
console.log('Decrypted Text:', decryptedText);
