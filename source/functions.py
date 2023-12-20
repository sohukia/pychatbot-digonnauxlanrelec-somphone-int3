"""
function.py
Authors: DIGONNAUX-LANRELEC Brewen, SOMPHONE Isabelle
Goal: main functionalities of the project, from tf_idf calculation to question tokenization.
"""

import re
import math
import source.utils as utils
from source.vector import Vector


class Functions:
    """
    WHY A CLASS:
    The reason why we use a class is that we want to be able to call the same functions multiple times and reuse easily the data.
    """

    def __init__(self):
        """
        The __init__ function is the constructor for the class. It initializes all the attributes
        that are used in this class.
        The first thing it does is copy files with cleared content, which means that it copies
        all the text files from speeches to cleaned and removes any non-alphabetical characters from them.
        
        Next, we create dictionaries about president : their name_surname, and the list of their name with duplicates
        and another one without duplicate. The list with duplicate is useful to browse a word within the text and gather meta-data

        Next, we create a list called corpus which contains the contents of every file in file_list.
        
        Next, we create a set called word_set which contains every word in the corpus.
        
        After that, we compute both tf of the corpus, it's idf and then the matrix td_idf
        """

        self.utils = utils.Utils()

        # copy files with cleared content, do not execute if folder alread exists
        if not self.utils.check_cleaned():
            self.copy_files(self.utils.list_files("./speeches", "txt"))
        self.file_list: list[str] = self.utils.list_files("./cleaned", "txt")

        # president data
        self.president_names: dict = {}
        self.president_list_with_duplicates: list[str] = self.extract_presidents()
        self.president_list = self.utils.del_duplicates(self.president_list_with_duplicates)
        self.create_president_dictionary()

        # tf idf computations
        self.corpus: list[str] = self.utils.cat_file(self.file_list)
        self.n_document: int = len(self.corpus)
        self.word_set: set = self.compute_word_set(self.corpus)

        self.tf: dict = self.term_frequency_corpus()
        self.idf: dict = self.inverse_document_frequency()
        self.matrix: dict = self.td_idf()
        

    def copy_files(self, filenames: list[str]) -> None:
        """
        The copy_files function takes a list of filenames as input and copies the content of each file into a new file in
        the cleaned directory. The function also formats the content by removing punctuation, stopwords, and non-alphabetic
        characters.

        Args:
            self: Refer to the object itself
            filenames: list[str]: Pass a list of filenames to the function

        """
        self.utils.create_directory("./cleaned")
        for filename in filenames:
            # create new path for the copied files
            file_name: list[str] = filename.split(self.utils.path_separator())
            file_name[-2] = "cleaned"
            new_filename = self.utils.path_separator().join(file_name)
            content: list[str] = []

            # extract content
            with open(filename, 'r', encoding='utf-8') as input_file:
                for line in input_file.readlines():
                    # ensure word are in lowercase
                    content += [''.join(word.lower() for word in line)]

            # format content
            content = self.utils.clear_content(content)

            # save formatted content into cleaned
            with open(new_filename, 'w', encoding='utf-8') as output_file:
                output_file.writelines(content)

    #############################
    ##     TF IDF FEATURES     ##
    #############################
    @staticmethod
    def compute_word_set(corpus: list[str]) -> set:
        """
        The compute_word_set function takes a corpus of documents and returns the set of all words in the corpus.

        Args:
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

    ################################
    ## PRESIDENT RELATED FEATURES ##
    ################################
    def extract_presidents(self) -> list[str]:
        """
        The extract_presidents function takes a list of file names and returns a list of the presidents' names.
        Watch out for duplicates that won't be deleted.
        Args:
            self: Refer to the instance of the class

        Returns:
            A list of strings
        """
        file_list: list[str] = [self.utils.clear_filename(file) for file in self.file_list]

        return file_list

    def create_president_dictionary(self) -> None:
        """
        The create_president_dictionary function creates a dictionary of the presidents' first names.
        """
        self.president_names: dict = {
            'Macron': 'Emmanuel',
            'Giscard dEstaing': 'Valery',
            'Chirac': 'Jacques',
            'Mitterrand': 'François',
            'Hollande': 'François',
            'Sarkozy': 'Nicolas'
        }

    # USAGE FEATURES
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

        for doc_matrix in self.matrix.values():
            for word, score in doc_matrix.items():
                if word not in word_scores:
                    word_scores[word] = []
                word_scores[word].append(score)
        for word, scores in word_scores.items():
            if all(i == 0 for i in scores):
                least_important_words.add(word)
        return least_important_words

    def compute_highest_score(self) -> set[str]:
        """
        The compute_highest_score function computes the highest score of each document and returns a set containing all words
        with the highest score.
        Use a set instead of a list to avoid duplicate word.

        Args:
            self: Refer to the instance of the class

        Returns:
            The set of words with the highest score
        """
        highest: set = set()
        highest_scores: list[float] = []
        for text in self.matrix.values():
            maxi_score: float = max(text.values())
            highest_scores.append(maxi_score)
        highest_score: float = max(highest_scores)
        del highest_scores
        for i in range(self.n_document):
            for word, score in self.matrix[i].items():
                if score == highest_score:
                    highest.add(word)
        return highest

    def search_word(self, word_to_search: str) -> tuple[list[int], int] or None:
        """
        The search_word function takes a word as input and looks for a word into the corpus. Find both
        who said this word_to_search and who said it the most.
        Uses a basic maximum comparison algorithm with a list to keep track of where the word was seen.

        Args:
            self: Access the attributes and methods of the class
            word_to_search: str: Search for the word in the documents

        Returns:
            A tuple with two elements:
        """
        found_index: list[int] = []
        maxi_index_document: int = 0
        maxi_score: int = 0
        for i in range(self.n_document):
            for word, score in self.tf[i].items():
                if word == word_to_search and score > 0:
                    if score > maxi_score:
                        maxi_score = score
                        maxi_index_document = i
                    found_index.append(i)
        return found_index, maxi_index_document

    def most_repeated_word_by(self, president_index: int) -> str:
        """
        The most_repeated_word_by function takes in a president index and returns the word that was used most frequently by
        that president. It does this by iterating through all the words in the tf dictionary for that president, and keeping
        track of which word has been repeated most often.

        Args:
            self: Refer to the object itself
            president_index: int: Specify which president we want to find the most repeated word for

        Returns:
            The word that is most repeated by the president at index president_index
        """
        maxi_word: str = ""
        maxi_score: float = 0
        for word, score in self.tf[president_index].items():
            if score > maxi_score:
                maxi_score = score
                maxi_word = word
        return maxi_word

    def first_to_say(self, word_to_search: str) -> int:
        """
        The first_to_say function takes a word as an argument and returns the index of the document in which it first appears.
        If the word does not appear in any documents, then - 1 is returned (should never happen).

        Args:
            self: Represent the instance of the class
            word_to_search: str: Specify the word to search for in the documents

        Returns:
            The index of the first document that contains the word_to_search
        """
        for i in range(self.n_document):
            for word, score in self.tf[i].items():
                if word == word_to_search and score > 0:
                    return i
        return -1

    def words_said_by_all_presidents(self) -> set[str]:
        """
        Look for the word that every president said excepted the unimportant words.
        Search for all words which have a tf score more than 1 in throughout corpus and a tf_df score more than 0.
        
        Returns:
            A list of words that every president said
        """
        common_words: set[str] = set()
        word_scores: dict = {}

        for doc_score in self.tf.values():
            for word, score in doc_score.items():
                if word not in word_scores:
                    word_scores[word] = []
                word_scores[word].append(score)
        for word, scores in word_scores.items():
            # ensure that the word appears everywhere and is not unimportant
            if all(i > 0 for i in scores) and word not in self.compute_least_important_words():
                common_words.add(word)

        return common_words

    ###############################
    ## CHATBOT RELATED FEATURES  ##
    ###############################
    def question_tokenization(self, question: str) -> set[str]:
        """
        Tokenize the question by splitting it into words.
        A token is a word in the question.

        Args:
            question: The question to tokenize

        Returns:
            set[str]: the set of words in the question
        """
        output: list = question.lower().split()
        # remove \n trailing char in the list of words cleaned from the question
        output = list(map(lambda x: x.replace('\n', ''), self.utils.clear_content(output)))
        if '' in output:
            output.remove('')  # still unknown why there is an empty string in the list
        return set(output)

    def remove_useless_words(self, tokens: set[str]) -> set[str]:
        """Remove the useless words from the question and keep only word that are in the corpus.

        Args:
            tokens (set[str]): The question to remove useless words from

        Returns:
            set[str]: The question without useless words.
        """
        return tokens.intersection(self.word_set).difference(self.compute_least_important_words())

    def question_tf_idf(self, question: str) -> dict:
        """Compute the tf_idf of the question.
        Same method as for the document but the score is not into a matrix but as a single dict.

        Args:
            question (str): The question to compute the tf_idf of

        Returns:
            dict: The tf_idf of the question
        """
        tokens: set[str] = self.question_tokenization(question)
        tokens = self.remove_useless_words(tokens)
        question_tf_idf: dict = dict.fromkeys(self.word_set, 0)

        tokens_tf: dict = {word: question.count(word) / len(question) for word in tokens}

        for i in range(self.n_document):
            for word in tokens:
                question_tf_idf[word] = tokens_tf[word] * self.idf[word]
        return question_tf_idf

    def most_relevant_document(self, question: str) -> str:
        """Find the most relevant document to the question.
        Simple maximum comparison algorithm.

        Returns:
            str: The most relevant document to the question
        """
        question_tf_idf: dict = self.question_tf_idf(question)
        vector: Vector = Vector()
        most_relevant_document: str = ""
        score_max: float = 0.0
        for i in range(self.n_document):
            score = vector.similarity(question_tf_idf=question_tf_idf, document_tf_idf=self.matrix[i])
            if score > score_max:
                score_max = score
                most_relevant_document = self.file_list[i]
        return most_relevant_document

    def question_compute_highest_score(self, question: str) -> str:
        """Look for the word with the highest tf_idf score in the question.

        Returns:
            str: This word
        """
        question_score: dict = self.question_tf_idf(question)
        max_score: float = 0.0
        max_word: str = ""
        for word, score in question_score.items():
            if score > max_score and word != 'comment':
                max_score = score
                max_word = word
        return max_word
    
    def select_starter(self, question: str) -> str:
        """Select the right starter for the answer. Depends on the question starter.

        Args:
            question (str): The question to select starter

        Returns:
            str: starter of the answer
        """
        starters: dict[str, str] = {
            "comment": "Après analyse, ",
            "pourquoi": "Car, ",
            "peux-tu": "Oui, bien sûr ! ",
        }
        question_starter: str = question.lower().split()[0]
        return starters[question_starter] if question_starter in starters.keys() else ""

    def generate_response(self, question: str) -> str:
        """Generate the response of the bot using the document with the similarity and the most relevant word.
        Use regular expression to match the word in the text and output the longest paragraph containing this word.

        Args:
            question (str): the question to answer

        Returns:
            str: the generated response
        """
        most_relevant_word: str = self.question_compute_highest_score(question)
        most_relevant_document: int = self.file_list.index(self.most_relevant_document(question))

        with open(utils.Utils.list_files('./speeches', 'txt')[most_relevant_document], encoding='utf-8') as file:
            content: str = ' '.join(file.readlines())

        pattern: str = r"(?i).*\b"+most_relevant_word+r"*\w.*"
        pattern_regex: re.Pattern = re.compile(pattern, re.IGNORECASE)

        match: list[str] = pattern_regex.findall(content)
        if match:
            return self.select_starter(question) + max(match, key=lambda x: len(x))

        return "No match found."
