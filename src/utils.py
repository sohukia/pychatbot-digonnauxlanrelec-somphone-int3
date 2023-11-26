import os
import platform


def clear_filename(filename: str) -> str:
    """
    Extract president names within the filename by remove the underscore, the extension
    and the number (special cases).
    :param filename: the absolute path of the file name
    :return: president's last name
    """
    without_underscore: str = filename.split('_')[-1]
    without_ext: str = without_underscore.split('.')[0]
    without_numbers: str = ''.join([char for char in without_ext if not char.isdigit()])
    return without_numbers


def del_duplicates(filenames: list[str]) -> list[str]:
    """
    Delete duplicate names within the list of president list
    :param filenames: the names of presidents, with duplicates
    :return: the name of presidents, without duplicates
    """
    file_names = []
    for filename in filenames:
        if filename not in file_names:
            file_names.append(filename)
    return file_names


def list_files(path: str, ext: str) -> list[str]:
    """
    List the files within the given directory path.
    :param ext: extension specified
    :param path: directory path
    :return: List of file absolute paths
    """
    path: str = os.path.abspath(path)
    file_list: list[str] = []
    for file in os.listdir(path):
        if file.endswith(ext):
            absolute_path: str = os.path.abspath(os.path.join(path, file))
            file_list.append(absolute_path)
    return file_list


def cat_files(list_of_files: list[str]) -> list[str]:
    cat_file = []
    for file in list_of_files:
        with open(file, "r", encoding='utf-8') as f:
            content = f.readlines()
            content = ' '.join(map(lambda x: x.removesuffix('\n'), content))
            cat_file.append(content)

    return cat_file

        
def create_directory(name: str) -> None:
    """
    Check whether the directory exists or not and create it if necessary
    :param name: the name of the directory to check
    """
    if not os.path.exists(os.path.abspath(name)):
        os.mkdir(os.path.abspath(name))


def path_separator() -> str:
    """
    Ensure right file separator is used across Windows or Unix-like OSes
    """
    return '\\' if platform.system() == "Windows" else '/'

