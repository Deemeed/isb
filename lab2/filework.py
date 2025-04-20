import json


def readfile(filename: str) -> str:

    """
    Reads data from txt file
    :param filename: path to file
    :return: data string
    """

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.read()
    except FileNotFoundError:
        print('File not found')
    except Exception as exc:
        print(f'Something went wrong: {exc}')

    return data


def writefile(filename: str, data: str) -> None:

    """
    Writes data to txt file
    :param filename: path to file
    :param data: data to write
    :return: none
    """

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(data)
    except FileNotFoundError:
        print('File not found')
    except Exception as exc:
        print(f'Something went wrong: {exc}')


def readjson(filename: str) -> dict[str, any]:

    """
    Reads data from json
    :param filename: path to file
    :return: data
    """

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Decoding error JSON: {e}")
    except FileNotFoundError:
        print('File not found')
    except Exception as exc:
        print(f'Something went wrong: {exc}')

    return data


def writejson(filename: str, data) -> None:

    """
    Writes data to json
    :param filename: path to file
    :param data: data to write
    :return: none
    """

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except json.JSONDecodeError as e:
        print(f"Decoding error JSON: {e}")
    except FileNotFoundError:
        print('File not found')
    except Exception as exc:
        print(f'Something went wrong: {exc}')