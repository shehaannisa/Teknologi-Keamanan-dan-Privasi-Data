from tkinter import *

# Enkripsi
def enkripsi():
    plaintext = entry1.get().upper()
    key = int(entry2.get())
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            ciphertext += chr((ord(char) - 65 + key) % 26 + 65)
        else:
            ciphertext += char
    entry3.delete(0, END)
    entry3.insert(0, ciphertext)

# Dekripsi
def dekripsi():
    ciphertext = entry1.get().upper()
    key = int(entry2.get())
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            plaintext += chr((ord(char) - 65 - key) % 26 + 65)
        else:
            plaintext += char
    entry3.delete(0, END)
    entry3.insert(0, plaintext)

# Membuat GUI
root = Tk()
root.title("Shift Cipher")

# Membuat Label
label1 = Label(root, text="Plaintext:")
label1.grid(row=0, column=0, padx=5, pady=5)
label2 = Label(root, text="Key:")
label2.grid(row=1, column=0, padx=5, pady=5)
label3 = Label(root, text="Hasil:")
label3.grid(row=2, column=0, padx=5, pady=5)

# Membuat text entry boxes
entry1 = Entry(root, width=30)
entry1.grid(row=0, column=1, padx=5, pady=5)
entry2 = Entry(root, width=30)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry3 = Entry(root, width=30)
entry3.grid(row=2, column=1, padx=5, pady=5)

# Membuat enkrip dan dekrip button
enkripsi_button = Button(root, text="Enkripsi", command=enkripsi)
enkripsi_button.grid(row=3, column=0, padx=5, pady=5)
dekripsi_button = Button(root, text="Dekripsi", command=dekripsi)
dekripsi_button.grid(row=3, column=1, padx=5, pady=5)

# Menjalankan GUI
root.mainloop()
