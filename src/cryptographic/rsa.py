from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

class RSACipher:
    def __init__(self, key_size=2048):
        self.key_size = key_size
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=self.key_size,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()

    def encrypt(self, message):
        """
        Encrypt a message using the RSA public key.

        Args:
            message (str): The message to encrypt.

        Returns:
            bytes: The encrypted message.
        """
        encrypted_message = self.public_key.encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted_message

    def decrypt(self, encrypted_message):
        """
        Decrypt a message using the RSA private key.

        Args:
            encrypted_message (bytes): The message to decrypt.

        Returns:
            str: The decrypted message.
        """
        decrypted_message = self.private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_message.decode()

# Example usage
rsa_cipher = RSACipher()
message = "Hello, RSA!"

# Encrypt
encrypted_msg = rsa_cipher.encrypt(message)
print(f"Encrypted message: {encrypted_msg}")

# Decrypt
decrypted_msg = rsa_cipher.decrypt(encrypted_msg)
print(f"Decrypted message: {decrypted_msg}")
