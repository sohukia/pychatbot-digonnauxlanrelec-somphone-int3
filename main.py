import src.file_cleaner as file_c
import src.utils as utils
from src.menu import Menu


"""
    Main program
    Execute the menu file to display CLI
"""


if __name__ == '__main__':
    # copy and clear files
    file_c.copy_files(utils.list_files('./speeches', '.txt'))
    
    # MAIN
    menu = Menu()

