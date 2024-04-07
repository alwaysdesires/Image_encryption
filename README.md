# Image_encryption
🛡️ Image Encryption and Decryption with Python
This Python project provides a simple yet powerful solution for encrypting and decrypting image files using the Advanced Encryption Standard (AES) algorithm. With this tool, you can ensure the security of your visual data by protecting it from unauthorized access.

Features:
🔒 Easy-to-use: Simple Python script for encrypting and decrypting image files.
🔐 AES Encryption: Utilizes AES encryption for robust security.
📦 PKCS7 Padding: Applies PKCS7 padding for compatibility and security.
🖥️ Cross-platform: Works seamlessly on Windows, macOS, and Linux.

Usage:
Clone the repository to your local machine:
bash
Copy code
git clone https://github.com/yourusername/image-encryption.git
Navigate to the project directory:
arduino
Copy code
cd image-encryption
Update the file paths and image names in the image_encrypt_decrypt.py script:
Just change the name or directory of your image files to 1st_image and 2nd_image.
Run the script to encrypt and decrypt images:
Copy code
python image_encrypt_decrypt.py
Example:
python
Copy code
# File paths
input_image_1st = r'/path/to/your/1st_image.jpg'
input_image_2nd = r'/path/to/your/2nd_image.jpg'
output_image_encrypted = r'/output/directory/encrypted_image.jpg'
output_image_decrypted = r'/output/directory/decrypted_image.jpg'

# Generate a random 256-bit (32 bytes) key
key = os.urandom(32)

# Encrypt the first image
encrypt_image(input_image_1st, output_image_encrypted, key)

# Decrypt the encrypted image
decrypt_image(output_image_encrypted, output_image_decrypted, key)
Contribution:
Contributions are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

Enjoy secure image encryption with Python! 🖼️🔐

