from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad
import os


# AES Utilities
def generate_aes_key():
    return os.urandom(16)  # 16 bytes = 128-bit key


def encrypt_aes(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)  # CBC mode
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return cipher.iv + ciphertext  # Prepend IV to ciphertext


def decrypt_aes(key, ciphertext):
    iv = ciphertext[:16]  # Extract IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[16:]), AES.block_size)
    return plaintext.decode()


# RSA Utilities
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key


def encrypt_rsa(public_key, data):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    return cipher.encrypt(data)


def decrypt_rsa(private_key, ciphertext):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    return cipher.decrypt(ciphertext)
