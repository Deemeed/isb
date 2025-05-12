import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def generate_symmetric_key() -> str:
    key = os.urandom(32)

    return key


def padding_text(text: str) -> str:
    padder = padding.ANSIX923(32).padder()
    text = bytes(text, 'UTF-8')
    padded_text = padder.update(text) + padder.finalize()

    return padded_text


def encrypt_text(text: str, key: str) -> str:
    padded_text = padding_text(text)

    iv = os.urandom(16)
    cipher = Cipher(algorithms.Camellia(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    c_text = encryptor.update(padded_text) + encryptor.finalize()

    return c_text


def decrypt_text(c_text: str, cipher=None) -> str:
    decryptor = cipher.decryptor()
    dc_text = decryptor.update(c_text) + decryptor.finalize()

    return unpadding_text(dc_text)


def unpadding_text(dc_text: str) -> str:
    unpadder = padding.ANSIX923(32).unpadder()
    unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()

    return unpadded_dc_text