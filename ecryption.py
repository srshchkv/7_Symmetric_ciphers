def encrypt(k, m):
    return ''.join(map(chr, [x + k for x in map(ord, m)]))

def decrypt(k, c):
    return ''.join(map(chr, [x - k for x in map(ord, c)]))

def caesar_encrypt(k, plaintext):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():  # Check if the character is an alphabet
            shifted = ord(char) + k
            if char.islower():  # Handle lowercase letters
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():  # Handle uppercase letters
                if shifted > ord('Z'):
                    shifted -= 26
            ciphertext += chr(shifted)
        else:
            ciphertext += char  # Keep non-alphabetic characters unchanged
    return ciphertext

def caesar_decrypt(k, ciphertext):
    return caesar_encrypt(-k, ciphertext)  # Decrypt by shifting in the opposite direction

def caesar_break(ciphertext):
    for key in range(26):  # Try all possible keys
        decrypted_text = caesar_decrypt(key, ciphertext)
        print(f'Key = {key}: {decrypted_text}')

if __name__ == "__main__":
    plaintext = 'Hello, World!'
    key = 3
    encrypted_text = caesar_encrypt(key, plaintext)
    decrypted_text = caesar_decrypt(key, encrypted_text)

    print('Original Text:', plaintext)
    print('Encrypted Text:', encrypted_text)
    print('Decrypted Text:', decrypted_text)
    # Test breaking the Caesar cipher without knowing the key
    encrypted_text_to_break = 'Khoor, Zruog!'
    caesar_break(encrypted_text_to_break)
