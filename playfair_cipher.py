def create_matrix(key):
    # Create the Playfair matrix using the keyword
    key = key.upper().replace('J', 'I')  # Replace J with I
    matrix = []
    matrix_chars = []
    
    # Add the key characters first
    for char in key:
        if char.isalpha() and char not in matrix_chars:
            matrix_chars.append(char)
    
    # Add the remaining alphabet
    for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':  # Note: I and J share a position
        if char not in matrix_chars:
            matrix_chars.append(char)
    
    # Create 5x5 matrix
    for i in range(0, 25, 5):
        matrix.append(matrix_chars[i:i+5])
    
    return matrix

def find_position(matrix, char):
    char = char.upper()
    if char == 'J':
        char = 'I'
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None

def prepare_text(text):
    # Remove non-alphabetic characters and convert to uppercase
    text = ''.join(c.upper() for c in text if c.isalpha())
    text = text.replace('J', 'I')
    
    # Split into digraphs and handle repeated letters
    digraphs = []
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            digraphs.append(text[i] + 'X')
            break
        if text[i] == text[i + 1]:
            digraphs.append(text[i] + 'X')
            i += 1
        else:
            digraphs.append(text[i] + text[i + 1])
            i += 2
            
    return digraphs

def playfair_encrypt(text, key):
    matrix = create_matrix(key)
    digraphs = prepare_text(text)
    result = ""
    
    for digraph in digraphs:
        row1, col1 = find_position(matrix, digraph[0])
        row2, col2 = find_position(matrix, digraph[1])
        
        if row1 == row2:  # Same row
            result += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            result += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:  # Rectangle
            result += matrix[row1][col2] + matrix[row2][col1]
    
    return result

def playfair_decrypt(text, key):
    matrix = create_matrix(key)
    # Split text into digraphs
    digraphs = [text[i:i+2] for i in range(0, len(text), 2)]
    result = ""
    
    for digraph in digraphs:
        row1, col1 = find_position(matrix, digraph[0])
        row2, col2 = find_position(matrix, digraph[1])
        
        if row1 == row2:  # Same row
            result += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            result += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:  # Rectangle
            result += matrix[row1][col2] + matrix[row2][col1]
    
    return result

def print_matrix(matrix):
    print("\nPlayfair Matrix:")
    for row in matrix:
        print(' '.join(row))
    print()

def main():
    while True:
        print("\nPlayfair Cipher Menu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. View Matrix")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '4':
            break
            
        key = input("Enter the keyword: ")
        matrix = create_matrix(key)
        
        if choice == '3':
            print_matrix(matrix)
            continue
            
        text = input("Enter the text: ")
        
        if choice == '1':
            result = playfair_encrypt(text, key)
            print(f"Encrypted text: {result}")
        elif choice == '2':
            result = playfair_decrypt(text, key)
            print(f"Decrypted text: {result}")

if __name__ == "__main__":
    main()

# Example usage from the assignment:
print("\nAssignment Examples:")

# Part a
message = "HIDE THE TREASURE"
key = "KEYBOARD"
print("\nPart a:")
print(f"Original message: {message}")
print(f"Key: {key}")
encrypted = playfair_encrypt(message, key)
decrypted = playfair_decrypt(encrypted, key)
print(f"Encrypted text: {encrypted}")
print(f"Decrypted text: {decrypted}")

# Part b
ciphertext = "GATLMZCLRQXA"
key = "SECRET"
print("\nPart b:")
print(f"Ciphertext: {ciphertext}")
print(f"Key: {key}")
decrypted = playfair_decrypt(ciphertext, key)
print(f"Decrypted text: {decrypted}")

# Display the matrix for the keyword "KEYBOARD"
print("\nMatrix for keyword 'KEYBOARD':")
print_matrix(create_matrix("KEYBOARD")) 