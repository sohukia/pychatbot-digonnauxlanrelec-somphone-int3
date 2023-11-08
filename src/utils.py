import os
import platform


def clear_filename(filename: str) -> str:
    without_underscore = filename.split('_')[-1]
    without_ext = without_underscore.split('.')[0]
    without_numbers = ''.join([char for char in without_ext if not char.isdigit()])
    return without_numbers


def del_duplicates(filenames: list) -> list:
    return list(set(filenames))


def list_files(path: str) -> list:
    ext = '.txt'
    path = os.path.abspath(path)
    file_list = [os.path.abspath(os.path.join(path, file)) for file in os.listdir(path) if file.endswith(ext)]
    return file_list


def create_directory(name: str) -> None:
    if not os.path.exists(os.path.abspath(name)):
        os.mkdir(os.path.abspath(name))


def path_separator() -> str:
    return '\\' if platform.system() == "Windows" else '/'
