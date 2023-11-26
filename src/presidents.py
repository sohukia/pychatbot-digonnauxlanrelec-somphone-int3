import src.utils as utils


def extract_presidents(path: str) -> list[str]:
    """
    Extract president name from given folder
    :param path:str
    :return: list of presidents names
    """
    file_list: list[str] = utils.list_files(path, '.txt')
    file_list = [utils.clear_filename(file) for file in file_list]
    file_list = utils.del_duplicates(file_list)

    return file_list


def display_entire_name(president_names: list[str]) -> None:
    """
    Associate each president name with its first name
    :param president_names:  str
    """
    names: dict = {
        'Macron': 'Emmanuel',
        'Giscard dEstaing': 'Valery',
        'Chirac': 'Jacques',
        'Mitterrand': 'François',
        'Hollande': 'François',
        'Sarkozy': 'Nicolas'
    }
    for president_name in president_names:
        print(names[president_name], president_name)


def index_president(president_names: list[str], president: str) -> int:
    return president_names.index(president)