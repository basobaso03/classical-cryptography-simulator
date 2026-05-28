/**
 * DecodeLabs Encryption Tool - Application Logic
 * Handles UI interactions and cipher operations
 */

// ============================================
// CAESAR CIPHER FUNCTIONS
// ============================================

function updateShiftDisplay(value) {
    document.getElementById('shift-display').textContent = value;
}

function getCiphertextForAction(inputId, outputId) {
    const outputElement = document.getElementById(outputId);
    const outputText = outputElement ? outputElement.textContent.trim() : '';

    if (outputText) {
        return outputText;
    }

    return document.getElementById(inputId).value;
}

function caesarEncrypt() {
    try {
        const plaintext = document.getElementById('caesar-plaintext').value;
        const shift = parseInt(document.getElementById('caesar-shift').value);

        if (!plaintext.trim()) {
            alert('Please enter text to encrypt');
            return;
        }

        const ciphertext = CaesarCipher.encrypt(plaintext, shift);
        
        // Display result
        document.getElementById('caesar-encrypted-text').textContent = ciphertext;
        document.getElementById('caesar-encrypt-output').classList.add('visible');
        document.getElementById('caesar-decrypt-output').classList.remove('visible');
        document.getElementById('caesar-bruteforce-output').classList.remove('visible');

        // Log to console
        console.log(`Caesar Encrypt (shift=${shift}): "${plaintext}" → "${ciphertext}"`);
    } catch (error) {
        alert('Error: ' + error.message);
    }
}

function caesarDecrypt() {
    try {
        const ciphertext = getCiphertextForAction('caesar-plaintext', 'caesar-encrypted-text');
        const shift = parseInt(document.getElementById('caesar-shift').value);

        if (!ciphertext.trim()) {
            alert('Please enter text to decrypt');
            return;
        }

        const plaintext = CaesarCipher.decrypt(ciphertext, shift);
        
        // Display result
        document.getElementById('caesar-decrypted-text').textContent = plaintext;
        document.getElementById('caesar-decrypt-output').classList.add('visible');
        document.getElementById('caesar-encrypt-output').classList.remove('visible');
        document.getElementById('caesar-bruteforce-output').classList.remove('visible');

        // Verify if decryption was successful
        const reencrypted = CaesarCipher.encrypt(plaintext, shift);
        const verifyElement = document.getElementById('caesar-verify');
        
        if (reencrypted === ciphertext) {
            verifyElement.innerHTML = '<div class="verification success">✓ Verification Passed - Decryption correct!</div>';
        } else {
            verifyElement.innerHTML = '<div class="verification failed">✗ Verification Failed</div>';
        }

        // Log to console
        console.log(`Caesar Decrypt (shift=${shift}): "${ciphertext}" → "${plaintext}"`);
    } catch (error) {
        alert('Error: ' + error.message);
    }
}

function caesarBruteforce() {
    try {
        const ciphertext = getCiphertextForAction('caesar-plaintext', 'caesar-encrypted-text');

        if (!ciphertext.trim()) {
            alert('Please enter text to brute force');
            return;
        }

        const results = CaesarCipher.bruteForce(ciphertext);
        
        // Display results
        let html = '';
        results.forEach(result => {
            html += `
                <div class="bruteforce-item">
                    <div class="bruteforce-shift">Shift ${result.shift}</div>
                    <div class="bruteforce-text">${result.text}</div>
                </div>
            `;
        });

        document.getElementById('caesar-bruteforce-results').innerHTML = html;
        document.getElementById('caesar-bruteforce-output').classList.add('visible');
        document.getElementById('caesar-encrypt-output').classList.remove('visible');
        document.getElementById('caesar-decrypt-output').classList.remove('visible');

        console.log('Caesar Brute Force: All 26 shifts calculated');
    } catch (error) {
        alert('Error: ' + error.message);
    }
}

// ============================================
// VIGENÈRE CIPHER FUNCTIONS
// ============================================

function vigenereEncrypt() {
    try {
        const plaintext = document.getElementById('vigenere-plaintext').value;
        const key = document.getElementById('vigenere-key').value;

        if (!plaintext.trim()) {
            alert('Please enter text to encrypt');
            return;
        }

        if (!key.trim()) {
            alert('Please enter a key');
            return;
        }

        const ciphertext = VigenereCipher.encrypt(plaintext, key);
        
        // Display result
        document.getElementById('vigenere-encrypted-text').textContent = ciphertext;
        document.getElementById('vigenere-encrypt-output').classList.add('visible');
        document.getElementById('vigenere-decrypt-output').classList.remove('visible');

        // Log to console
        console.log(`Vigenère Encrypt (key="${key}"): "${plaintext}" → "${ciphertext}"`);
    } catch (error) {
        alert('Error: ' + error.message);
    }
}

function vigenereDecrypt() {
    try {
        const ciphertext = getCiphertextForAction('vigenere-plaintext', 'vigenere-encrypted-text');
        const key = document.getElementById('vigenere-key').value;

        if (!ciphertext.trim()) {
            alert('Please enter text to decrypt');
            return;
        }

        if (!key.trim()) {
            alert('Please enter a key');
            return;
        }

        const plaintext = VigenereCipher.decrypt(ciphertext, key);
        
        // Display result
        document.getElementById('vigenere-decrypted-text').textContent = plaintext;
        document.getElementById('vigenere-decrypt-output').classList.add('visible');
        document.getElementById('vigenere-encrypt-output').classList.remove('visible');

        // Verify if decryption was successful
        const reencrypted = VigenereCipher.encrypt(plaintext, key);
        const verifyElement = document.getElementById('vigenere-verify');
        
        if (reencrypted === ciphertext) {
            verifyElement.innerHTML = '<div class="verification success">✓ Verification Passed - Decryption correct!</div>';
        } else {
            verifyElement.innerHTML = '<div class="verification failed">✗ Verification Failed</div>';
        }

        // Log to console
        console.log(`Vigenère Decrypt (key="${key}"): "${ciphertext}" → "${plaintext}"`);
    } catch (error) {
        alert('Error: ' + error.message);
    }
}

// ============================================
// UTILITY FUNCTIONS
// ============================================

function copyToClipboard(elementId, button) {
    const element = document.getElementById(elementId);
    const text = element.textContent;
    
    navigator.clipboard.writeText(text).then(() => {
        // Show feedback
        const originalText = button.textContent;
        button.textContent = '✓ Copied!';
        button.style.background = 'var(--success-color)';
        
        setTimeout(() => {
            button.textContent = originalText;
            button.style.background = '';
        }, 2000);
    }).catch(err => {
        alert('Failed to copy: ' + err);
    });
}

// ============================================
// INITIALIZATION
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    console.log('🛡️ DecodeLabs Encryption Tool Loaded');
    console.log('Available functions: CaesarCipher, VigenereCipher');

    // Initialize with sample data
    console.log('\n📝 Sample Data Loaded:');
    console.log('Caesar: "Hello World" with shift=3');
    console.log('Vigenère: "Cyber Security" with key="DECODELABS"');
});
