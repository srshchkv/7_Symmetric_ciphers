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

# Test the Caesar cipher functions
plaintext = 'Hello, World!'
key = 3
encrypted_text = caesar_encrypt(key, plaintext)
decrypted_text = caesar_decrypt(key, encrypted_text)

print('Original Text:', plaintext)
print('Encrypted Text:', encrypted_text)
print('Decrypted Text:', decrypted_text)
