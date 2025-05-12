from symmetric import Symmetric
from asymmetric import Asymmetric
from filework import (readfile, writefile, serialization_public, serialization_private, deserialization_public, deserialization_private)


class CryptoSistem:
    def __init__(self, key_len):
        self._key_len = key_len

    def generate_hybrid_keys(self, path_c_symmetric_key: str, path_public_key: str, path_private_key: str) -> None:

        """
        Runs 1st scenario: generate keys
        :param path_c_symmetric_key: path to symmetric key
        :param path_public_key: path to public key
        :param path_private_key: path to private key
        :return: None
        """

        symmetric_key = Symmetric.generate_symmetric_key(self._key_len)

        private_key, public_key = Asymmetric.generate_asymmetric_keys()

        serialization_public(path_public_key, public_key)
        serialization_private(path_private_key, private_key)

        c_symmetric_key = Asymmetric.encrypt_symmetric_key(public_key, symmetric_key)
        writefile(path_c_symmetric_key, c_symmetric_key, 'wb')

    def encrypt_data(self, path_plain_text: str, path_private_key: str, path_c_symmetric_key: str, path_encrypted_text: str) -> None:

        """
        Runs 2nd scenario: encrypt text
        :param path_plain_text: path to plain text
        :param path_private_key: path to private key
        :param path_c_symmetric_key: path to symmetric key
        :param path_encrypted_text: path to encrypted text
        :return: None
        """

        private_key = deserialization_private(path_private_key)
        c_symmetric_key = readfile(path_c_symmetric_key, 'rb')
        symmetric_key = Asymmetric.decrypt_symmetric_key(private_key, c_symmetric_key)

        plain_text = readfile(path_plain_text, 'rb')

        encrypted_text = Symmetric.encrypt_text(plain_text, symmetric_key)
        writefile(path_encrypted_text, encrypted_text, 'wb')

    def decrypt_data(self, path_encrypted_text: str, path_private_key: str, path_c_symmetric_key: str, path_decrypted_text: str) -> None:

        """
        Runs 3d scenario: decrypt text
        :param path_encrypted_text: path to encrypted text
        :param path_private_key: path to private key
        :param path_c_symmetric_key: path to symmetric key
        :param path_decrypted_text: path to decrypted text
        :return: None
        """

        private_key = deserialization_private(path_private_key)
        c_symmetric_key = readfile(path_c_symmetric_key, 'rb')
        symmetric_key = Asymmetric.decrypt_symmetric_key(private_key, c_symmetric_key)

        encrypted_text = readfile(path_encrypted_text, 'rb')
        if not isinstance(encrypted_text, bytes):
            raise ValueError("Invalid encrypted data format")

        decrypted_text = Symmetric.decrypt_text(encrypted_text, symmetric_key)
        writefile(path_decrypted_text, decrypted_text, 'w')