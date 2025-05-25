from lab4.app.card_number_work import CardNumberWork
from lab4.app.filework import writefile


class Application:
    @staticmethod
    def search_card_number(hash: str, last_four: str, bins: list[str], path_to_number: str) -> None:

        """
        Runs 1st scenario
        :param hash: hash
        :param last_four: last four digits
        :param bins: bins
        :param path_to_number: path to save found number
        :return: None
        """

        cores = CardNumberWork.get_cores()
        number = CardNumberWork.search_number(hash, last_four, bins, cores)
        writefile(path_to_number, number)

    @staticmethod
    def check_for_correctness(number: str) -> bool:

        """
        Runs 2nd scenario
        :param number: card number
        :return: is number correct
        """

        return "Number is correct!" if CardNumberWork.luhn_check(number) else "Number is incorrect!"

    @staticmethod
    def measure_search_time(hash: str, last_four: str, bins: list[str], cores: int, path_to_results: str) -> None:

        """
        Runs 3rd scenario
        :param hash: hash
        :param last_four: last four digits
        :param bins: bins
        :param cores: cores count
        :param path_to_results: path to save graph
        :return: None
        """

        CardNumberWork.measure_time(hash, last_four, bins, cores, path_to_results)