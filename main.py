from source.functions import Functions


"""
    Main program
    Execute the menu file to display CLI
"""


if __name__ == '__main__':
    # copy and clear files
    # file_c.copy_files(utils.list_files('./speeches', '.txt'))

    # MAIN
    # menu = Menu()

    functions = Functions()
    print(functions.words_said_by_all_presidents())
