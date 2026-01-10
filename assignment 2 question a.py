# Custom Encryption–Decryption Program
# Reads from raw_text.txt, encrypts, decrypts, and verifies correctness

def encrypt_char(char, shift1, shift2):
    # Encrypt lowercase letters
    if char.islower():
        pos = ord(char) - ord('a')

        if pos <= 12:  # a-m
            shift = shift1 * shift2
            new_pos = (pos + shift) % 26
        else:  # n-z
            shift = shift1 + shift2
            new_pos = (pos - shift) % 26

        return chr(new_pos + ord('a'))

    # Encrypt uppercase letters
    elif char.isupper():
        pos = ord(char) - ord('A')

        if pos <= 12:  # A-M
            new_pos = (pos - shift1) % 26
        else:  # N-Z
            new_pos = (pos + (shift2 ** 2)) % 26

        return chr(new_pos + ord('A'))

    # Other characters remain unchanged
    else:
        return char


def decrypt_char(char, shift1, shift2):
    # Decrypt lowercase letters
    if char.islower():
        pos = ord(char) - ord('a')

        if pos <= 12:  # a-m (originally shifted forward)
            shift = shift1 * shift2
            new_pos = (pos - shift) % 26
        else:  # n-z (originally shifted backward)
            shift = shift1 + shift2
            new_pos = (pos + shift) % 26

        return chr(new_pos + ord('a'))

    # Decrypt uppercase letters
    elif char.isupper():
        pos = ord(char) - ord('A')

        if pos <= 12:  # A-M (originally shifted backward)
            new_pos = (pos + shift1) % 26
        else:  # N-Z (originally shifted forward)
            new_pos = (pos - (shift2 ** 2)) % 26

        return chr(new_pos + ord('A'))

    # Other characters remain unchanged
    else:
        return char


def encrypt_file(shift1, shift2):
    with open("raw_text.txt", "r", encoding="utf-8") as infile, \
         open("encrypted_text.txt", "w", encoding="utf-8") as outfile:

        for line in infile:
            encrypted_line = ""
            for char in line:
                encrypted_line += encrypt_char(char, shift1, shift2)
            outfile.write(encrypted_line)


def decrypt_file(shift1, shift2):
    with open("encrypted_text.txt", "r", encoding="utf-8") as infile, \
         open("decrypted_text.txt", "w", encoding="utf-8") as outfile:

        for line in infile:
            decrypted_line = ""
            for char in line:
                decrypted_line += decrypt_char(char, shift1, shift2)
            outfile.write(decrypted_line)


def verify_files():
    with open("raw_text.txt", "r", encoding="utf-8") as f1, \
         open("decrypted_text.txt", "r", encoding="utf-8") as f2:

        if f1.read() == f2.read():
            print("✅ Decryption successful: Files match.")
        else:
            print("❌ Decryption failed: Files do NOT match.")


# ================= MAIN PROGRAM =================

def main():
    shift1 = int(input("Enter shift1 value: "))
    shift2 = int(input("Enter shift2 value: "))

    encrypt_file(shift1, shift2)
    print("Encryption completed.")

    decrypt_file(shift1, shift2)
    print("Decryption completed.")

    verify_files()


main()

