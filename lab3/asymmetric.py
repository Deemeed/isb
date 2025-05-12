from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa


def generate_asymmetric_keys(key_len: str) -> tuple[str, str]:
    keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    private_key = keys
    public_key = keys.public_key()

    return private_key, public_key


def encrypt_symmetric_key(public_key: str, simmetric_key: str, key_len: str):
    key = bytes(simmetric_key, 'UTF-8')
    c_key = public_key.encrypt(key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

    return c_key


def decrypt_symmetric_key(private_key: str, c_key: str):
    dc_key = private_key.decrypt(c_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

    return dc_key