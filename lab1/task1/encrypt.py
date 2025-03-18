def encrypt(data: str, key: dict[str, str]) -> str:

    """
    Encrypts text using a key
    :param data: text to encrypt
    :param key: encryption key
    :return: encrypted text
    """

    result = ""

    for value in data.upper():
        result += key[value]

    return result