# Diagonal Transposition Cipher GUI

This project implements a Diagonal Transposition Cipher with a Tkinter-based GUI. The cipher encrypts messages by first reorganizing the plaintext into a grid written top to bottom, splitting the grid diagonally, switching the sides, and then reading the grid diagonally.

## Features

- **Encrypt Messages**: Input plaintext, and the application will encrypt it using the specified diagonal transposition cipher method.
- **User-friendly GUI**: Simple interface to input text and display encrypted messages.
- **Matrix-based Encryption**: The encryption algorithm first organizes the plaintext into a matrix filled top to bottom, splits the matrix diagonally, switches the sides, and then reads diagonally to create the cipher text.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## How to Use

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/kylelee529/diagonal-transposition-cipher.git
    cd diagonal-transposition-cipher
    ```

2. **Run the Application**:
    ```sh
    python diagonal_transposition_cipher_gui.py
    ```

3. **Encrypt a Message**:
    - Enter the plaintext you want to encrypt in the text input area.
    - Click the **Encrypt** button to see the encrypted message.

## File Structure

- `diagonal_transposition_cipher_gui.py`: Main Python script with the Tkinter GUI and encryption logic.
- `README.md`: This file.

## Encryption Process

1. **Matrix Creation**:
    - The plaintext is organized into a matrix where the text is written top to bottom in columns.

2. **Diagonal Split and Switch**:
    - The matrix is split diagonally and the two parts are switched.

3. **Diagonal Transposition**:
    - The matrix is then read diagonally to create the encrypted message.

