import math


def term_frequency(text: str) -> dict:
    """
    Use comprehension to create a dictionary with each word as keys and its occurrences as values
    :param text: str
    :return: term frequency dictionary
    """
    return {word: text.count(word) for word in text}


def inverse_document_frequency(term_freq: dict) -> dict:
    """
    Take every value of the term frequency dictionary and compute the logarithm of the inverse of this frequency
    :param term_freq: dict containing each word frequency
    :return: inverse document frequency dictionary
    """
    return {word: math.log10(value) for word, value in term_freq.items()}

