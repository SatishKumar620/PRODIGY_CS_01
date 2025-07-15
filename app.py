import streamlit as st
import re
import string

def caesar_cipher(text, shift, decrypt=False):
    """
    Perform Caesar cipher encryption or decryption on the given text.
    
    Args:
        text (str): The input text to encrypt/decrypt
        shift (int): The shift value (1-25)
        decrypt (bool): If True, decrypt the text; if False, encrypt
    
    Returns:
        str: The encrypted/decrypted text
    """
    if decrypt:
        shift = -shift
    
    result = ""
    
    for char in text:
        if char.isalpha():
            # Determine if character is uppercase or lowercase
            is_upper = char.isupper()
            char = char.lower()
            
            # Shift the character
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            
            # Restore original case
            if is_upper:
                shifted_char = shifted_char.upper()
            
            result += shifted_char
        else:
            # Preserve non-alphabetic characters
            result += char
    
    return result

def validate_shift(shift):
    """Validate that the shift value is within acceptable range."""
    return 1 <= shift <= 25

def get_cipher_info():
    """Return educational information about Caesar cipher."""
    return """
    ## About Caesar Cipher
    
    The Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
    
    **How it works:**
    - Each letter is shifted by a fixed number of positions in the alphabet
    - For example, with a shift of 3: A→D, B→E, C→F, etc.
    - The cipher wraps around, so with shift 3: X→A, Y→B, Z→C
    
    **Security Note:**
    The Caesar cipher is easily broken and should never be used for real security purposes. It's an excellent educational tool for understanding basic cryptographic concepts.
    """

def main():
    st.set_page_config(
        page_title="Caesar Cipher Tool",
        page_icon="🔐",
        layout="wide"
    )
    
    st.title("🔐 Caesar Cipher Encryption/Decryption Tool")
    st.subheader("Educational Cybersecurity Tool")
    
    # Create two columns for layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Input section
        st.markdown("### Input Text")
        input_text = st.text_area(
            "Enter your text here:",
            height=150,
            placeholder="Type your message here...",
            help="Enter the text you want to encrypt or decrypt"
        )
        
        # Shift value selection
        st.markdown("### Cipher Settings")
        shift_value = st.slider(
            "Shift Value:",
            min_value=1,
            max_value=25,
            value=3,
            help="Choose how many positions to shift each letter (1-25)"
        )
        
        # Operation buttons
        col_encrypt, col_decrypt = st.columns(2)
        
        with col_encrypt:
            encrypt_btn = st.button("🔒 Encrypt", type="primary", use_container_width=True)
        
        with col_decrypt:
            decrypt_btn = st.button("🔓 Decrypt", type="secondary", use_container_width=True)
        
        # Options
        st.markdown("### Options")
        preserve_case = st.checkbox("Preserve original case", value=True, help="Keep uppercase and lowercase letters as they are")
        preserve_nonalpha = st.checkbox("Preserve non-alphabetic characters", value=True, help="Keep numbers, spaces, and punctuation unchanged")
        
    with col2:
        # Educational information
        st.markdown(get_cipher_info())
    
    # Results section
    if input_text:
        st.markdown("---")
        st.markdown("### Results")
        
        # Validate shift value
        if not validate_shift(shift_value):
            st.error("❌ Invalid shift value! Please use a value between 1 and 25.")
            return
        
        # Real-time encryption display
        if input_text and not encrypt_btn and not decrypt_btn:
            st.info("💡 Click 'Encrypt' or 'Decrypt' to see the result, or type to see live preview below:")
            
            # Live preview of encryption
            encrypted_preview = caesar_cipher(input_text, shift_value, decrypt=False)
            st.text_area("Live Encryption Preview:", value=encrypted_preview, height=100, disabled=True)
        
        # Handle button clicks
        if encrypt_btn:
            if not input_text.strip():
                st.warning("⚠️ Please enter some text to encrypt.")
            else:
                encrypted_text = caesar_cipher(input_text, shift_value, decrypt=False)
                
                st.success("✅ Text encrypted successfully!")
                st.text_area("Encrypted Text:", value=encrypted_text, height=100)
                
                # Copy to clipboard button
                st.code(encrypted_text, language=None)
                
                # Show transformation details
                with st.expander("🔍 View Transformation Details"):
                    st.write(f"**Original Text:** {input_text}")
                    st.write(f"**Shift Value:** {shift_value}")
                    st.write(f"**Encrypted Text:** {encrypted_text}")
                    
                    # Show character mapping for first few characters
                    if len(input_text) > 0:
                        st.write("**Character Mapping (first 10 characters):**")
                        for i, char in enumerate(input_text[:10]):
                            if char.isalpha():
                                encrypted_char = caesar_cipher(char, shift_value, decrypt=False)
                                st.write(f"'{char}' → '{encrypted_char}'")
        
        if decrypt_btn:
            if not input_text.strip():
                st.warning("⚠️ Please enter some text to decrypt.")
            else:
                decrypted_text = caesar_cipher(input_text, shift_value, decrypt=True)
                
                st.success("✅ Text decrypted successfully!")
                st.text_area("Decrypted Text:", value=decrypted_text, height=100)
                
                # Copy to clipboard button
                st.code(decrypted_text, language=None)
                
                # Show transformation details
                with st.expander("🔍 View Transformation Details"):
                    st.write(f"**Encrypted Text:** {input_text}")
                    st.write(f"**Shift Value:** {shift_value}")
                    st.write(f"**Decrypted Text:** {decrypted_text}")
    
    # Footer with additional information
    st.markdown("---")
    
    # Analysis section
    if input_text:
        st.markdown("### Text Analysis")
        analysis_col1, analysis_col2, analysis_col3 = st.columns(3)
        
        with analysis_col1:
            st.metric("Total Characters", len(input_text))
        
        with analysis_col2:
            alpha_count = sum(1 for c in input_text if c.isalpha())
            st.metric("Alphabetic Characters", alpha_count)
        
        with analysis_col3:
            nonalpha_count = len(input_text) - alpha_count
            st.metric("Non-alphabetic Characters", nonalpha_count)
    
    # Brute force analysis section
    if input_text and len(input_text.strip()) > 0:
        with st.expander("🔬 Brute Force Analysis (Educational)"):
            st.write("This shows all possible decryptions with different shift values:")
            st.warning("⚠️ This demonstrates why Caesar cipher is not secure - all possibilities can be easily checked!")
            
            for shift in range(1, 26):
                decrypted = caesar_cipher(input_text, shift, decrypt=True)
                st.write(f"**Shift {shift:2d}:** {decrypted}")
    
    # Educational notes
    st.markdown("---")
    st.markdown("### 📚 Educational Notes")
    
    col_note1, col_note2 = st.columns(2)
    
    with col_note1:
        st.info("""
        **Why Caesar Cipher is Insecure:**
        - Only 25 possible keys
        - Can be broken by brute force in seconds
        - Vulnerable to frequency analysis
        - No protection against known-plaintext attacks
        """)
    
    with col_note2:
        st.info("""
        **Modern Alternatives:**
        - AES (Advanced Encryption Standard)
        - RSA for public-key cryptography
        - ChaCha20 for stream encryption
        - Always use established cryptographic libraries
        """)

if __name__ == "__main__":
    main()
