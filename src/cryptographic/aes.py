from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

class AESCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        """
        Encrypt a plaintext string using AES.

        Args:
            plaintext (str): The plaintext to encrypt.

        Returns:
            bytes: The encrypted ciphertext.
        """
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plaintext.encode()) + padder.finalize()

        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()

        return iv + ciphertext

    def decrypt(self, ciphertext):
        """
        Decrypt a ciphertext string using AES.

        Args:
            ciphertext (bytes): The ciphertext to decrypt.

        Returns:
            str: The decrypted plaintext.
        """
        iv = ciphertext[:16]
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_padded = decryptor.update(ciphertext[16:]) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()
        decrypted_data = unpadder.update(decrypted_padded) + unpadder.finalize()

        return decrypted_data.decode()

# Example usage
import os

# Generate a random 256-bit key
key = os.urandom(32)

aes_cipher = AESCipher(key)

# Encrypt
plaintext = "Hello, AES!"
ciphertext = aes_cipher.encrypt(plaintext)
print(f"Ciphertext: {ciphertext}")

# Decrypt
decrypted_text = aes_cipher.decrypt(ciphertext)
print(f"Decrypted Text: {decrypted_text}")
