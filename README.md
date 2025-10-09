**Code by**

***Raavinuthala Sai Praneeth Karthikeya***

***Yatharth Jain***

Advanced Caesar Cipher Web Tool
An interactive, web-based tool built with Streamlit and Python to demonstrate the principles of the classic Caesar Cipher, serving as an excellent educational introduction to symmetric-key cryptography.

Features
This application offers a modern and user-friendly interface for cryptographic demonstration:

Interactive Controls: All inputs—text, shift key, and mode (Encrypt/Decrypt)—are housed in a clean sidebar for seamless operation.

Variable Shift Key: Allows the user to select any shift value between 1 and 25.

Algorithmic Accuracy: The core logic correctly implements modulus 26 arithmetic to handle alphabet wrap-around (e.g., A → Z).

Preservation of Context: The application intelligently preserves character casing (uppercase/lowercase) and retains all non-alphabetic characters (spaces, punctuation, numbers) in the output.

Educational Content: Includes a dedicated "Cipher Information" tab that explains the cipher's history, symmetric key principle, and inherent security weaknesses.

Getting Started
Follow these instructions to run the application on your local machine.

Prerequisites
You need to have Python installed (Python 3.8+ is recommended).

Installation
Clone the Repository:

git clone [https://github.com/your-username/caesar-cipher-app.git](https://github.com/your-username/caesar-cipher-app.git)
cd caesar-cipher-app

Install Dependencies:
This project requires the streamlit library.

pip install streamlit

Running the Application
Save the code into a file named app.py. Then, execute it using the Streamlit CLI:

streamlit run app.py

The application will automatically open in your default web browser, usually at http://localhost:8501.

Usage
Enter Text: Use the "Enter text for processing" area in the sidebar to type or paste your message.

Select Key: Use the "Select shift value (Key)" slider to choose your desired shift, from 1 to 25.

Choose Mode: Select either "Encrypt" (to create ciphertext) or "Decrypt" (to recover plaintext).

Execute: Click the "Execute Cipher Operation" button.

View Result: The result will be displayed in the "Operation Result" tab in the main application area.

Future Scope
The project is designed to be a foundation for further educational enhancements:

Advanced Ciphers: Integration of more complex algorithms, such as the Vigenère Cipher or the Hill Cipher, to compare security levels.

Cryptanalysis Module: Addition of a Frequency Analysis Tool to visually chart letter occurrences, demonstrating how easily the Caesar cipher can be broken.

Brute-Force Solver: Implementation of a feature that automatically runs decryption against all 25 possible keys, instantly revealing the plaintext, thus completing the practical demonstration of its inherent weakness.




