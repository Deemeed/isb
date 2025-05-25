import json


def readfile(filename: str) -> str | dict:

    """
    Reads data from file
    :param filename: directory
    :param mode: mode of reading
    :return: data
    """

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            if filename.endswith(".json"):
                return json.load(file)
            else:
                return file.read()
    except json.JSONDecodeError as e:
        print(f"Decoding error JSON: {e}")
    except FileNotFoundError:
        print('File not found')
    except Exception as exc:
        print(f'Something went wrong: {exc}')


def writefile(filename: str, data: str | dict) -> None:

    """
    Writes data to txt file
    :param filename: path to file
    :param data: data to write
    :param mode: mode of reading
    :return: none
    """

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            if filename.endswith(".json"):
                json.dump(data, file, ensure_ascii=False, indent=4)
            else:
                file.write(data)
    except json.JSONDecodeError as e:
        print(f"Decoding error JSON: {e}")
    except FileNotFoundError:
        print('File not found')
    except Exception as exc:
        print(f'Something went wrong: {exc}')