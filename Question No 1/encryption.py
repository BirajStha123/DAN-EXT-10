# ------------------------------------------------------------
# Encryption/Decryption Program
# ------------------------------------------------------------
# This program encrypts and decrypts messages using a key.
# It will outputs the result to the console and will save them to files.
# ------------------------------------------------------------

import os

# ------------------------------------------------------------
# Function will be  encrypt a message using Vigenère Cipher
# ------------------------------------------------------------
def encrypt(message, key):
    encrypted = []
    key = key.upper()  # Converting  the key to uppercase
    key_index = 0

    for char in message:
        if char.isalpha():  # Only encrypting the  letters
            shift = ord(key[key_index]) - ord('A')  # Geting the  shift from key
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

            encrypted.append(encrypted_char)
            key_index = (key_index + 1) % len(key)  # Moving  to further key letter
        else:
            encrypted.append(char)  # Non-letters will remain unchanged

    return ''.join(encrypted)

# ------------------------------------------------------------
# Function for decryping a message which uses Vigenère Cipher
# ------------------------------------------------------------
def decrypt(encrypted_message, key):
    decrypted = []
    key = key.upper()
    key_index = 0

    for char in encrypted_message:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))

            decrypted.append(decrypted_char)
            key_index = (key_index + 1) % len(key)
        else:
            decrypted.append(char)

    return ''.join(decrypted)

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
def main():
    print("------ Encryption/Decryption Program ------")
    
    # Putting input message from user
    message = input("Enter the message: ")
    
    # Putting input key from user
    key = input("Enter the encryption key: ")
    
    # Encrypting the message
    encrypted_text = encrypt(message, key)
    print("\nEncrypted Text:", encrypted_text)
    
    # Decrypting the message
    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted Text:", decrypted_text)
    
    # Saving results to files
    with open("encrypted_output.txt", "w") as f:
        f.write(encrypted_text)
    
    with open("decrypted_output.txt", "w") as f:
        f.write(decrypted_text)
    
    print("\nResults saved to 'encrypted_output.txt' and 'decrypted_output.txt'")

# ------------------------------------------------------------
# Running the program
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
