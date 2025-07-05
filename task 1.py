def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Tool ===")
    choice = input("Type 'E' to encrypt or 'D' to decrypt: ").strip().upper()
    
    if choice not in ['E', 'D']:
        print("Invalid choice. Please select 'E' or 'D'.")
        return

    message = input("Enter your message: ")
    
    try:
        shift = int(input("Enter shift value (e.g., 3): "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return

    if choice == 'E':
        encrypted = caesar_cipher_encrypt(message, shift)
        print("Encrypted Message:", encrypted)
    else:
        decrypted = caesar_cipher_decrypt(message, shift)
        print("Decrypted Message:", decrypted)

if __name__ == "__main__":
    main()
