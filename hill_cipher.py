import numpy as np
from numpy.linalg import inv, det

def matrix_mod_inverse(matrix, modulus):
    """Calculate the modular multiplicative inverse of a matrix"""
    det_val = int(round(det(matrix))) % modulus
    det_inverse = pow(det_val, -1, modulus)
    adjugate = np.round(det_val * inv(matrix)).astype(int) % modulus
    return (det_inverse * adjugate) % modulus

def prepare_text(text, block_size):
    """Prepare text for Hill cipher encryption"""
    # Remove non-alphabetic characters and convert to uppercase
    text = ''.join(c.upper() for c in text if c.isalpha())
    
    # Pad with 'X' if necessary
    padding_length = block_size - (len(text) % block_size) if len(text) % block_size != 0 else 0
    text += 'X' * padding_length
    
    # Convert text to numbers (A=0, B=1, etc.)
    numbers = [ord(c) - ord('A') for c in text]
    
    # Split into blocks
    blocks = [numbers[i:i + block_size] for i in range(0, len(numbers), block_size)]
    return blocks

def hill_encrypt(text, key_matrix):
    """Encrypt text using Hill cipher"""
    block_size = len(key_matrix)
    blocks = prepare_text(text, block_size)
    
    # Convert blocks to column vectors and multiply with key matrix
    result = ""
    for block in blocks:
        vector = np.array(block).reshape(block_size, 1)
        encrypted_vector = np.dot(key_matrix, vector) % 26
        # Convert numbers back to letters
        result += ''.join(chr(int(x) + ord('A')) for x in encrypted_vector.flatten())
    
    return result

def hill_decrypt(text, key_matrix):
    """Decrypt text using Hill cipher"""
    try:
        # Calculate inverse key matrix
        inverse_key = matrix_mod_inverse(key_matrix, 26)
        return hill_encrypt(text, inverse_key)
    except:
        return "Error: Key matrix is not invertible modulo 26"

def is_valid_key_matrix(matrix):
    """Check if the key matrix is valid for Hill cipher"""
    try:
        # Matrix must be square
        if matrix.shape[0] != matrix.shape[1]:
            return False
        
        # Determinant must be non-zero and coprime with 26
        determinant = int(round(det(matrix))) % 26
        if determinant == 0 or np.gcd(determinant, 26) != 1:
            return False
        
        return True
    except:
        return False

def main():
    while True:
        print("\nHill Cipher Menu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '3':
            break
        
        # Get matrix size
        n = int(input("Enter matrix size (2 or 3): "))
        if n not in [2, 3]:
            print("Invalid matrix size. Please use 2 or 3.")
            continue
        
        # Get key matrix
        print(f"Enter {n}x{n} key matrix elements (space-separated rows):")
        key_matrix = []
        for i in range(n):
            row = list(map(int, input().split()))
            if len(row) != n:
                print(f"Each row must have exactly {n} elements")
                continue
            key_matrix.append(row)
        
        key_matrix = np.array(key_matrix)
        
        if not is_valid_key_matrix(key_matrix):
            print("Invalid key matrix. Matrix must be invertible modulo 26.")
            continue
        
        text = input("Enter the text: ")
        
        if choice == '1':
            result = hill_encrypt(text, key_matrix)
            print(f"Encrypted text: {result}")
        elif choice == '2':
            result = hill_decrypt(text, key_matrix)
            print(f"Decrypted text: {result}")

if __name__ == "__main__":
    main()

# Example usage from the assignment:
print("\nAssignment Example:")
# Example key matrix (2x2)
key_matrix = np.array([[2, 3], [1, 4]])
message = "ATTACK"

print("Key Matrix:")
print(key_matrix)
print(f"\nOriginal message: {message}")

encrypted = hill_encrypt(message, key_matrix)
print(f"Encrypted text: {encrypted}")

decrypted = hill_decrypt(encrypted, key_matrix)
print(f"Decrypted text: {decrypted}") 