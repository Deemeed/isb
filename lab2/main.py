from filework import readfile, readjson, writejson
from task2.NIST_tests import frequency_bit_test, identical_consecutive_bit_test, longest_sequence_of_ones_test


def tests() -> None:

    """
    Running all tests with each sequence, saving results to json
    :return: None
    """

    files = readjson("settings.json")

    data = readjson(files["results"])
    cpp_sequence = readfile(files["cpp_sequence"])
    java_sequence = readfile(files["java_sequence"])

    data["cpp_sequence"]["frequency_bit_test"] = frequency_bit_test(cpp_sequence)
    data["cpp_sequence"]["identical_consecutive_bit_test"] = identical_consecutive_bit_test(cpp_sequence)
    data["cpp_sequence"]["longest_sequence_of_ones_test"] = longest_sequence_of_ones_test(cpp_sequence)

    data["java_sequence"]["frequency_bit_test"] = frequency_bit_test(java_sequence)
    data["java_sequence"]["identical_consecutive_bit_test"] = identical_consecutive_bit_test(java_sequence)
    data["java_sequence"]["longest_sequence_of_ones_test"] = longest_sequence_of_ones_test(java_sequence)

    writejson(files["results"], data)


def main():
    try:
        tests()
    except Exception as exc:
        print(f'Something went wrong: {exc}')


if __name__ == "__main__":
    main()