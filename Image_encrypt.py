from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def encrypt_image(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        image_data = file.read()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(image_data) + padder.finalize()

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    with open(output_file, 'wb') as file:
        file.write(iv + encrypted_data)

def decrypt_image(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()

    iv = encrypted_data[:16]
    encrypted_data = encrypted_data[16:]

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

    with open(output_file, 'wb') as file:
        file.write(unpadded_data)

# File paths
input_image_1st = r'/1st_image.jpeg'
input_image_2nd = r'/2nd_image.jpeg'
output_image_encrypted = r'/encrypted_image.jpg'
output_image_decrypted = r'/decrypted_image.jpg'

# Generate a random 256-bit (32 bytes) key
key = os.urandom(32)

# Encrypt the 1st image
encrypt_image(input_image_1st, output_image_encrypted, key)

# Decrypt the encrypted image
decrypt_image(output_image_encrypted, output_image_decrypted, key)
