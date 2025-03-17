def encrypt(data: str, key):
    result = ""

    for value in data.upper():
        result += key[value]

    return result