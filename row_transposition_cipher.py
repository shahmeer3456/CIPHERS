def prepare_text(text):
    """Prepare text by removing spaces and converting to uppercase"""
    return ''.join(text.upper().split())

def create_matrix(text, key_length):
    """Create the matrix for row transposition"""
    # Calculate number of rows needed
    text_length = len(text)
    num_rows = (text_length + key_length - 1) // key_length
    
    # Pad text if necessary
    padding_length = num_rows * key_length - text_length
    if padding_length > 0:
        text += 'X' * padding_length
    
    # Create matrix
    matrix = []
    for i in range(0, len(text), key_length):
        matrix.append(list(text[i:i + key_length]))
    
    return matrix

def get_column_order(key):
    """Convert numerical key to column order"""
    # Create list of (value, position) pairs
    key_pairs = [(int(digit), i) for i, digit in enumerate(str(key))]
    # Sort by value and extract positions
    return [pos for _, pos in sorted(key_pairs)]

def row_transposition_encrypt(text, key):
    """Encrypt text using Row Transposition cipher"""
    text = prepare_text(text)
    key_length = len(str(key))
    
    # Create the matrix
    matrix = create_matrix(text, key_length)
    
    # Get the column order from the key
    column_order = get_column_order(key)
    
    # Read off columns in key order
    result = ""
    for col in column_order:
        for row in matrix:
            result += row[col]
    
    return result

def row_transposition_decrypt(text, key):
    """Decrypt text using Row Transposition cipher"""
    key_length = len(str(key))
    text_length = len(text)
    num_rows = (text_length + key_length - 1) // key_length
    
    # Create empty matrix
    matrix = [['' for _ in range(key_length)] for _ in range(num_rows)]
    
    # Get the column order from the key
    column_order = get_column_order(key)
    
    # Calculate positions in the matrix
    pos = 0
    for col in column_order:
        for row in range(num_rows):
            if pos < text_length:
                matrix[row][col] = text[pos]
                pos += 1
    
    # Read off the matrix row by row
    result = ""
    for row in matrix:
        result += ''.join(row)
    
    return result

def print_matrix(matrix):
    """Print the matrix in a readable format"""
    print("\nMatrix:")
    for row in matrix:
        print(' '.join(row))
    print()

def main():
    while True:
        print("\nRow Transposition Cipher Menu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. View Matrix")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '4':
            break
            
        text = input("Enter the text: ")
        key = input("Enter the numerical key (e.g., 315624): ")
        
        if choice == '1':
            result = row_transposition_encrypt(text, key)
            print(f"Encrypted text: {result}")
            if choice == '3':
                print_matrix(create_matrix(prepare_text(text), len(key)))
        elif choice == '2':
            result = row_transposition_decrypt(text, key)
            print(f"Decrypted text: {result}")
        elif choice == '3':
            print_matrix(create_matrix(prepare_text(text), len(key)))

if __name__ == "__main__":
    main()

# Example usage from the assignment:
print("\nAssignment Example:")
message = "CIPHER CHALLENGE"
key = "315624"

print(f"Original message: {message}")
print(f"Key: {key}")

# Show the matrix
matrix = create_matrix(prepare_text(message), len(key))
print_matrix(matrix)

# Encrypt and decrypt
encrypted = row_transposition_encrypt(message, key)
print(f"Encrypted text: {encrypted}")

decrypted = row_transposition_decrypt(encrypted, key)
print(f"Decrypted text: {decrypted}")

# Part a answer
print("\nPart a - Retrieving message with unknown key order:")
print("To retrieve a message when the key order is forgotten:")
print("1. The number of columns is known from the key length")
print("2. Try all possible permutations of the columns")
print("3. Look for readable text in the results")
print("4. The number of possible permutations is n! where n is the key length")
print("5. For a 6-digit key, there are 720 possible permutations to check") 