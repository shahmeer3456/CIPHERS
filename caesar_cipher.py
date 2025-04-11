def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - ascii_offset + shift) % 26
            result += chr(shifted + ascii_offset)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def double_caesar_encrypt(text, shift1, shift2):
    # First encryption
    first_encryption = caesar_encrypt(text, shift1)
    # Second encryption
    return caesar_encrypt(first_encryption, shift2)

def double_caesar_decrypt(text, shift1, shift2):
    # First decryption (reverse of second encryption)
    first_decryption = caesar_decrypt(text, shift2)
    # Second decryption (reverse of first encryption)
    return caesar_decrypt(first_decryption, shift1)

def main():
    while True:
        print("\nCaesar Cipher Menu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Double Shift Encrypt")
        print("4. Double Shift Decrypt")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            break
            
        text = input("Enter the text: ")
        
        if choice in ['1', '2']:
            shift = int(input("Enter the shift value: "))
            if choice == '1':
                result = caesar_encrypt(text, shift)
                print(f"Encrypted text: {result}")
            else:
                result = caesar_decrypt(text, shift)
                print(f"Decrypted text: {result}")
                
        elif choice in ['3', '4']:
            shift1 = int(input("Enter first shift value: "))
            shift2 = int(input("Enter second shift value: "))
            if choice == '3':
                result = double_caesar_encrypt(text, shift1, shift2)
                print(f"Double encrypted text: {result}")
            else:
                result = double_caesar_decrypt(text, shift1, shift2)
                print(f"Double decrypted text: {result}")

if __name__ == "__main__":
    main()

# Example usage from the assignment:
print("\nAssignment Examples:")
# Part a
plaintext = "CRYPTOGRAPHY"
shift1, shift2 = 7, 5
encrypted = double_caesar_encrypt(plaintext, shift1, shift2)
decrypted = double_caesar_decrypt(encrypted, shift1, shift2)
print(f"\nPart a:")
print(f"Original text: {plaintext}")
print(f"Encrypted text: {encrypted}")
print(f"Decrypted text: {decrypted}")

# Part b
name = "SHAHMEER"  # Replace with your actual name
shift1, shift2 = 8, 4
encrypted = double_caesar_encrypt(name, shift1, shift2)
decrypted = double_caesar_decrypt(encrypted, shift1, shift2)
print(f"\nPart b:")
print(f"Original name: {name}")
print(f"Encrypted name: {encrypted}")
print(f"Decrypted name: {decrypted}") 