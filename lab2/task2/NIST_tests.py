from math import erfc, sqrt


def frequency_bit_test(sequence: str) -> float:
    s = 0
    for i in sequence:
        if i == "1":
            s += 1
        else:
            s -= 1
    s = abs(s) / sqrt(len(sequence))
    p_value = erfc(s / sqrt(2))

    return p_value


def identical_consecutive_bit_test(sequence: str) -> float:
    pass


def longest_sequence_of_ones_test(sequence: str) -> float:
    pass