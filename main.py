import src.president_names as pres_name
import src.file_cleaner as file_c
import src.utils as utils

if __name__ == '__main__':
    presidents: list[str] = pres_name.extract_presidents('./speeches')
    pres_name.display_entire_name(presidents)

    file_c.copy_files(utils.list_files('./speeches'))
