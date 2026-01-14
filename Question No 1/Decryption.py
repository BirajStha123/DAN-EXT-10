# ------------------------------------------------------------
# Decryption Program  using Vigenère Cipher
# ------------------------------------------------------------
# This program will help us decrypt an encrypted message using a key.
# The result will be printed to console and will be saved to a file.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Function will help us  to decrypt a message using Vigenère Cipher
# ------------------------------------------------------------
def decrypt(encrypted_message, key):
    """
    Decrypts a message using the Vigenère cipher.

    Parameters:
        encrypted_message (str): The message to decrypt
        key (str): The encryption key

    Returns:
        str: Decrypted message
    """
    decrypted = []
    key = key.upper()
    key_index = 0

    for char in encrypted_message:
        if char.isalpha():  # Only letters will be decrypted
            shift = ord(key[key_index]) - ord('A')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))

            decrypted.append(decrypted_char)
            key_index = (key_index + 1) % len(key)  # Moving to next letter in key
        else:
            decrypted.append(char)  # Non-letter characters will remain unchanged

    return ''.join(decrypted)

# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------
def main():
    print("------ Decryption Program ------")
    
    # Input will encryptedmessage from  the user
    encrypted_message = input("Enter the encrypted message: ")
    
    # Ihe key used for encryption will be entered 
    key = input("Enter the decryption key: ")
    
    # Decryption will be performed
    decrypted_message = decrypt(encrypted_message, key)
    
    # Displaying the  result
    print("\nDecrypted Message:", decrypted_message)
    
    # Saving the result to a file
    with open("decrypted_output.txt", "w") as f:
        f.write(decrypted_message)
    
    print("\nDecrypted message saved to 'decrypted_output.txt'")

# ------------------------------------------------------------
# Running the program
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
