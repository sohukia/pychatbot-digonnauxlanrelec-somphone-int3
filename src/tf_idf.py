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


def inverse_document_frequency(term_freq_all: dict) -> dict:
    """
    For each word within the term_frequency_all
    Find if it appears at least once in each document frequency (list document frequency) then compute the inverse of this proportion
    (count the number of document)
    Finaly compute the logarithm base 10 of this value and associate it with each word.
    Each word should have at least one occurrence across all files. 
    """
    inv_doc_freq = {}
    all_texts = []
    files = utils.list_files('./cleaned', ".txt")

    for file in files:
        with open(file, 'r', encoding="utf-8") as f:
            # put all documents into a single list (its size will then be the number of document)
            all_texts.append(' '.join(map(lambda x: x.removesuffix('\n'),f.readlines())))
    for word in term_freq_all.keys():
        counter = 0
        for text in all_texts:
            # if the word appears in the text, its proportion is increased by one
            if word in text:
                counter += 1
        # compute the inverse frequency of this word
        inv_doc_freq[word] = math.log10(1/counter)
    return inv_doc_freq
