/**
 * DecodeLabs Encryption & Decryption Library
 * JavaScript Implementation of Caesar and Vigenère Ciphers
 */

// ============================================
// CAESAR CIPHER
// ============================================

const CaesarCipher = {
    /**
     * Encrypt text using Caesar Cipher
     * @param {string} text - Plain text to encrypt
     * @param {number} shift - Shift value (0-25)
     * @returns {string} Encrypted text
     */
    encrypt: function(text, shift) {
        // Validate shift
        if (typeof shift !== 'number' || shift < 0 || shift > 25) {
            throw new Error('Shift must be a number between 0 and 25');
        }

        let result = [];
        
        for (let char of text) {
            if (/[a-zA-Z]/.test(char)) {
                // Determine if uppercase or lowercase
                const isUpper = /[A-Z]/.test(char);
                const base = isUpper ? 65 : 97; // ASCII values
                
                // Apply shift with wrapping
                const charCode = char.charCodeAt(0);
                const position = charCode - base;
                const shifted = (position + shift) % 26;
                
                result.push(String.fromCharCode(shifted + base));
            } else {
                // Keep non-alphabetic characters unchanged
                result.push(char);
            }
        }
        
        return result.join('');
    },

    /**
     * Decrypt text using Caesar Cipher
     * @param {string} text - Encrypted text to decrypt
     * @param {number} shift - Shift value (0-25)
     * @returns {string} Decrypted text
     */
    decrypt: function(text, shift) {
        // Decrypt by shifting in opposite direction
        // Use formula: ((-shift) % 26 + 26) % 26 to ensure positive result
        return this.encrypt(text, ((-shift) % 26 + 26) % 26);
    },

    /**
     * Try all possible Caesar shifts to decrypt
     * @param {string} text - Encrypted text
     * @returns {Array} Array of [shift, decrypted_text] pairs
     */
    bruteForce: function(text) {
        const results = [];
        for (let shift = 0; shift < 26; shift++) {
            results.push({
                shift: shift,
                text: this.decrypt(text, shift)
            });
        }
        return results;
    }
};

// ============================================
// VIGENÈRE CIPHER
// ============================================

const VigenereCipher = {
    /**
     * Prepare and validate key
     * @param {string} key - Encryption key
     * @returns {string} Uppercase key
     */
    prepareKey: function(key) {
        if (!key || !/^[a-zA-Z]+$/.test(key)) {
            throw new Error('Key must contain only alphabetic characters');
        }
        return key.toUpperCase();
    },

    /**
     * Get shift value from key character
     * @param {string} char - Single character from key
     * @returns {number} Shift value (0-25)
     */
    getShiftValue: function(char) {
        return char.toUpperCase().charCodeAt(0) - 65;
    },

    /**
     * Encrypt text using Vigenère Cipher
     * @param {string} text - Plain text to encrypt
     * @param {string} key - Encryption key (letters only)
     * @returns {string} Encrypted text
     */
    encrypt: function(text, key) {
        const preparedKey = this.prepareKey(key);
        let result = [];
        let keyIndex = 0;

        for (let char of text) {
            if (/[a-zA-Z]/.test(char)) {
                // Get shift value from key
                const shift = this.getShiftValue(preparedKey[keyIndex % preparedKey.length]);
                
                // Determine if uppercase or lowercase
                const isUpper = /[A-Z]/.test(char);
                const base = isUpper ? 65 : 97;
                
                // Apply shift
                const charCode = char.charCodeAt(0);
                const position = charCode - base;
                const shifted = (position + shift) % 26;
                
                result.push(String.fromCharCode(shifted + base));
                keyIndex++;
            } else {
                // Keep non-alphabetic characters unchanged
                result.push(char);
            }
        }

        return result.join('');
    },

    /**
     * Decrypt text using Vigenère Cipher
     * @param {string} text - Encrypted text to decrypt
     * @param {string} key - Decryption key (same as encryption)
     * @returns {string} Decrypted text
     */
    decrypt: function(text, key) {
        const preparedKey = this.prepareKey(key);
        let result = [];
        let keyIndex = 0;

        for (let char of text) {
            if (/[a-zA-Z]/.test(char)) {
                // Get shift value from key
                const shift = this.getShiftValue(preparedKey[keyIndex % preparedKey.length]);
                
                // Determine if uppercase or lowercase
                const isUpper = /[A-Z]/.test(char);
                const base = isUpper ? 65 : 97;
                
                // Apply reverse shift
                const charCode = char.charCodeAt(0);
                const position = charCode - base;
                const shifted = (position - shift + 26) % 26;
                
                result.push(String.fromCharCode(shifted + base));
                keyIndex++;
            } else {
                // Keep non-alphabetic characters unchanged
                result.push(char);
            }
        }

        return result.join('');
    }
};

// Export for use in HTML
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { CaesarCipher, VigenereCipher };
}
