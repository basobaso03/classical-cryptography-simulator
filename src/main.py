"""
DecodeLabs Cyber Security - Project 2
Basic Encryption & Decryption Application
Author: Cyber Security Analyst (Intern)
Version: 1.0

This application demonstrates fundamental encryption and decryption concepts
using both Caesar and Vigenère ciphers.
"""

from ciphers import CaesarCipher, VigenereCipher


def display_banner():
    """Display welcome banner"""
    print("\n" + "=" * 60)
    print("🛡️  DecodeLabs Cyber Security - Project 2")
    print("   Basic Encryption & Decryption")
    print("=" * 60 + "\n")


def display_menu():
    """Display main menu options"""
    print("\n📋 Select Encryption Method:")
    print("1. Caesar Cipher (Basic - Fixed Shift)")
    print("2. Vigenère Cipher (Advanced - Keyword-based)")
    print("0. Exit")
    print("-" * 60)


def get_valid_shift():
    """
    Get and validate shift value from user
    
    Returns:
        int: Valid shift value (0-25)
    """
    while True:
        try:
            shift = int(input("\n🔑 Enter shift value (0-25): "))
            if 0 <= shift <= 25:
                return shift
            else:
                print("❌ Error: Shift must be between 0 and 25")
        except ValueError:
            print("❌ Error: Please enter a valid number")


def get_valid_key():
    """
    Get and validate key from user for Vigenère cipher
    
    Returns:
        str: Valid alphabetic key
    """
    while True:
        key = input("\n🔑 Enter encryption key (letters only): ").strip()
        if key and key.isalpha():
            return key
        else:
            print("❌ Error: Key must contain only alphabetic characters")


def caesar_cipher_mode():
    """Handle Caesar Cipher encryption/decryption"""
    print("\n" + "-" * 60)
    print("🔐 CAESAR CIPHER MODE")
    print("-" * 60)
    
    # Get user input
    plaintext = input("\n📝 Enter text to encrypt: ").strip()
    if not plaintext:
        print("❌ Error: Text cannot be empty")
        return
    
    shift = get_valid_shift()
    
    # Encrypt
    ciphertext = CaesarCipher.encrypt(plaintext, shift)
    print(f"\n✅ Encryption successful!")
    print(f"   Original Text:   {plaintext}")
    print(f"   Shift Value:     {shift}")
    print(f"   Encrypted Text:  {ciphertext}")
    
    # Decrypt
    decrypted = CaesarCipher.decrypt(ciphertext, shift)
    print(f"\n✅ Decryption successful!")
    print(f"   Encrypted Text:  {ciphertext}")
    print(f"   Decrypted Text:  {decrypted}")
    
    # Verification
    if decrypted == plaintext:
        print("\n✔️  Verification: PASSED - Text matches original!")
    else:
        print("\n✖️  Verification: FAILED - Text does not match!")


def vigenere_cipher_mode():
    """Handle Vigenère Cipher encryption/decryption"""
    print("\n" + "-" * 60)
    print("🔐 VIGENÈRE CIPHER MODE")
    print("-" * 60)
    
    # Get user input
    plaintext = input("\n📝 Enter text to encrypt: ").strip()
    if not plaintext:
        print("❌ Error: Text cannot be empty")
        return
    
    key = get_valid_key()
    
    # Encrypt
    ciphertext = VigenereCipher.encrypt(plaintext, key)
    print(f"\n✅ Encryption successful!")
    print(f"   Original Text:   {plaintext}")
    print(f"   Encryption Key:  {key}")
    print(f"   Encrypted Text:  {ciphertext}")
    
    # Decrypt
    decrypted = VigenereCipher.decrypt(ciphertext, key)
    print(f"\n✅ Decryption successful!")
    print(f"   Encrypted Text:  {ciphertext}")
    print(f"   Decrypted Text:  {decrypted}")
    
    # Verification
    if decrypted == plaintext:
        print("\n✔️  Verification: PASSED - Text matches original!")
    else:
        print("\n✖️  Verification: FAILED - Text does not match!")


def main():
    """Main application loop"""
    display_banner()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            caesar_cipher_mode()
        elif choice == "2":
            vigenere_cipher_mode()
        elif choice == "0":
            print("\n👋 Thank you for using DecodeLabs Encryption Tool!")
            print("   Secure data protection starts with strong fundamentals.")
            print("=" * 60 + "\n")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, or 0")


if __name__ == "__main__":
    main()
