from filework import readfile, writefile, readjson, writejson
from task1.encrypt import encrypt
from task2.decrypt import get_frequency, get_key, decrypt


def main():
    #data = readfile("task1/plaintext.txt")
    #key = readjson("task1/key.json")
    #ciphertext = encrypt(data, key)
    #writefile("task1/ciphertext.txt", ciphertext)

    data = readfile("task2/cod23.txt")
    #writejson("task2/frequency.json", get_frequency(data))
    #key = get_key(get_frequency(data), readjson("task2/russian_frequency.json"))
    #writejson("task2/key.json", key)
    key = readjson("task2/key.json")
    writefile("task2/plaintext.txt", decrypt(data, key))




if __name__ == "__main__":
    main()