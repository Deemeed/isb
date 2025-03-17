def encrypt(data: str, key: dict[str, str]) -> str:
    result = ""

    for value in data.upper():
        result += key[value]

    return result