# Assignment 2 part A which is for Custom Encryption & Decryption Program
# File location will be  C:\Users\bijen\Downloads\Assignment 2

import os
#Step 1: We will define the paths of file
BASE_DIR = r"C:\Users\bijen\Downloads\Assignment 2"

RAW_FILE = os.path.join(BASE_DIR, "raw_text.txt")
ENC_FILE = os.path.join(BASE_DIR, "encrypted_text.txt")
DEC_FILE = os.path.join(BASE_DIR, "decrypted_text.txt")

#Step 2:We will encrypt a single character
def encrypt_char(char, shift1, shift2):
    # Lowercase letters
    if char.islower():
        pos = ord(char) - ord('a')

        if pos <= 12:  # a-m
            new_pos = (pos + (shift1 * shift2)) % 26
        else:          # n-z
            new_pos = (pos - (shift1 + shift2)) % 26

        return chr(new_pos + ord('a'))

    # Uppercase letters
    elif char.isupper():
        pos = ord(char) - ord('A')

        if pos <= 12:  # A-M
            new_pos = (pos - shift1) % 26
        else:          # N-Z
            new_pos = (pos + (shift2 ** 2)) % 26

        return chr(new_pos + ord('A'))

    # Other characters unchanged
    return char

#Step 3:We will decrypt a single character
def decrypt_char(char, shift1, shift2):
    # Reverse of encryption rules

    if char.islower():
        pos = ord(char) - ord('a')

        if pos <= 12:  # a-m
            new_pos = (pos - (shift1 * shift2)) % 26
        else:          # n-z
            new_pos = (pos + (shift1 + shift2)) % 26

        return chr(new_pos + ord('a'))

    elif char.isupper():
        pos = ord(char) - ord('A')

        if pos <= 12:  # A-M
            new_pos = (pos + shift1) % 26
        else:          # N-Z
            new_pos = (pos - (shift2 ** 2)) % 26

        return chr(new_pos + ord('A'))

    return char

#Step 4;We will encrypt a single file
def encrypt_file(shift1, shift2):
    if not os.path.exists(RAW_FILE):
        print("❌ raw_text.txt not found in Assignment 2 folder.")
        return

    with open(RAW_FILE, "r", encoding="utf-8") as infile, \
         open(ENC_FILE, "w", encoding="utf-8") as outfile:

        for line in infile:
            for char in line:
                outfile.write(encrypt_char(char, shift1, shift2))

    print("Encryption completed.")

#Step 5:Decrypting the full file
def decrypt_file(shift1, shift2):
    with open(ENC_FILE, "r", encoding="utf-8") as infile, \
         open(DEC_FILE, "w", encoding="utf-8") as outfile:

        for line in infile:
            for char in line:
                outfile.write(decrypt_char(char, shift1, shift2))

    print("Decryption completed.")

#Step 6:Verify if decryption matches original
def verify_files():
    with open(RAW_FILE, "r", encoding="utf-8") as f1, \
         open(DEC_FILE, "r", encoding="utf-8") as f2:

        if f1.read() == f2.read():
            print("✅ Decryption successful: Files match.")
        else:
            print("❌ Decryption failed: Files do NOT match.")

#Step 7:Main program Runs all the step
def main():
 #7.1 We will get user input for shifts
    shift1 = int(input("Enter shift1 value: "))
    shift2 = int(input("Enter shift2 value: "))
#7.2 Encrypt the original text
    encrypt_file(shift1, shift2)
    #7.3  We will decrypt encrypted text
    decrypt_file(shift1, shift2)
    #7.4 We wil verify the correctness
    verify_files()

#8Step 8:Execute the programs
main()



