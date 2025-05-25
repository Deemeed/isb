from lab4.filework import writefile
from lab4.card_number_work import CardNumberWork


class Application:
    @staticmethod
    def search_card_number(hash: str, last_four: str, bins: list[str], path_to_number: str) -> None:
        cores = CardNumberWork.get_cores()
        number = CardNumberWork.search_number(hash, last_four, bins, cores)
        writefile(path_to_number, number)

    @staticmethod
    def check_for_correctness(number: str) -> bool:
        return "Number is correct!" if CardNumberWork.luhn_check(number) else "Number is incorrect!"

    @staticmethod
    def measure_search_time(hash: str, last_four: str, bins: list[str]):
        cores = 14
        CardNumberWork.measure_time(hash, last_four, bins, cores)