from lab4.filework import writefile
from lab4.luhn_check import LuhnCheck
from lab4.search_number import SearchCardNumber


class Application:
    @staticmethod
    def search_card_number(hash: str, last_four: str, bins: list[str], path_to_number: str) -> None:
        cores = SearchCardNumber.get_cores()
        number = SearchCardNumber.search_number(hash, last_four, bins, cores)
        writefile(path_to_number, number)

    @staticmethod
    def check_for_correctness(number: str) -> bool:
        return LuhnCheck.luhn_check(number)

    def measure_search_time(self):
        pass