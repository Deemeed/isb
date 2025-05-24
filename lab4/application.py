from lab4.filework import writefile
from lab4.search_number import SearchCardNumber


class Application:
    @staticmethod
    def search_card_number(hash: str, last_four: str, bins: list[str], path_to_number: str) -> None:
        cores = SearchCardNumber.get_cores()
        number = SearchCardNumber.search_number(hash, last_four, bins, cores)
        writefile(path_to_number, number)

    def check_for_correctness(self):
        pass

    def measure_search_time(self):
        pass