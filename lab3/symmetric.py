import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class Symmetric:
    @staticmethod
    def generate_symmetric_key(key_len: int) -> bytes:
        key = os.urandom(key_len // 8)

        return key

    @staticmethod
    def padding_text(text: str) -> bytes:
        padder = padding.ANSIX923(16).padder()
        b_text = bytes(text, 'UTF-8')
        padded_text = padder.update(b_text) + padder.finalize()

        return padded_text

    @staticmethod
    def encrypt_text(text: str, key: bytes) -> bytes:
        padded_text = Symmetric.padding_text(text)

        iv = os.urandom(16)
        cipher = Cipher(algorithms.Camellia(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        c_text = encryptor.update(padded_text) + encryptor.finalize()

        return c_text

    @staticmethod
    def decrypt_text(c_text: bytes, key: bytes) -> str:
        iv = os.urandom(16)
        cipher = Cipher(algorithms.Camellia(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        dc_text = decryptor.update(c_text) + decryptor.finalize()

        return Symmetric.unpadding_text(dc_text)

    @staticmethod
    def unpadding_text(dc_text: bytes) -> str:
        unpadder = padding.ANSIX923(16).unpadder()
        unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()

        return unpadded_dc_text