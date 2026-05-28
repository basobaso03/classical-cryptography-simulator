"""
Unit Tests for Encryption/Decryption Ciphers
Tests both Caesar and Vigenère cipher implementations
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ciphers import CaesarCipher, VigenereCipher


def test_caesar_basic():
    """Test basic Caesar cipher encryption/decryption"""
    plaintext = "Hello World"
    shift = 3
    
    # Encrypt
    ciphertext = CaesarCipher.encrypt(plaintext, shift)
    print(f"✓ Caesar Cipher (shift={shift})")
    print(f"  Plain:  {plaintext}")
    print(f"  Cipher: {ciphertext}")
    
    # Decrypt
    decrypted = CaesarCipher.decrypt(ciphertext, shift)
    assert decrypted == plaintext, "Decryption failed!"
    print(f"  Decrypted: {decrypted} ✔")
    return True


def test_caesar_uppercase():
    """Test Caesar cipher with uppercase text"""
    plaintext = "ABCXYZ"
    shift = 1
    
    ciphertext = CaesarCipher.encrypt(plaintext, shift)
    expected = "BCDYZA"
    
    print(f"\n✓ Caesar Cipher - Uppercase (shift={shift})")
    print(f"  Plain:  {plaintext}")
    print(f"  Cipher: {ciphertext}")
    print(f"  Expected: {expected}")
    
    assert ciphertext == expected, f"Expected {expected}, got {ciphertext}"
    decrypted = CaesarCipher.decrypt(ciphertext, shift)
    assert decrypted == plaintext
    print(f"  Decrypted: {decrypted} ✔")
    return True


def test_caesar_with_numbers():
    """Test Caesar cipher with numbers and special characters"""
    plaintext = "Test123!@#"
    shift = 5
    
    ciphertext = CaesarCipher.encrypt(plaintext, shift)
    decrypted = CaesarCipher.decrypt(ciphertext, shift)
    
    print(f"\n✓ Caesar Cipher - Numbers & Symbols (shift={shift})")
    print(f"  Plain:  {plaintext}")
    print(f"  Cipher: {ciphertext}")
    print(f"  Decrypted: {decrypted}")
    
    assert decrypted == plaintext, "Numbers/symbols not preserved!"
    print(f"  ✔ Special characters preserved")
    return True


def test_caesar_zero_shift():
    """Test Caesar cipher with zero shift (no change)"""
    plaintext = "NoChange"
    shift = 0
    
    ciphertext = CaesarCipher.encrypt(plaintext, shift)
    
    print(f"\n✓ Caesar Cipher - Zero Shift")
    print(f"  Plain:  {plaintext}")
    print(f"  Cipher: {ciphertext}")
    
    assert ciphertext == plaintext, "Zero shift should not change text!"
    print(f"  ✔ No change with zero shift")
    return True


def test_vigenere_basic():
    """Test basic Vigenère cipher encryption/decryption"""
    plaintext = "Hello World"
    key = "SECRET"
    
    ciphertext = VigenereCipher.encrypt(plaintext, key)
    print(f"\n✓ Vigenère Cipher (key={key})")
    print(f"  Plain:  {plaintext}")
    print(f"  Cipher: {ciphertext}")
    
    decrypted = VigenereCipher.decrypt(ciphertext, key)
    assert decrypted == plaintext, "Vigenère decryption failed!"
    print(f"  Decrypted: {decrypted} ✔")
    return True


def test_vigenere_single_char_key():
    """Test Vigenère cipher with single character key (equivalent to Caesar)"""
    plaintext = "ABCXYZ"
    key = "B"  # Shift by 1
    
    ciphertext = VigenereCipher.encrypt(plaintext, key)
    expected = "BCDYZA"
    
    print(f"\n✓ Vigenère Cipher - Single Char Key (key={key})")
    print(f"  Plain:  {plaintext}")
    print(f"  Cipher: {ciphertext}")
    
    assert ciphertext == expected, f"Expected {expected}, got {ciphertext}"
    decrypted = VigenereCipher.decrypt(ciphertext, key)
    assert decrypted == plaintext
    print(f"  Decrypted: {decrypted} ✔")
    return True


def test_vigenere_case_insensitive():
    """Test Vigenère cipher case handling"""
    plaintext = "Hello"
    key = "secret"  # lowercase key
    
    ciphertext = VigenereCipher.encrypt(plaintext, key)
    decrypted = VigenereCipher.decrypt(ciphertext, key)
    
    print(f"\n✓ Vigenère Cipher - Case Insensitive Key")
    print(f"  Plain:  {plaintext}")
    print(f"  Key:    {key} (lowercase)")
    print(f"  Cipher: {ciphertext}")
    print(f"  Decrypted: {decrypted}")
    
    assert decrypted == plaintext
    print(f"  ✔ Case insensitive key handling works")
    return True


def test_vigenere_mixed_content():
    """Test Vigenère cipher with mixed content"""
    plaintext = "Test123!@#"
    key = "CRYPTO"
    
    ciphertext = VigenereCipher.encrypt(plaintext, key)
    decrypted = VigenereCipher.decrypt(ciphertext, key)
    
    print(f"\n✓ Vigenère Cipher - Mixed Content (key={key})")
    print(f"  Plain:  {plaintext}")
    print(f"  Cipher: {ciphertext}")
    print(f"  Decrypted: {decrypted}")
    
    assert decrypted == plaintext
    print(f"  ✔ Numbers/symbols handled correctly")
    return True


def test_error_handling():
    """Test error handling"""
    print(f"\n✓ Error Handling Tests")
    
    # Invalid shift
    try:
        CaesarCipher.encrypt("Hello", 26)
        print("  ✗ Should have raised error for shift > 25")
        return False
    except ValueError:
        print("  ✔ Rejects invalid shift values")
    
    # Invalid Vigenère key
    try:
        VigenereCipher.encrypt("Hello", "123")
        print("  ✗ Should have raised error for non-alphabetic key")
        return False
    except ValueError:
        print("  ✔ Rejects non-alphabetic keys")
    
    return True


def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("🧪 Running Cipher Tests")
    print("=" * 60)
    
    tests = [
        test_caesar_basic,
        test_caesar_uppercase,
        test_caesar_with_numbers,
        test_caesar_zero_shift,
        test_vigenere_basic,
        test_vigenere_single_char_key,
        test_vigenere_case_insensitive,
        test_vigenere_mixed_content,
        test_error_handling,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"  ✗ Test failed with error: {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"📊 Test Results: {passed} passed, {failed} failed")
    print("=" * 60 + "\n")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
