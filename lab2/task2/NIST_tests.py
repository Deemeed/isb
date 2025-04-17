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
    n = len(sequence)
    z = sequence.count("1") / n

    if abs(z - 0.5) < (2 / sqrt(n)):
        v = 0
        for i in range(n - 1):
            if sequence[i] != sequence[i+1]:
                v += 1

        p_value = erfc(abs(v - 2 * n * z * (1 - z)) / (2 * sqrt(2 * n) * z * (1 - z)))
        return p_value
    else:
        p_value = 0
        return p_value


def longest_sequence_of_ones_test(sequence: str) -> float:
    pass