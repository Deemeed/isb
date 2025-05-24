from lab4.application import Application
from lab4.filework import readfile

def main():
    settings = readfile("settings.json")
    Application.search_card_number(settings["hash"], settings["last_four"], settings["BINS"], settings["card_number"])


if __name__ == "__main__":
    main()