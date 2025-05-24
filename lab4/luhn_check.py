class LuhnCheck:
    @staticmethod
    def luhn_check(number: str) -> bool:
        reversed_number = number[::-1]
        s = 0
        for i in range(len(reversed_number)):
            if i % 2 == 1:
                sum = 2 * int(reversed_number[i])
                if sum < 10:
                    s += sum
                else:
                    sum = int(str(sum)[0]) + int(str(sum)[1])
                    s += sum
            else:
                s += int(reversed_number[i])

        return s % 10 == 0