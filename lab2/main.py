from filework import readfile, writefile, readjson, writejson
from task2.NIST_tests import frequency_bit_test, identical_consecutive_bit_test, longest_sequence_of_ones_test


def tests(sequence: str, java_sequence: str) -> None:
    pass


def main():
    try:
        files = readjson("settings.json")
        cpp_sequence = readfile(files["cpp_sequence"])
        java_sequence = readfile(files["java_sequence"])
        tests(cpp_sequence, java_sequence)
    except Exception as exc:
        print(f'Something went wrong: {exc}')


if __name__ == "__main__":
    main()