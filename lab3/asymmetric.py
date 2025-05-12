from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa

class Asymmetric:
    @staticmethod
    def generate_asymmetric_keys() -> tuple:
        keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        private_key = keys
        public_key = keys.public_key()

        return private_key, public_key

    @staticmethod
    def encrypt_symmetric_key(public_key: rsa.RSAPublicKey, symmetric_key: bytes) -> bytes:
        key = bytes(symmetric_key, 'UTF-8')
        c_key = public_key.encrypt(key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

        return c_key

    @staticmethod
    def decrypt_symmetric_key(private_key: rsa.RSAPrivateKey, c_key: bytes) -> bytes:
        dc_key = private_key.decrypt(c_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

        return dc_key