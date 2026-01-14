# ------------------------------------------------------------
# Encryption & Decryption Program done for  Main File
# ------------------------------------------------------------
# This program will allow the user to encrypt or decrypt a message
# Results are displayed and saved using a key (Vigenère Cipher). 
# ------------------------------------------------------------

# ------------------------------------------------------------
# Function used for encrypting a message
# ------------------------------------------------------------
def encrypt(message, key):
    """
    Encrypts a message using the Vigenère cipher.

    Parameters:
        message (str): The plaintext message
        key (str): The encryption key

    Returns:
        str: Encrypted message
    """
    encrypted = []
    key = key.upper()
    key_index = 0

    for char in message:
        if char.isalpha():  # Encrypting letters only
            shift = ord(key[key_index]) - ord('A')
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

            encrypted.append(encrypted_char)
            key_index = (key_index + 1) % len(key)
        else:
            encrypted.append(char)  # Keeping non-letter characters unchanged

    return ''.join(encrypted)

# ------------------------------------------------------------
# Function used for decrypting a message
# ------------------------------------------------------------
def decrypt(encrypted_message, key):
    """
    Decrypts a message using the Vigenère cipher.

    Parameters:
        encrypted_message (str): The encrypted message
        key (str): The encryption key

    Returns:
        str: Decrypted message
    """
    decrypted = []
    key = key.upper()
    key_index = 0

    for char in encrypted_message:
        if char.isalpha():  #Decrypting letters only
            shift = ord(key[key_index]) - ord('A')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))

            decrypted.append(decrypted_char)
            key_index = (key_index + 1) % len(key)
        else:
            decrypted.append(char)  # Keeping non-letter characters same

    return ''.join(decrypted)

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
def main():
    print("------ Encryption & Decryption Program ------")
    
    # User let choose the operation
    choice = input("Choose an option:\n1. Encrypt\n2. Decrypt\nEnter 1 or 2: ")

    if choice not in ["1", "2"]:
        print("Invalid choice! Exiting program.")
        return

    # Message and Key will be entered
    message = input("Enter the message: ")
    key = input("Enter the key: ")

    if choice == "1":
        # Encrypting the message
        result = encrypt(message, key)
        print("\nEncrypted Message:", result)
        with open("encrypted_output.txt", "w") as f:
            f.write(result)
        print("\nEncrypted message saved to 'encrypted_output.txt'")

    else:
        # Decrypting the message
        result = decrypt(message, key)
        print("\nDecrypted Message:", result)
        with open("decrypted_output.txt", "w") as f:
            f.write(result)
        print("\nDecrypted message saved to 'decrypted_output.txt'")

# ------------------------------------------------------------
# Running the program
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
