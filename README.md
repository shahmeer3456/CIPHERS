# Classical Cryptography Implementations

This repository contains Python implementations of various classical cryptographic ciphers as part of an Information Security assignment.

## Implemented Ciphers

1. Caesar Cipher (`caesar_cipher.py`)
   - Single and double shift encryption/decryption
   - Interactive menu interface

2. Affine Cipher (`affine_cipher.py`)
   - Encryption/decryption with modular arithmetic
   - Key validation for coprime requirements

3. Vigenère Cipher (`vigenere_cipher.py`)
   - Single and double keyword encryption/decryption
   - Supports spaces and case-insensitive input

4. Playfair Cipher (`playfair_cipher.py`)
   - 5x5 matrix generation with keyword
   - Handles duplicate letters with 'X' substitution
   - Matrix visualization

5. Hill Cipher (`hill_cipher.py`)
   - Matrix-based encryption/decryption
   - Key matrix validation
   - Requires numpy library

6. Rail Fence Cipher (`rail_fence_cipher.py`)
   - Variable depth encryption/decryption
   - Supports alternating depths
   - Visual matrix representation

7. Row Transposition Cipher (`row_transposition_cipher.py`)
   - Numerical key-based column transposition
   - Matrix visualization
   - Handles variable length inputs

## Setup

1. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Each cipher implementation can be run independently:

```bash
python ciphers/caesar_cipher.py
python ciphers/affine_cipher.py
python ciphers/vigenere_cipher.py
python ciphers/playfair_cipher.py
python ciphers/hill_cipher.py
python ciphers/rail_fence_cipher.py
python ciphers/row_transposition_cipher.py
```

Each program provides an interactive menu with options for:
- Encryption
- Decryption
- Additional features specific to each cipher
- Example usage from the assignment

## Notes

- All implementations handle uppercase alphabetic input
- Special characters and spaces are either removed or handled appropriately
- Each cipher includes example usage from the assignment questions
- The Hill Cipher requires numpy for matrix operations

## Assignment Requirements

- All code is written in Python as required
- Each implementation includes interactive menus
- Example cases from the assignment are included
- Code is well-documented and modular
- Error handling is implemented where necessary 
