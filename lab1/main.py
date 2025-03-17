from filework import readfile, writefile, readjson, writejson
from task1.encrypt import encrypt


def main():
    data = readfile("task1/plaintext.txt")
    key = readjson("task1/key.json")
    ciphertext = encrypt(data, key)
    writefile("task1/ciphertext.txt", ciphertext)

if __name__ == "__main__":
    main()