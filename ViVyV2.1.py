# Welcome to my encoder!

# This encoder uses a standard Viginere encrypter.
# But it's optimised by having the space and other special characters
# included in the list
# making it safer and allowing special characters.

import tkinter as tk # Imports the built-in gui system
import math # Imports the standard math functions

alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',

    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',

    '.', ',', '?', '!', '(', ')', '[', ']', '{', '}',
    ':', ';', "'", '"', '-', '_', '/', '\\', '@', '#',
    '$', '%', '&', '*', '+', '=', '<', '>', ' ', '`', 
    '~', '€', '£', '^',

    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
] # Creates the alphabet list.
# Feel free to add more characters for extra compatibility.
# Note: this WILL ALTER THE PROGRAM
# encrypted items may not be decryptable if u use an adjusted alphabet
# That meams also no inter-version en- and decryptions possible
# because different versions may contain different alphabets

def encrypt(code, key): # Creates the encrypt function
    resultList = []
    for place in range(len(code)):
        resultList.append(
            alphabet[
                (alphabet.index(code[place]) + alphabet.index(key[place]))
                % len(alphabet)
            ]
        )
    return "".join(resultList)


def decrypt(code, key): # Creates the decrypt function
    resultList = []
    for place in range(len(code)):
        resultList.append(
            alphabet[
                (alphabet.index(code[place]) - alphabet.index(key[place]))
                % len(alphabet)
            ]
        )
    return "".join(resultList)


def makekey(code, key): # Makes the key long enough for the entire message
    keyList = []
    for i in range(math.ceil(len(code) / len(key))):
        keyList.append(key)
    return "".join(keyList)


# Tkinter GUI system

def run_encrypt(): 
    code = code_entry.get()
    key = key_entry.get()

    if not code or not key: # Checks if the correct input is given
        output_entry.delete(0, tk.END)
        output_entry.insert(0, "Wrong input given!")
        return

    try:
        key = makekey(code, key)
        output = encrypt(code, key)

        output_entry.delete(0, tk.END)
        output_entry.insert(0, output)

    except ValueError: # Checks if the correct input is given
        output_entry.delete(0, tk.END)
        output_entry.insert(0, "Wrong input given!")

# The second part is all the GUI used to take inputs and output the result

def run_decrypt():
    code = code_entry.get()
    key = key_entry.get()

    if not code or not key: # Checks if the correct input is given
        output_entry.delete(0, tk.END)
        output_entry.insert(0, "Wrong input given!")
        return

    try:
        key = makekey(code, key)
        output = decrypt(code, key)

        output_entry.delete(0, tk.END)
        output_entry.insert(0, output)

    except ValueError: # Checks if the correct input is given
        output_entry.delete(0, tk.END)
        output_entry.insert(0, "Wrong input given!")


window = tk.Tk() # Creates the main window
window.title("ViVyV2.1") # Titles it ViVyV2.1
window.geometry("1920x1080") # Makes the screen 1920 by 1080 pixels

font = ("Arial", 25) # creates the font

tk.Label(
    window,
    text="Code:",
    font=font
).pack(pady=10) # Creates the "Code:" text next to the code input

code_entry = tk.Entry(
    window,
    width=50,
    font=font
)
code_entry.pack(pady=10) # Creates the actual code input

tk.Label(
    window,
    text="Key:",
    font=font
).pack(pady=10) # Creates the "Key:" text next to the key input

key_entry = tk.Entry(
    window,
    width=50,
    font=font
)
key_entry.pack(pady=10) # Creates the actual key input

tk.Button(
    window,
    text="Encrypt",
    command=run_encrypt,
    font=font
).pack(pady=10) # Creates the encrypt button

tk.Button(
    window,
    text="Decrypt",
    command=run_decrypt,
    font=font
).pack(pady=10) # Creates the decrypt button

tk.Label(
    window,
    text="Output:",
    font=font
).pack(pady=10) # Creates the "Output:" text next to the output section

output_entry = tk.Entry(
    window,
    width=50,
    font=font
)
output_entry.pack(pady=20) # Creates the actual output section

window.mainloop()

# If you encounter any trouble with the program
# or want to propose any idea for a future version
# please contact me on one of these platforms:

# GitHub: Vyprinnn
# Discord: Vyprinnn
# Gmail: vyprinnn@gmail.com
# Minecraft: Vyprinnn
# Roblox: Vyprinnn