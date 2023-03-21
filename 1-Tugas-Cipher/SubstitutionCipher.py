import tkinter as tk
from tkinter import ttk
import string

# Membuat dictionary huruf yang diganti
substitution_dict = {
    'a': 'm',
    'b': 'n',
    'c': 'b',
    'd': 'v',
    'e': 'c',
    'f': 'x',
    'g': 'z',
    'h': 'l',
    'i': 'k',
    'j': 'j',
    'k': 'h',
    'l': 'g',
    'm': 'f',
    'n': 'd',
    'o': 's',
    'p': 'a',
    'q': 'p',
    'r': 'o',
    's': 'i',
    't': 'u',
    'u': 'y',
    'v': 't',
    'w': 'r',
    'x': 'e',
    'y': 'w',
    'z': 'q'
}

# Membuat fungsi untuk melakukan penggantian huruf
def substitution_cipher(text):
    result = ""
    for char in text.lower():
        if char in string.ascii_lowercase:
            result += substitution_dict[char]
        else:
            result += char
    return result

# Membuat fungsi untuk button "Enkripsi"
def enkripsi():
    plaintext = plaintext_entry.get()
    ciphertext = substitution_cipher(plaintext)
    ciphertext_entry.delete(0, tk.END)
    ciphertext_entry.insert(0, ciphertext)

# Membuat fungsi untuk button "Dekripsi"
def dekripsi():
    ciphertext = ciphertext_entry.get()
    plaintext = substitution_cipher(ciphertext)
    plaintext_entry.delete(0, tk.END)
    plaintext_entry.insert(0, plaintext)

# Membuat window
root = tk.Tk()
root.title("Substitution Cipher")

# Membuat label "Plaintext"
plaintext_label = ttk.Label(root, text="Plaintext:")
plaintext_label.grid(column=0, row=0, padx=5, pady=5)

# Membuat entry untuk plaintext
plaintext_entry = ttk.Entry(root, width=30)
plaintext_entry.grid(column=1, row=0, padx=5, pady=5)

# Membuat label "Ciphertext"
ciphertext_label = ttk.Label(root, text="Ciphertext:")
ciphertext_label.grid(column=0, row=1, padx=5, pady=5)

# Membuat entry untuk ciphertext
ciphertext_entry = ttk.Entry(root, width=30)
ciphertext_entry.grid(column=1, row=1, padx=5, pady=5)

# Membuat button "Enkripsi"
enkripsi_button = ttk.Button(root, text="Enkripsi", command=enkripsi)
enkripsi_button.grid(column=0, row=2, padx=5, pady=5)

# Membuat button "Dekripsi"
dekripsi_button = ttk.Button(root, text="Dekripsi", command=dekripsi)
dekripsi_button.grid(column=1, row=2, padx=5, pady=5)

# Menjalankan window
root.mainloop()
