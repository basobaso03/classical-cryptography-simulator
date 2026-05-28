# 🌐 Web Interface - DecodeLabs Encryption Tool

## Overview

A beautiful, interactive web-based interface for the Caesar and Vigenère cipher encryption/decryption tools. Built with vanilla HTML, CSS, and JavaScript - no external dependencies required!

## 🎯 Features

### ✅ Interactive Encryption/Decryption
- **Caesar Cipher**: Encrypt and decrypt with adjustable shift value (0-25)
- **Vigenère Cipher**: Encrypt and decrypt with keyword-based encryption
- **Real-time results**: Instant feedback on encryption/decryption operations
- **Verification badges**: Automatic verification that decryption matches original

### ✅ Advanced Tools
- **Brute Force Attack**: Try all 26 possible Caesar cipher shifts to find the answer
- **Copy to Clipboard**: Easily copy encrypted/decrypted text
- **Beautiful UI**: Modern dark theme with gradient effects and smooth animations

## 📁 File Structure

```
web/
├── index.html           # Main HTML interface
├── css/
│   └── style.css        # Professional styling with dark theme
├── js/
│   ├── ciphers.js       # JavaScript cipher implementations
│   └── app.js           # UI logic and event handlers
└── assets/              # For future assets (images, etc.)
```

## 🚀 How to Use

### Opening the Website

1. **Simple Method**: Double-click `index.html` to open in your default browser.
2. **Command Line**: `start index.html` (Windows) or `open index.html` (Mac).
3. **Web Server**: Serve with Python or Node.js for a better experience:
   ```bash
   # Python 3
   python -m http.server 8000
   
   # Then visit: http://localhost:8000/web/
   ```

### Using the Interface

#### Caesar Cipher Tab
1. Enter text to encrypt in the plaintext field.
2. Adjust the shift slider (0-25).
3. Click **Encrypt** to see the encrypted result.
4. To decrypt: enter encrypted text, adjust shift, click **Decrypt**.
5. Try **Brute Force** to see all 26 possible decryptions.

#### Vigenère Cipher Tab
1. Enter text to encrypt in the plaintext field.
2. Enter an encryption key (letters only).
3. Click **Encrypt** to see the encrypted result.
4. To decrypt: enter encrypted text, use same key, click **Decrypt**.

## 🎨 UI Components

### Design Features
- **Dark theme**: Easy on the eyes, professional appearance.
- **Responsive design**: Works on desktop, tablet, and mobile.
- **Color scheme**:
  - Primary: Dark blue (#1a1a2e)
  - Accent: Coral/Red (#e94560)
  - Success: Green (#2ecc71)
  - Text: Light gray (#ecf0f1)

### Navigation
- Header with logo and navigation tabs.
- Tab switching without page reload.
- Smooth animations and transitions.
- Footer with project information and contact details.

### Output Display
- Highlighted output sections.
- Copy-to-clipboard functionality.
- Success/failed verification badges.
- Scrollable brute force results.

## 🔧 Technical Details

### JavaScript Cipher Implementation

**CaesarCipher Object**
- `encrypt(text, shift)` - Encrypts plaintext.
- `decrypt(text, shift)` - Decrypts ciphertext.
- `bruteForce(text)` - Returns all 26 possible decryptions.

**VigenereCipher Object**
- `encrypt(text, key)` - Encrypts with keyword.
- `decrypt(text, key)` - Decrypts with keyword.
- `prepareKey(key)` - Validates and formats key.
- `getShiftValue(char)` - Converts character to shift value.

### Browser Compatibility
- Modern browsers (Chrome, Firefox, Safari, Edge).
- No external dependencies.
- Pure vanilla JavaScript.
- CSS Grid and Flexbox for layout.

## 📱 Responsive Features

- **Desktop**: Full two-column layout for Caesar and Vigenère side-by-side.
- **Tablet**: Stacked columns with readable text.
- **Mobile**: Single column, optimized touch targets.
- **Scrollable**: Content sections scroll independently.

## 🔐 Security Features

- Client-side only: No data sent to servers.
- No cookies or tracking.
- Text encryption happens in your browser.
- Can be used offline after initial load.

## 🎓 Educational Value

This web interface teaches:
- How substitution ciphers work.
- Caesar cipher mechanics.
- Polyalphabetic encryption (Vigenère).
- Brute force attack concepts.
- Character encoding and modulo arithmetic.
- Interactive learning through experimentation.

## 💡 Tips for Users

1. **Copy Encrypted Text**: Use the Copy button to quickly copy results.
2. **Try Brute Force**: Use Caesar brute force to understand attack vectors.
3. **Experiment with Keys**: Try different key lengths in Vigenère.

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Page doesn't load | Ensure `index.html` is in the correct path |
| Buttons not responding | Check browser console for errors (F12) |
| Styles look wrong | Refresh page (Ctrl+F5) to clear cache |
| Copy button not working | Check browser permissions for clipboard |

## 📞 Support

For issues or suggestions:
- 📧 Email: decodelabs.tech@gmail.com
- 🌎 Website: www.decodelabs.tech
- 📱 Phone: +91 89330 06408

## 📄 License

Part of DecodeLabs Cyber Security Project 2 - Educational purposes only.

---

**Happy Learning!** 🎓

Open `index.html` in your browser to start encrypting and decrypting with the DecodeLabs Encryption Tool!
