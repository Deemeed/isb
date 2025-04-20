from math import erfc, sqrt
import scipy.special as sc


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
    v = [0, 0, 0, 0]
    p = [0.2148, 0.3672, 0.2305, 0.1875]

    for i in range(0, len(sequence), 8):
        ones_cnt = 0
        ones_max = -1
        for j in range(i, i + 8):
            if sequence[j] == "1":
                ones_cnt += 1
                ones_max = max(ones_cnt, ones_max)
            else:
                ones_cnt = 0

        match ones_max:
            case ones_max if ones_max <= 1:
                v[0] += 1
            case 2:
                v[1] += 1
            case 3:
                v[2] += 1
            case ones_max if ones_max >= 4:
                v[3] += 1

    hi_2 = 0
    for i in range(4):
        hi_2 += pow(v[i] - 16 * p[i], 2) / (16 * p[i])

    p_value = sc.gammainc((3 / 2), (hi_2 / 2))
    return p_value