import math
import os
import platform


class Functions:
    def __init__(self):
        # copy files with cleared content
        self.copy_files(self.list_files("./speeches", "txt"))

        self.file_list: list[str] = self.list_files("./cleaned", "txt")
        self.corpus: list[str] = self.cat_file(self.file_list)
        self.n_document: int = len(self.corpus)

        self.word_set: set = self.compute_word_set(self.corpus)

        self.tf: dict = self.term_frequency_corpus()
        self.idf: dict = self.inverse_document_frequency()

        self.matrix: dict = self.td_idf()

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
    def del_duplicates(filenames: list[str]) -> list[str]:
        """
        The del_duplicates function takes a list of filenames and returns a new list with the duplicates removed.

        Args:
            filenames: list[str]: Define the list of filenames that will be passed to the function

        Returns:
            A list of strings
        """
        file_names: list[str] = []
        for filename in filenames:
            if filename not in file_names:
                file_names.append(filename)
        return file_names

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
                    # if the char is ' or -, check if it is betweens to char or not
                    elif word[(i - 1) % len(word)].isalpha() and (word[i] == '-' or word[i] == '\'') and word[
                            (i + 1) % len(word)].isalpha():
                        final_word += ' '
                final_line.append(final_word)
            final_text.append((' '.join(final_line)).strip() + '\n')
        return final_text

    def copy_files(self, filenames: list[str]) -> None:
        """
        The copy_files function takes a list of filenames as input and copies the content of each file into a new file in
        the cleaned directory. The function also formats the content by removing punctuation, stopwords, and non-alphabetic
        characters.

        Args:
            self: Refer to the object itself
            filenames: list[str]: Pass a list of filenames to the function

        """
        self.create_directory("./cleaned")
        for filename in filenames:
            # create new path for the copied files
            file_name: list[str] = filename.split(self.path_separator())
            file_name[-2] = "cleaned"
            new_filename = self.path_separator().join(file_name)
            content: list[str] = []

            # extract content
            with open(filename, 'r', encoding='utf-8') as input_file:
                for line in input_file.readlines():
                    # ensure word are in lowercase
                    content += [''.join(word.lower() for word in line)]

            # format content
            content = self.clear_content(content)

            # save formatted content into cleaned
            with open(new_filename, 'w', encoding='utf-8') as output_file:
                output_file.writelines(content)

    def compute_word_set(self, corpus: list[str]) -> set:
        """
        The compute_word_set function takes a corpus of documents and returns the set of all words in the corpus.

        Args:
            self: Represent the instance of the object itself
            corpus: list[str]: Pass the corpus to the function

        Returns:
            A set of all words in the corpus
        """
        word_set: set = set()
        for document in corpus:
            words: list[str] = document.split()
            word_set = word_set.union(set(words))
        return word_set

    def term_frequency_corpus(self) -> dict:
        """
        The term_frequency_corpus function takes the corpus and returns a dictionary of dictionaries.
        The outer dictionary has keys that are integers corresponding to each document in the corpus.
        The inner dictionaries have keys that are words from the word_set, and values that correspond to
        the number of times those words appear in their respective documents.

        Returns:
            A dictionary with the document number as a key and another dictionary with the word as a key and its frequency in that document
        """
        term_frequency: dict = {i: dict.fromkeys(self.word_set, 0) for i in range(self.n_document)}
        for i in range(self.n_document):
            words: list[str] = self.corpus[i].split()
            for word in words:
                if word != '':
                    term_frequency[i][word] += 1
        return term_frequency

    def inverse_document_frequency(self) -> dict:
        """
        The inverse_document_frequency function takes the corpus and returns a dictionary of words with their inverse document frequency.
        The inverse document frequency is calculated by taking the logarithm of the number of documents divided by how many times that word appears in all documents.

        Returns:
            A dictionary of words and their inverse document frequency
        """
        inv_doc_frequency: dict = {}
        for word in self.word_set:
            counter: int = 0
            for i in range(self.n_document):
                if word in self.corpus[i].split():
                    counter += 1
            inv_doc_frequency[word] = math.log10(self.n_document / counter)
        return inv_doc_frequency

    def td_idf(self) -> dict:
        """
        The td_idf function takes the tf and idf dictionaries and multiplies them together to create a new dictionary.
        The new dictionary is then returned.

        Returns:
            A dictionary of the tf-idf matrix
        """
        matrix: dict = self.tf.copy()
        for word in self.word_set:
            for i in range(self.n_document):
                matrix[i][word] = self.tf[i][word] * self.idf[word]
        return matrix

    def compute_least_important_words(self) -> set[str]:
        """
        The compute_least_important_words function takes the matrix of documents and words,
        and returns a set of words that are not important to any document.
        It does this by iterating through each word in the matrix, and checking if all scores for that word are 0.
        If they are all 0, then it is added to the least_important_words set.

        Args:
            self: Access the attributes and methods of the class

        Returns:
            A set of words that are not present in any document
        """
        least_important_words: set[str] = set()
        word_scores: dict = {}

        for doc_id, doc_matrix in self.matrix.items():
            for word, score in doc_matrix.items():
                if word not in word_scores:
                    word_scores[word] = []
                word_scores[word].append(score)

        for word, scores in word_scores.items():
            if all(i == 0 for i in scores):
                least_important_words.add(word)

        return least_important_words
