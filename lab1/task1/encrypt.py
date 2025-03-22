def encrypt_vigenere(data: str, key: str, alphabet: str) -> str:
    result = ""

    data = data.upper()
    for i in range(len(data)):
        if data[i] in alphabet:
            value = alphabet[(alphabet.index(data[i]) + alphabet.index(key[i % len(key)])) % len(alphabet)]
            result += value
        else:
            result += data[i]

    return result

def decrypt_vigenere(data, key, alphabet):
    result = ""

    data = data.upper()
    for i in range(len(data)):
        if data[i] in alphabet:
            value = alphabet[(alphabet.index(data[i]) + len(alphabet) - alphabet.index(key[i % len(key)])) % len(alphabet)]
            result += value
        else:
            result += data[i]

    return result