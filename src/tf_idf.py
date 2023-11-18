import src.utils as utils
import math


def term_frequency(text: list) -> dict:
    """
    Use comprehension to create a dictionary with each word as keys and its occurrences as values
    :param text: str
    :return: term frequency dictionary
    """
    return {word: text.count(word) for word in text}


def list_document_tf(path: str) -> list[dict]:
    """
    Create the list of the term frequency for each document
    :param path: str
    :return: list of dict with tf frequency of each word
    """
    file_list = utils.list_files(path, '.txt')
    documents_tf = []
    for file in file_list:
        with open(file, 'r') as f:
            content = ' '.join([word.removesuffix('\n') for word in f.readlines()]).split()
            term_frequency_document = term_frequency(content)
        documents_tf.append(term_frequency_document)
    return documents_tf


def inverse_document_frequency(term_freq: dict) -> dict:
    """
    Take every value of the term frequency dictionary and compute the logarithm of the inverse of this frequency
    :param term_freq: dict containing each word frequency
    :return: inverse document frequency dictionary
    """
    return {word: math.log10(value) for word, value in term_freq.items()}
