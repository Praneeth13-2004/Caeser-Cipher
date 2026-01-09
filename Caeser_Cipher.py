"""
@authors: Raavinuthala Sai Praneeth Karthikeya
Project: Caesar Cipher (Shift Cipher)
"""


import streamlit as st


def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def main():
    st.set_page_config(
        page_title="Cipher Tool",
        page_icon="🔒",
        layout="wide"
    )

    if 'output' not in st.session_state:
        st.session_state.output = "Enter text and run the cipher."
    
    if 'input_text' not in st.session_state:
        st.session_state.input_text = ""

    with st.sidebar:
        st.header("Cipher Controls")
        
        
        input_text = st.text_area("Enter text for processing:", key='input_key', height=200, value=st.session_state.input_text)
        st.session_state.input_text = input_text
        
        
        shift_value = st.slider("Select shift value (Key):", 1, 25, 3, key='shift_key')
        
        
        mode_selection = st.radio("Choose operation mode:", ["Encrypt", "Decrypt"], key='mode_key')
        
        st.markdown("---")

        if st.button("Execute Cipher Operation", use_container_width=True, type="primary"):
            if st.session_state.input_text.strip():
                st.session_state.output = caesar_cipher(
                    st.session_state.input_text, 
                    shift_value, 
                    mode_selection.lower()
                )
                st.success(f"{mode_selection} successful!")
            else:
                st.session_state.output = "Please enter some text to proceed."
                st.warning("Input text is empty.")

    st.title("Advanced Caesar Cipher Web Tool")

    tab1, tab2 = st.tabs(["Operation Result", "Cipher Information"])

    with tab1:
        st.subheader(f"{mode_selection} Result:")
        st.markdown("---")
        
        output_container = st.container(border=True)
        with output_container:
            st.code(st.session_state.output, language='text')
            
        st.markdown("---")
        col_buttons = st.columns(3)
        with col_buttons[0]:
            if st.button("Clear Output"):
                st.session_state.output = "Result cleared."
                st.session_state.input_text = ""
                st.rerun()

    with tab2:
        st.header("Understanding the Caesar Cipher (Shift Cipher)")
        st.write("""
            The Caesar Cipher is one of the simplest and most well-known encryption techniques. It is a type of monoalphabetic substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down or up the alphabet. This fixed number, the 'shift value', serves as the secret key.
        """)
        
        st.markdown("### Key Operational Principles:")
        st.markdown("- **Symmetric Key:** The same key is used for both encryption and decryption.")
        st.markdown("- **Modulus** $26$ **Arithmetic:** The operation relies on modulo arithmetic to wrap the alphabet from Z back to A (or vice versa during decryption). The formula for encryption is $C = (P + K) \mod 26$, where $C$ is the ciphertext letter, $P$ is the plaintext letter, and $K$ is the key.")
        st.markdown("- **Security:** Given only 25 possible keys, the cipher offers virtually no security against modern cryptanalysis, which typically involves a brute-force attack or simple frequency analysis.")

if __name__ == "__main__":
    main()

