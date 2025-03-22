def encrypt_vigenere(data: str, key: str, alphabet: str) -> str:

    """
    Encrypts text using Vigenere cipher
    :param data: text to encrypt
    :param key: kye of encryption
    :param alphabet: alphabet
    :return: encrypted text
    """

    result = ""

    data = data.upper()
    for i in range(len(data)):
        if data[i] in alphabet:
            value = alphabet[(alphabet.index(data[i]) + alphabet.index(key[i % len(key)])) % len(alphabet)]
            result += value
        else:
            result += data[i]

    return result


def decrypt_vigenere(data: str, key: str, alphabet: str) -> str:

    """
    Decrypts text using Vigenere cipher
    :param data: text to decrypt
    :param key: key of encryption
    :param alphabet: alphabet
    :return: decrypted text
    """

    result = ""

    data = data.upper()
    for i in range(len(data)):
        if data[i] in alphabet:
            value = alphabet[(alphabet.index(data[i]) + len(alphabet) - alphabet.index(key[i % len(key)])) % len(alphabet)]
            result += value
        else:
            result += data[i]

    return result