def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            # Convert to uppercase and get position (0-25)
            char = char.upper()
            pos = ord(char) - ord('A')
            # Apply affine transformation
            new_pos = (a * pos + b) % 26
            # Convert back to character
            result += chr(new_pos + ord('A'))
        else:
            result += char
    return result

def affine_decrypt(text, a, b):
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return "Error: 'a' value is not coprime with 26"
    
    result = ""
    for char in text:
        if char.isalpha():
            # Convert to uppercase and get position (0-25)
            char = char.upper()
            pos = ord(char) - ord('A')
            # Apply inverse affine transformation
            new_pos = (a_inv * (pos - b)) % 26
            # Convert back to character
            result += chr(new_pos + ord('A'))
        else:
            result += char
    return result

def main():
    while True:
        print("\nAffine Cipher Menu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '3':
            break
            
        text = input("Enter the text: ")
        a = int(input("Enter the value of 'a' (must be coprime with 26): "))
        b = int(input("Enter the value of 'b': "))
        
        if gcd(a, 26) != 1:
            print("Error: 'a' must be coprime with 26")
            continue
            
        if choice == '1':
            result = affine_encrypt(text, a, b)
            print(f"Encrypted text: {result}")
        elif choice == '2':
            result = affine_decrypt(text, a, b)
            print(f"Decrypted text: {result}")

if __name__ == "__main__":
    main()

# Example usage from the assignment:
print("\nAssignment Examples:")
# Part a
message1 = "ENCRYPTION"
a1, b1 = 11, 7
encrypted1 = affine_encrypt(message1, a1, b1)
decrypted1 = affine_decrypt(encrypted1, a1, b1)
print(f"\nPart a:")
print(f"Original text: {message1}")
print(f"Encrypted text: {encrypted1}")
print(f"Decrypted text: {decrypted1}")

# Part b
message2 = "EXTENDED"
a2, b2 = 15, 9
encrypted2 = affine_encrypt(message2, a2, b2)
decrypted2 = affine_decrypt(encrypted2, a2, b2)
print(f"\nPart b:")
print(f"Original text: {message2}")
print(f"Encrypted text: {encrypted2}")
print(f"Decrypted text: {decrypted2}") 