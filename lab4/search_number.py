import hashlib
import itertools
import multiprocessing as mp
from itertools import repeat


class SearchCardNumber:
    @staticmethod
    def get_cores() -> int:
        cores = mp.cpu_count()

        return cores

    @staticmethod
    def generate_numbers(bins: list[str], last_four: str) -> list[str]:
        new_numbers = []
        for part_of_new_number in itertools.product("0123456789", repeat=6):
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
            options = [[hash, new_number] for new_number in SearchCardNumber.generate_numbers(bins, last_four)]
            for result in p.map(SearchCardNumber.is_same_number, options):
                if result:
                    number = result
                    p.terminate()
                    break

        return number