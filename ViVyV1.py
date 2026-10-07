# Welcome to my encoder!

# This encoder uses a standard Viginere encrypter.
# But it's optimised by having the space and other special characters
# included in the list
# making it safer and allowing special characters.

import tkinter as tk  # imports a built-in GUI system called tkinter
import math

alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',

    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',

    '.', ',', '?', '!', '(', ')', '[', ']', '{', '}',
    ':', ';', "'", '"', '-', '_', '/', '\\', '@', '#',
    '$', '%', '&', '*', '+', '=', '<', '>', ' '
]


def encrypt(code, key):
    resultList = []
    for place in range(len(code)):
        resultList.append(
            alphabet[
                (alphabet.index(code[place]) + alphabet.index(key[place]))
                % len(alphabet)
            ]
        )
    return "".join(resultList)


def decrypt(code, key):
    resultList = []
    for place in range(len(code)):
        resultList.append(
            alphabet[
                (alphabet.index(code[place]) - alphabet.index(key[place]))
                % len(alphabet)
            ]
        )
    return "".join(resultList)


def makekey(code, key):
    keyList = []
    for i in range(math.ceil(len(code) / len(key))):
        keyList.append(key)
    return "".join(keyList)


# Tkinter GUI

def run_encrypt():
    code = code_entry.get()
    key = key_entry.get()

    if not code or not key:
        output_label.config(text="Wrong input given!")
        return

    try:
        key = makekey(code, key)
        output = encrypt(code, key)
        output_label.config(text=output)
    except ValueError:
        output_label.config(text="Wrong input given!")


def run_decrypt():
    code = code_entry.get()
    key = key_entry.get()

    if not code or not key:
        output_label.config(text="Wrong input given!")
        return

    try:
        key = makekey(code, key)
        output = decrypt(code, key)
        output_label.config(text=output)
    except ValueError:
        output_label.config(text="Wrong input given!")


window = tk.Tk()
window.title("ViVyV1")
window.geometry("1920x1080")

# 25px font
font = ("Arial", 25)

tk.Label(window, text="Code:", font=font).pack(pady=10)

code_entry = tk.Entry(window, width=50, font=font)
code_entry.pack(pady=10)

tk.Label(window, text="Key:", font=font).pack(pady=10)

key_entry = tk.Entry(window, width=50, font=font)
key_entry.pack(pady=10)

tk.Button(
    window,
    text="Encrypt",
    command=run_encrypt,
    font=font
).pack(pady=10)

tk.Button(
    window,
    text="Decrypt",
    command=run_decrypt,
    font=font
).pack(pady=10)

output_label = tk.Label(window, text="Output:", font=font)
output_label.pack(pady=30)

window.mainloop()