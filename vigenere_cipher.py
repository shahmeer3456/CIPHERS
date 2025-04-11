def vigenere_encrypt(text, key):
    text = text.upper()
    key = key.upper()
    result = ""
    key_index = 0
    
    for char in text:
        if char.isalpha():
            # Get the shift value from the key
            shift = ord(key[key_index % len(key)]) - ord('A')
            # Apply the shift
            char_pos = ord(char) - ord('A')
            new_pos = (char_pos + shift) % 26
            result += chr(new_pos + ord('A'))
            key_index += 1
        else:
            result += char
    
    return result

def vigenere_decrypt(text, key):
    text = text.upper()
    key = key.upper()
    result = ""
    key_index = 0
    
    for char in text:
        if char.isalpha():
            # Get the shift value from the key
            shift = ord(key[key_index % len(key)]) - ord('A')
            # Apply the reverse shift
            char_pos = ord(char) - ord('A')
            new_pos = (char_pos - shift) % 26
            result += chr(new_pos + ord('A'))
            key_index += 1
        else:
            result += char
    
    return result

def double_vigenere_encrypt(text, key1, key2):
    # First encryption with key1
    first_encryption = vigenere_encrypt(text, key1)
    # Second encryption with key2
    return vigenere_encrypt(first_encryption, key2)

def double_vigenere_decrypt(text, key1, key2):
    # First decryption with key2
    first_decryption = vigenere_decrypt(text, key2)
    # Second decryption with key1
    return vigenere_decrypt(first_decryption, key1)

def main():
    while True:
        print("\nVigenère Cipher Menu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Double Encrypt")
        print("4. Double Decrypt")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            break
            
        text = input("Enter the text: ")
        
        if choice in ['1', '2']:
            key = input("Enter the key: ")
            if choice == '1':
                result = vigenere_encrypt(text, key)
                print(f"Encrypted text: {result}")
            else:
                result = vigenere_decrypt(text, key)
                print(f"Decrypted text: {result}")
        
        elif choice in ['3', '4']:
            key1 = input("Enter the first key: ")
            key2 = input("Enter the second key: ")
            if choice == '3':
                result = double_vigenere_encrypt(text, key1, key2)
                print(f"Double encrypted text: {result}")
            else:
                result = double_vigenere_decrypt(text, key1, key2)
                print(f"Double decrypted text: {result}")

if __name__ == "__main__":
    main()

# Example usage from the assignment:
print("\nAssignment Example:")
plaintext = "SECURE SYSTEMS"
key1 = "MATRIXCODE"
key2 = "SECURITY"

# Double encryption
encrypted = double_vigenere_encrypt(plaintext, key1, key2)
# Double decryption
decrypted = double_vigenere_decrypt(encrypted, key1, key2)

print(f"Original text: {plaintext}")
print(f"First key: {key1}")
print(f"Second key: {key2}")
print(f"Double encrypted text: {encrypted}")
print(f"Double decrypted text: {decrypted}") 