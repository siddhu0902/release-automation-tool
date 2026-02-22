import string
import random
from collections import Counter

# ---- Password Strength Analyzer ----
def analyze_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    score = 0

    print("\nChecking password strength...")
    if length >= 8:
        score += 1
    else:
        print("Password should be at least 8 characters.")

    if has_upper:
        score += 1
    else:
        print("Password should contain uppercase letters.")

    if has_lower:
        score += 1
    else:
        print("Password should contain lowercase letters.")

    if has_digit:
        score += 1
    else:
        print("Password should contain digits.")

    if has_special:
        score += 1
    else:
        print("Password should contain special characters.")

    if score == 5:
        print("Strength: Strong")
    elif score >= 3:
        print("Strength: Medium")
    else:
        print("Strength: Weak")

# ---- Simple Caesar Cipher File Encryption ----
def caesar_encrypt(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def caesar_decrypt(cipher, shift=3):
    return caesar_encrypt(cipher, -shift)

def encrypt_file(filename, shift=3):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        encrypted = caesar_encrypt(content, shift)
        with open(filename + ".enc", 'w', encoding='utf-8') as file:
            file.write(encrypted)
        print("File encrypted and saved as:", filename + ".enc")
    except Exception as e:
        print("Error:", e)

def decrypt_file(filename, shift=3):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        decrypted = caesar_decrypt(content, shift)
        with open(filename.replace(".enc", ".dec"), 'w', encoding='utf-8') as file:
            file.write(decrypted)
        print("File decrypted and saved as:", filename.replace(".enc", ".dec"))
    except Exception as e:
        print("Error:", e)

# ---- Detect Repeated Passwords ----
def detect_repeats(passwords):
    repeat_counts = Counter(passwords)
    repeats = [pw for pw, cnt in repeat_counts.items() if cnt > 1]
    if repeats:
        print("Repeated passwords found:", repeats)
    else:
        print("No repeated passwords found.")

# ---- Secure Password Generator ----
def generate_secure_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.SystemRandom().choice(chars) for _ in range(length))
        if (any(c.isupper() for c in password) and any(c.islower() for c in password)
            and any(c.isdigit() for c in password) and any(c in string.punctuation for c in password)):
            return password

# ---- Main Menu ----
def main():
    while True:
        print("\nCyber Security Suite")
        print("--------------------")
        print("1. Analyze Password Strength")
        print("2. Encrypt a File (Caesar Cipher)")
        print("3. Decrypt a File (Caesar Cipher)")
        print("4. Check Repeated Passwords")
        print("5. Generate Secure Password")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            pw = input("Enter password to analyze: ")
            analyze_password_strength(pw)
        elif choice == '2':
            fname = input("Enter file name to encrypt: ")
            encrypt_file(fname)
        elif choice == '3':
            fname = input("Enter file name to decrypt (should end with .enc): ")
            decrypt_file(fname)
        elif choice == '4':
            pw_list = input("Enter passwords separated by commas: ").split(",")
            detect_repeats([pw.strip() for pw in pw_list])
        elif choice == '5':
            length = input("Enter desired password length (default 12): ")
            length = int(length) if length.isdigit() else 12
            pw = generate_secure_password(length)
            print("Generated secure password:", pw)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()