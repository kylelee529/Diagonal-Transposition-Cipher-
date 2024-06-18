import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def create_matrix_top_to_bottom(message, cols):
    """ Create a matrix with the message written top to bottom in columns. """
    rows = (len(message) + cols - 1) // cols  # Ceiling division to get the number of rows
    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    idx = 0
    for col in range(cols):
        for row in range(rows):
            if idx < len(message):
                matrix[row][col] = message[idx]
                idx += 1
            else:
                matrix[row][col] = ''

    return matrix

def split_and_switch(matrix):
    """ Split the matrix diagonally and switch the sides. """
    rows = len(matrix)
    cols = len(matrix[0])
    switched_matrix = [['' for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if row >= col:
                # Bottom-left triangle (including diagonal)
                switched_matrix[row][col] = matrix[row - col][col]
            else:
                # Top-right triangle
                switched_matrix[row][col] = matrix[row][cols - col + row - 1]

    return switched_matrix

def encrypt(matrix):
    """ Apply diagonal transposition cipher to the matrix. """
    rows = len(matrix)
    cols = len(matrix[0])
    cipher = ['' for _ in range(rows + cols - 1)]

    for row in range(rows):
        for col in range(cols):
            cipher[row + col] += matrix[row][col]

    return ''.join(cipher)

def handle_encrypt():
    message = text_input.get("1.0", "end-1c").replace('\n', '')
    if not message:
        messagebox.showwarning("Input Error", "Please enter some text to encrypt.")
        return
    cols = 4  # fixed number of columns, adjust as needed
    matrix = create_matrix_top_to_bottom(message, cols)
    switched_matrix = split_and_switch(matrix)
    encrypted_message = encrypt(switched_matrix)
    
    # Clear previous content and insert encrypted message
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, encrypted_message)

    # Adjust the height of the text input area if necessary
    text_input.config(height=max(10, len(encrypted_message) // 50))

# Set up the main application window
app = tk.Tk()
app.title("Diagonal Transposition Cipher")

# Text input for the message
text_input = tk.Text(app, height=10, width=50)
text_input.pack(pady=10)

# Encrypt button
encrypt_button = tk.Button(app, text="Encrypt", command=handle_encrypt)
encrypt_button.pack(pady=5)

# Scrollbar for the result text
scrollbar = tk.Scrollbar(app, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Result text area with scrolling capability
result_text = tk.Text(app, height=10, width=50, wrap=tk.WORD, yscrollcommand=scrollbar.set)
result_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
result_text.config(relief=tk.SUNKEN, bd=2)
scrollbar.config(command=result_text.yview)

# Start the GUI event loop
app.mainloop()
