import hashlib
from itertools import product
import multiprocessing as mp
import time
from matplotlib import pyplot as plt
import numpy as np


class CardNumberWork:
    @staticmethod
    def get_cores() -> int:
        cores = mp.cpu_count()

        return cores

    @staticmethod
    def generate_numbers(bins: list[str], last_four: str) -> list[str]:
        new_numbers = []
        for part_of_new_number in product("0123456789", repeat=6):
            for bin in bins:
                new_numbers.append(bin + ''.join(part_of_new_number) + last_four)

        return new_numbers

    @staticmethod
    def is_same_number(options: list[str]) -> str | bool:
        hashed = hashlib.sha1(options[1].encode()).hexdigest()

        return options[1] if options[0] == hashed else False

    @staticmethod
    def search_number(hash: str, last_four: str, bins: tuple[str, str], cores: int) -> str:
        number = ""
        with mp.Pool(processes=cores) as p:
            options = [[hash, new_number] for new_number in CardNumberWork.generate_numbers(bins, last_four)]
            for result in p.map(CardNumberWork.is_same_number, options):
                if result:
                    number = result
                    p.terminate()
                    break

        return number

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

    @staticmethod
    def measure_time(hash: str, last_four: str, bins: list[str], max_cores: int):
        import gc
        times = []
        x = range(1, int(1.5 * max_cores))

        for cores in x:
            gc.collect()
            start_time = time.time()
            result = CardNumberWork.search_number(hash, last_four, bins, cores)
            end_time = time.time()
            total_time = end_time - start_time
            times.append(total_time)

        y = times
        plt.figure(figsize=(30, 5))
        plt.plot(x, y, 'bo-', label='Search time')

        min_time = min(times)
        min_index = times.index(min_time)
        min_processes = x[min_index]
        plt.plot(min_processes, min_time, 'ro', label=f'Minimum ({min_processes} processes)')

        plt.title('Time by processes')
        plt.xlabel('Processes')
        plt.ylabel('Time, seconds')
        plt.xticks(x)
        plt.grid(True)
        plt.legend()

        plt.savefig('time_by_processes.png')
        plt.show()

        return times