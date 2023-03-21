import tkinter as tk
from tkinter import messagebox

def vigenere_cipher(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_as_int = [ord(i) for i in plaintext]
    ciphertext = ""
    for i in range(len(plaintext_as_int)):
        value = (plaintext_as_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext

def enkripsi():
    plaintext = entry_plaintext.get()
    key = entry_key.get()
    ciphertext = vigenere_cipher(plaintext, key)
    entry_ciphertext.delete(0, tk.END)
    entry_ciphertext.insert(0, ciphertext)

def dekripsi():
    ciphertext = entry_ciphertext.get()
    key = entry_key.get()
    plaintext = ""
    for i in range(len(ciphertext)):
        value = (ord(ciphertext[i]) - ord(key[i % len(key)]) + 26) % 26
        plaintext += chr(value + 65)
    entry_plaintext.delete(0, tk.END)
    entry_plaintext.insert(0, plaintext)

# Membuat GUI
root = tk.Tk()
root.title("Vigenere Cipher")

# Membuat Label
label_plaintext = tk.Label(root, text="Plaintext:")
label_key = tk.Label(root, text="Key:")
label_ciphertext = tk.Label(root, text="Ciphertext:")
entry_plaintext = tk.Entry(root)
entry_key = tk.Entry(root)
entry_ciphertext = tk.Entry(root)
button_enkripsi = tk.Button(root, text="Enkripsi", command=enkripsi)
button_dekripsi = tk.Button(root, text="Dekripsi", command=dekripsi)

# Add widgets to GUI
label_plaintext.grid(row=0, column=0, padx=10, pady=10, sticky="w")
label_key.grid(row=1, column=0, padx=10, pady=10, sticky="w")
label_ciphertext.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_plaintext.grid(row=0, column=1, padx=10, pady=10)
entry_key.grid(row=1, column=1, padx=10, pady=10)
entry_ciphertext.grid(row=2, column=1, padx=10, pady=10)
button_enkripsi.grid(row=3, column=0, padx=10, pady=10)
button_dekripsi.grid(row=3, column=1, padx=10, pady=10)

# Jalankan GUI
root.mainloop()
