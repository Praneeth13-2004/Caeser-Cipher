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


st.title("Caesar Cipher App")

text = st.text_area("Enter text:")
shift = st.number_input("Enter shift value:", min_value=1, max_value=25, value=3)
mode = st.radio("Choose mode:", ["Encrypt", "Decrypt"])

if st.button("Run Caesar Cipher"):
    if text.strip():
        output = caesar_cipher(text, shift, mode.lower())
        st.subheader("Result:")
        st.success(output)
    else:
        st.warning("Please enter some text to proceed.")

