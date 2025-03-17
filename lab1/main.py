from fileWork import readfile, writefile, readjson, writejson
from task1.task1 import encrypt


def main():
    data = readfile("task1/plaintext_task1.txt")
    key = readjson("task1/key1.json")
    ciphertext = encrypt(data, key)
    writefile("task1/ciphertext_task1.txt", ciphertext)

if __name__ == "__main__":
    main()