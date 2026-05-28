"""
Encryption and Decryption Module
Implements Caesar Cipher and Vigenère Cipher for secure data encryption
"""

class CaesarCipher:
    """
    Caesar Cipher implementation for basic encryption/decryption.
    Shifts each character by a fixed number (shift key).
    
    Example:
        With shift=3: A->D, B->E, C->F, etc.
    """
    
    @staticmethod
    def encrypt(text, shift):
        """
        Encrypt text using Caesar Cipher
        
        Args:
            text (str): Plain text to encrypt
            shift (int): Number of positions to shift (1-25)
            
        Returns:
            str: Encrypted text (ciphertext)
        """
        if not isinstance(shift, int) or shift < 0 or shift > 25:
            raise ValueError("Shift must be an integer between 0 and 25")
        
        result = []
        
        for char in text:
            if char.isalpha():
                # Determine if uppercase or lowercase
                if char.isupper():
                    # Shift within uppercase letters (A-Z)
                    shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    # Shift within lowercase letters (a-z)
                    shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                result.append(shifted)
            else:
                # Keep non-alphabetic characters unchanged
                result.append(char)
        
        return ''.join(result)
    
    @staticmethod
    def decrypt(text, shift):
        """
        Decrypt text using Caesar Cipher
        Reverses the encryption by shifting backwards
        
        Args:
            text (str): Encrypted text (ciphertext)
            shift (int): Number of positions that were shifted (1-25)
            
        Returns:
            str: Decrypted text (plaintext)
        """
        # Decrypt by shifting in opposite direction
        return CaesarCipher.encrypt(text, -shift % 26)


class VigenereCipher:
    """
    Vigenère Cipher implementation - more complex encryption.
    Uses a keyword to create a repeating shift pattern.
    
    Example:
        Key: "SECRET"
        Each character in key determines shift for corresponding plaintext char
    """
    
    @staticmethod
    def _prepare_key(key):
        """
        Convert keyword to uppercase and validate
        
        Args:
            key (str): Encryption key/keyword
            
        Returns:
            str: Uppercase keyword containing only letters
        """
        if not key or not key.isalpha():
            raise ValueError("Key must contain only alphabetic characters")
        return key.upper()
    
    @staticmethod
    def _get_shift_value(char):
        """
        Convert character to shift value (A=0, B=1, ..., Z=25)
        
        Args:
            char (str): Single character from key
            
        Returns:
            int: Shift value (0-25)
        """
        return ord(char.upper()) - ord('A')
    
    @staticmethod
    def encrypt(text, key):
        """
        Encrypt text using Vigenère Cipher
        
        Args:
            text (str): Plain text to encrypt
            key (str): Encryption key (must contain only letters)
            
        Returns:
            str: Encrypted text (ciphertext)
        """
        key = VigenereCipher._prepare_key(key)
        result = []
        key_index = 0
        
        for char in text:
            if char.isalpha():
                # Get shift value from key
                shift = VigenereCipher._get_shift_value(key[key_index % len(key)])
                
                # Encrypt character using Caesar-like shift
                if char.isupper():
                    encrypted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    encrypted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                
                result.append(encrypted)
                key_index += 1
            else:
                # Keep non-alphabetic characters unchanged
                result.append(char)
        
        return ''.join(result)
    
    @staticmethod
    def decrypt(text, key):
        """
        Decrypt text using Vigenère Cipher
        Reverses encryption by using negative shift values
        
        Args:
            text (str): Encrypted text (ciphertext)
            key (str): Decryption key (same as encryption key)
            
        Returns:
            str: Decrypted text (plaintext)
        """
        key = VigenereCipher._prepare_key(key)
        result = []
        key_index = 0
        
        for char in text:
            if char.isalpha():
                # Get shift value from key
                shift = VigenereCipher._get_shift_value(key[key_index % len(key)])
                
                # Decrypt character by reversing the shift
                if char.isupper():
                    decrypted = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                else:
                    decrypted = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                
                result.append(decrypted)
                key_index += 1
            else:
                # Keep non-alphabetic characters unchanged
                result.append(char)
        
        return ''.join(result)
