def get_frequency(data: str) -> dict[str, float]:

    """
    Compiles a dict with frequencies of every char
    :param data: text to count
    :return: dict with frequencies
    """

    result = {key:0 for key in data}

    for key in data:
        result[key] += 1

    for key, value in result.items():
        result[key] = value / len(data)

    return dict(sorted(result.items(), key = lambda item:item[1], reverse=True))


def get_key(ciphertext_frequency: dict[str, float], russian_frequency: dict[str, float]) -> dict[str, str]:

    """
    Compiles a dict which is a key of decryption
    :param ciphertext_frequency: frequencies of ciphertext
    :param russian_frequency: frequencies of russian chars
    :return: a dict which is a key
    """

    result = dict()
    for cipher_kye, russian_key in zip(ciphertext_frequency.keys(), russian_frequency.keys()):
        result[cipher_kye] = russian_key

    return result


def decrypt(data: str, key: dict[str, str]) -> str:

    """
    Decrypts a text using key
    :param data: text to decrypt
    :param key: key of decryption
    :return: decrypted text
    """

    result = ""
    for value in data:
        result += key[value]

    return result