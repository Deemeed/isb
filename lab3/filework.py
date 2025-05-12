import json
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


def readfile(filename: str, mode: str) -> str | dict | bytes:

    """
    Reads data from file
    :param filename: directory
    :param mode: mode of reading
    :return: data
    """

    try:
        with open(filename, mode) as file:
            if filename.endswith(".json"):
                return json.load(file)
            else:
                return file.read()
    except json.JSONDecodeError as e:
        print(f"Decoding error JSON: {e}")
    except FileNotFoundError:
        print('File not found')
    except Exception as exc:
        print(f'Something went wrong: {exc}')


def writefile(filename: str, data: str | dict | bytes, mode: str) -> None:

    """
    Writes data to txt file
    :param filename: path to file
    :param data: data to write
    :param mode: mode of reading
    :return: none
    """

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            if filename.endswith(".json"):
                json.dump(data, file, ensure_ascii=False, indent=4)
            else:
                file.write(data)
    except json.JSONDecodeError as e:
        print(f"Decoding error JSON: {e}")
    except FileNotFoundError:
        print('File not found')
    except Exception as exc:
        print(f'Something went wrong: {exc}')


def serialization_public(public_pem: str, public_key: rsa.RSAPublicKey) -> None:

    """
    serializes public key
    :param public_pem: path to public key file
    :param public_key: key
    :return: None
    """

    try:
        with open(public_pem, 'wb') as public_out:
            public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo))
    except Exception as e:
        raise Exception(f"Error serialization public key: {e}")


def serialization_private(private_pem: str, private_key: rsa.RSAPrivateKey) -> None:

    """
    serializes private key
    :param private_pem: path to private key file
    :param private_key: key
    :return: None
    """

    try:
        with open(private_pem, 'wb') as private_out:
            private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                        encryption_algorithm=serialization.NoEncryption()))
    except Exception as e:
        raise Exception(f"Error serialization private key: {e}")


def deserialization_public(public_pem: str) -> rsa.RSAPublicKey:

    """
    deserializes public key
    :param public_pem: path to public key
    :return: public key
    """

    try:
        with open(public_pem, 'rb') as pem_in:
            public_bytes = pem_in.read()
        d_public_key = load_pem_public_key(public_bytes)
    except Exception as e:
        raise Exception(f"Error deserialization public key: {e}")

    return d_public_key


def deserialization_private(private_pem: str) -> rsa.RSAPrivateKey:

    """
    deserializes private key
    :param private_pem: path to private key
    :return: private key
    """

    try:
        with open(private_pem, 'rb') as pem_in:
            private_bytes = pem_in.read()
        d_private_key = load_pem_private_key(private_bytes, password=None, )
    except Exception as e:
        raise Exception(f"Error deserialization private key: {e}")

    return d_private_key