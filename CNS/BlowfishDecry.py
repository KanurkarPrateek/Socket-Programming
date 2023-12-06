from Crypto.Cipher import Blowfish
from Crypto import Random

def encrypt(key, plaintext):
    iv = Random.new().read(Blowfish.block_size)
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    padded_plaintext = _pad_string(plaintext)
    ciphertext = cipher.encrypt(padded_plaintext)
    return iv + ciphertext

def decrypt(key, ciphertext):
    iv = ciphertext[:Blowfish.block_size]
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    padded_plaintext = cipher.decrypt(ciphertext[Blowfish.block_size:])
    plaintext = _unpad_string(padded_plaintext)
    return plaintext

def _pad_string(s):
    padding_size = Blowfish.block_size - len(s) % Blowfish.block_size
    padding = chr(padding_size) * padding_size
    return s + padding

def _unpad_string(s):
    padding_size = ord(s[-1])
    return s[:-padding_size]

key = b'secret_key'
plaintext = 'This is a secret message.'
encrypted_data = encrypt(key, plaintext)
print('Encrypted data:', encrypted_data.hex())
decrypted_data = decrypt(key, encrypted_data)
print('Decrypted data:', decrypted_data)