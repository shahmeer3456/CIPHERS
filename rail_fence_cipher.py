def create_rail_matrix(text, depth):
    """Create the rail fence pattern matrix"""
    rail = [['\n' for i in range(len(text))] for j in range(depth)]
    
    # Variables to track current direction and position
    dir_down = False
    row, col = 0, 0
    
    # Fill the rail matrix with characters
    for i in range(len(text)):
        # Check if we need to change direction
        if (row == 0) or (row == depth - 1):
            dir_down = not dir_down
        
        # Fill the current position
        rail[row][col] = text[i]
        col += 1
        
        # Update row based on direction
        if dir_down:
            row += 1
        else:
            row -= 1
            
    return rail

def rail_fence_encrypt(text, depth):
    """Encrypt text using Rail Fence cipher"""
    # Remove spaces and convert to uppercase
    text = ''.join(text.upper().split())
    
    # Create the rail pattern
    rail = create_rail_matrix(text, depth)
    
    # Read off the pattern
    result = ""
    for i in range(depth):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result += rail[i][j]
    
    return result

def rail_fence_decrypt(text, depth):
    """Decrypt text using Rail Fence cipher"""
    # Create the rail pattern
    rail = [['\n' for i in range(len(text))] for j in range(depth)]
    
    # Mark the positions in rail matrix
    dir_down = None
    row, col = 0, 0
    
    # Mark the positions where characters will be placed
    for i in range(len(text)):
        if row == 0:
            dir_down = True
        if row == depth - 1:
            dir_down = False
            
        rail[row][col] = '*'
        col += 1
        
        if dir_down:
            row += 1
        else:
            row -= 1
            
    # Fill the rail matrix with encrypted text
    index = 0
    for i in range(depth):
        for j in range(len(text)):
            if rail[i][j] == '*' and index < len(text):
                rail[i][j] = text[index]
                index += 1
    
    # Read off the decrypted text
    result = ""
    row, col = 0, 0
    dir_down = None
    
    for i in range(len(text)):
        if row == 0:
            dir_down = True
        if row == depth - 1:
            dir_down = False
            
        if rail[row][col] != '*':
            result += rail[row][col]
        col += 1
        
        if dir_down:
            row += 1
        else:
            row -= 1
            
    return result

def alternating_depth_encrypt(text, depths):
    """Encrypt text using alternating depths"""
    result = text
    for depth in depths:
        result = rail_fence_encrypt(result, depth)
    return result

def alternating_depth_decrypt(text, depths):
    """Decrypt text using alternating depths"""
    result = text
    for depth in reversed(depths):
        result = rail_fence_decrypt(result, depth)
    return result

def main():
    while True:
        print("\nRail Fence Cipher Menu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Alternating Depth Encrypt")
        print("4. Alternating Depth Decrypt")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            break
            
        text = input("Enter the text: ")
        
        if choice in ['1', '2']:
            depth = int(input("Enter the depth: "))
            if choice == '1':
                result = rail_fence_encrypt(text, depth)
                print(f"Encrypted text: {result}")
            else:
                result = rail_fence_decrypt(text, depth)
                print(f"Decrypted text: {result}")
                
        elif choice in ['3', '4']:
            depths = list(map(int, input("Enter depths (space-separated): ").split()))
            if choice == '3':
                result = alternating_depth_encrypt(text, depths)
                print(f"Encrypted text with alternating depths: {result}")
            else:
                result = alternating_depth_decrypt(text, depths)
                print(f"Decrypted text with alternating depths: {result}")

if __name__ == "__main__":
    main()

# Example usage from the assignment:
print("\nAssignment Example:")
message = "INFORMATION SECURITY"
depths = [2, 4]  # Alternating depths

print(f"Original message: {message}")
print(f"Using alternating depths: {depths}")

# Encrypt using alternating depths
encrypted = alternating_depth_encrypt(message, depths)
print(f"Encrypted text: {encrypted}")

# Decrypt using alternating depths
decrypted = alternating_depth_decrypt(encrypted, depths)
print(f"Decrypted text: {decrypted}")

# Example with single rail (Part a answer)
print("\nSingle Rail Example:")
single_rail = rail_fence_encrypt("TEST MESSAGE", 1)
print(f"Single rail encryption: {single_rail}")
print("Note: With a single rail, the message remains unchanged as it's just read in a straight line.") 