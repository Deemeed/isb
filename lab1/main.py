from filework import readfile, writefile, readjson, writejson
from task1.encrypt import encrypt_vigenere
from task2.decrypt import get_frequency, get_key, decrypt


def main():
    try:
        task1 = readjson("settings.json").get("task1")
        task2 = readjson("settings.json").get("task2")

        data = readfile(task1["plaintext"])
        key = readjson(task1["key"]).get("key")
        alphabet = readjson(task1["key"]).get("alphabet")
        ciphertext = encrypt_vigenere(data, key, alphabet)
        writefile(task1["ciphertext"], ciphertext)

        #data = readfile(task2["ciphertext"])
        #writejson(task2["frequency"], get_frequency(data))
        #key = get_key(get_frequency(data), readjson(task2["russian_frequency"]))
        #writejson(task2["key"], key)
        #key = readjson(task2["key"])
        #writefile(task2["plaintext"], decrypt(data, key))
    except Exception as exc:
        print(f'Something went wrong: {exc}')


if __name__ == "__main__":
    main()