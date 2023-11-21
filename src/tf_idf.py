import src.utils as utils
import math


def term_frequency(text: list) -> dict:
    """
    Take a whole text as a list and analyse each word, 
    count the number of occurrences of each word and store the final and store everything in a dictionary with 
    the word as key and its occurrences counter as value
    :param text: str
    :return: term frequency dictionary
    """
    tf_dict = {}
    for word in text:
        if word not in tf_dict.keys():
            tf_dict[word] = 1
        else:
            tf_dict[word] += 1
    
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
        with open(file, 'r', encoding='utf-8') as f:
            content = ' '.join([word.removesuffix('\n') for word in f.readlines()]).split()
            term_frequency_document = term_frequency(content)
        documents_tf.append(term_frequency_document)
    return documents_tf


def term_frequency_all(path: str) -> dict:
    """
    Compute term frequency across all documents in the given directory
    :param path: str
    :return: dictionary of tf across documents.
    """
    file_list = utils.list_files(path, '.txt')
    text_across_documents = []

    for file in file_list:
        with open(file, 'r', encoding='utf-8') as f:
            content = ' '.join([word.removesuffix('\n') for word in f.readlines()]).split()
            text_across_documents += content
    return term_frequency(text_across_documents)


def tf_idf(
"""
For each word within the term_frequency all
Find if it appears at least once in each document frequency (list document frequency) then compute the inverse of this proportion
(count the number of document)
Finaly compute the logarithm base 10 of this value and associate it with each word.
Each word should have at least one occurrence across all files. 
"""




def inverse_document_frequency(term_freq: dict) -> dict:
    """
    Take every value of the term frequency dictionary and compute the logarithm of the inverse of this frequency
    :param term_freq: dict containing each word frequency
    :return: inverse document frequency dictionary
    """
    return {word: math.log10(value) for word, value in term_freq.items()}
