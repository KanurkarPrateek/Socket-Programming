from Crypto.Cipher import Blowfish
import os

# Generate a random 128-bit encryption key
key = os.urandom(16)

# Create a Blowfish cipher object with the encryption key
cipher = Blowfish.new(key, Blowfish.MODE_ECB)

# Encrypt the plaintext
plaintext = b"Hello, World!"
ciphertext = cipher.encrypt(plaintext)

# Decrypt the ciphertext
decrypted_text = cipher.decrypt(ciphertext)

# Print the results
print("Encryption Key:", key)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)