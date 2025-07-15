# Caesar Cipher Educational Tool

A Python-based Caesar cipher encryption/decryption tool with Streamlit interface designed for cybersecurity education.

## Features

- **Caesar Cipher Implementation**: Complete encryption and decryption functionality
- **Interactive Web Interface**: User-friendly Streamlit-based GUI
- **Real-time Processing**: Live preview of encryption as you type
- **Educational Content**: Built-in information about Caesar cipher and its security implications
- **Customizable Shift Values**: Support for shift values from 1-25
- **Text Analysis**: Character count and composition analysis
- **Brute Force Demonstration**: Shows all possible decryptions to illustrate cipher weakness
- **Case Preservation**: Maintains uppercase and lowercase formatting
- **Non-alphabetic Character Handling**: Preserves spaces, numbers, and punctuation

## Installation

1. Ensure you have Python 3.7+ installed
2. Install required dependencies:
   ```bash
   pip install streamlit
   ```

## Usage

1. Run the application:
   ```bash
   streamlit run app.py --server.port 5000
   ```

2. Open your web browser and navigate to `http://localhost:5000`

3. **To Encrypt Text:**
   - Enter your plaintext in the input area
   - Select your desired shift value (1-25)
   - Click the ’ Encrypt" button
   - Copy the encrypted result

4. **To Decrypt Text:**
   - Enter your encrypted text in the input area
   - Set the shift value to the same value used for encryption
   - Click the “ Decrypt" button
   - View the decrypted plaintext

## Educational Features

### Live Demonstration
- Real-time encryption preview as you type
- Interactive shift value adjustment
- Immediate feedback on text transformations

### Security Analysis
- **Brute Force Analysis**: Demonstrates all 25 possible decryptions
- **Character Mapping**: Shows how individual characters are transformed
- **Vulnerability Explanation**: Clear explanation of why Caesar cipher is insecure

### Text Analysis
- Character count statistics
- Alphabetic vs non-alphabetic character breakdown
- Transformation details for educational purposes

## Security Education

This tool is designed specifically for educational purposes to teach:

1. **Basic Cryptography Concepts**:
   - Substitution ciphers
   - Shift-based encryption
   - Key space limitations

2. **Security Vulnerabilities**:
   - Brute force attacks
   - Small key space (only 25 possible keys)
   - Frequency analysis susceptibility

3. **Modern Cryptography Awareness**:
   - Why historical ciphers are inadequate today
   - Introduction to modern encryption standards
   - Importance of using established cryptographic libraries

## Technical Implementation

### Core Algorithm
```python
def caesar_cipher(text, shift, decrypt=False):
    """Caesar cipher implementation with support for encryption/decryption"""
    # Implementation handles:
    # - Case preservation
    # - Non-alphabetic character preservation
    # - Wrap-around for alphabet boundaries
