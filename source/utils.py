"""
utils.py
Authors: DIGONNAUX-LANRELEC Brewen, SOMPHONE Isabelle
Goal: functions useful across documents
"""


import os
import platform


class Utils:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def list_files(path: str, ext: str) -> list[str]:
        """
        The list_files function takes a path and an extension as arguments.
        It returns a list of all files in the given directory with the given extension.

        Args:
            path: str: Specify the path to the directory that you want to list files from
            ext: str: Specify the file extension that you want to search for

        Returns:
            A list of strings
        """
        path: str = os.path.abspath(path)
        file_list: list[str] = []
        for file in os.listdir(path):
            if file.endswith(ext):
                absolute_path: str = os.path.abspath(os.path.join(path, file))
                file_list.append(absolute_path)
        return file_list

    @staticmethod
    def clear_filename(filename: str) -> str:
        """
        The clear_filename function takes a filename as an argument and returns the name of the file without any numbers or underscores.
            For example, if you pass in 'Nomination_Chirac1.txt', it will return 'Chirac'.

        Args:
            filename: str: Pass the filename to the function

        Returns:
            The filename without the underscore and extension

        """
        without_underscore: str = filename.split('_')[-1]
        without_ext: str = without_underscore.split('.')[0]
        without_number: str = ''.join([char for char in without_ext if not char.isdigit()])
        return without_number

    @staticmethod
    def del_duplicates(elements: list[str]) -> list[str]:
        """
        The del_duplicates function takes a list of elements and returns a new list with the duplicates removed.

        Args:
            elements: list[str]: Define the list of filenames that will be passed to the function

        Returns:
            A list of strings
        """
        return list(dict.fromkeys(elements).keys())

    @staticmethod
    def cat_file(file_list: list[str]) -> list[str]:
        """
        The cat_file function takes a list of file names and returns a list of strings, where each string is the contents
        of one file. The function should open each file in read mode, read all lines from the file into memory as a single
        string (using .readlines()), then join those lines together into one long string using ' '.join(...). Finally, it
        should return that long string.

        Args:
            file_list: list[str]: Pass in a list of files to be read

        Returns:
            A list of strings, where each string is the contents of a file
        """
        cat_file: list[str] = []
        for file in file_list:
            with open(file, 'r', encoding='utf-8') as f:
                content: list[str] = f.readlines()
                content_single_line: str = " ".join(map(lambda x: x.removesuffix('\n'), content))
                cat_file.append(content_single_line)
        return cat_file

    @staticmethod
    def create_directory(dir_name: str) -> None:
        """
        The create_directory function creates a directory with the name dir_name if not existing.

        Args:
            dir_name: str: Specify the name of the directory that will be created
        """
        if not os.path.exists(os.path.abspath(dir_name)):
            os.mkdir(os.path.abspath(dir_name))
    
    @staticmethod
    def check_cleaned() -> bool:
        return os.path.exists(os.path.abspath('./cleaned'))
    
    @staticmethod
    def path_separator() -> str:
        """
        The path_separator function returns a string that is the path separator for the current operating system.

        Returns:
            The path separator for the current operating system

        """
        return '\\' if platform.system() == "Windows" else "/"

    @staticmethod
    def clear_content(text: list[str]) -> list[str]:
        """
        The clear_content function takes a list of strings as input and returns a list of strings.
        It removes all non-alphanumeric characters from the text, except for '-' and ' when they are between two alphanumeric characters.

        Args:
            text: list[str]: Store the text to be cleaned

        Returns:
            A list of strings
        """
        final_text: list[str] = []
        # browse each line
        for line in text:
            current_line: list[str] = line.split()
            final_line: list[str] = []
            # browse each word
            for word in current_line:
                final_word: str = ''
                # browse each char
                for i in range(len(word)):
                    # check if the char is alphanumeric
                    if word[i].isalnum():
                        final_word += word[i]
                    # if the char is ' or -, check if it is betweens two char or not
                    elif word[(i - 1) % len(word)].isalnum() and (word[i] == '-' or word[i] == '\'') and word[
                        (i + 1) % len(word)].isalnum():
                        final_word += ' '
                final_line.append(final_word)
            final_text.append((' '.join(final_line)).strip() + '\n')
        return final_text

    @staticmethod
    def my_input(text: str) -> str:
        """
        The my_input function takes a string as input and returns a string.
        It is used to replace the input() function to avoid UnicodeDecodeError.

        Args:
            text: str: Store the text to be displayed

        Returns:
            A string
        """
        return input(text).encode('utf-8').decode('utf-8')