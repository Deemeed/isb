import pyinputplus as pyip

from lab4.app.application import Application
from lab4.app.filework import readfile


def main():
    settings = readfile("settings.json")

    while True:
        print("\n=== Главное меню ===")
        choice = pyip.inputMenu(
            ['Подобрать номер карты',
             'Проверить корректность номера',
             'Замерить время поиска',
             'Изменить настройки (загрузить из файла)',
             'Выход'],
            numbered=True
        )

        if choice == 'Подобрать номер карты':
            print("\nНачался подбор номера карты...")
            Application.search_card_number(
                settings["hash"],
                settings["last_four"],
                settings["BINS"],
                settings["card_number"]
            )
            result = readfile(settings["card_number"])
            print(f"Результат: {result if result else 'Не найдено'}")

        elif choice == 'Проверить корректность номера':
            card_number = readfile(settings["card_number"])
            if not card_number:
                print("Ошибка: номер карты еще не найден")
                continue
            print(f"\nПроверка номера: {card_number}")
            result = Application.check_for_correctness(card_number)
            print(f"Результат: {result}")

        elif choice == 'Замерить время поиска':
            print("\nНачался замер времени поиска...")
            Application.measure_search_time(
                settings["hash"],
                settings["last_four"],
                settings["BINS"],
                settings["cores"],
                settings["time_by_processes_results"]
            )
            print(f"График сохранен в {settings['time_by_processes_results']}")

        elif choice == 'Изменить настройки (загрузить из файла)':
            try:
                config_file = pyip.inputFilepath("Введите путь к файлу настроек: ", mustExist=True)
                new_settings = readfile(config_file)
                settings.update(new_settings)
                print("Настройки обновлены")
            except Exception as e:
                print(f"Ошибка: {str(e)}")

        elif choice == 'Выход':
            print("Завершение работы")
            break


if __name__ == "__main__":
    main()