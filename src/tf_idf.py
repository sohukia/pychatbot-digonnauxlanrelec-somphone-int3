import src.utils as utils
import math


def compute_word_set(corpus: list[str]) -> set():
    word_set = set()
    for document in corpus:
        words = document.split(' ')
        word_set = word_set.union(set(words))
    word_set.remove('')
    return word_set


def term_frequency_unit_file(text: str) -> dict:
    """
    Take a whole text as a list and analyse each word, 
    count the number of occurrences of each word and store the final and store everything in a dictionary with 
    the word as key and its occurrences counter as value
    :param text: str
    :return: term frequency dictionary
    """
    tf_dict = {}
    for word in text.split():
        if word not in tf_dict.keys():
            tf_dict[word] = 1
        else:
            tf_dict[word] += 1
    
    return {word: text.count(word) for word in text}


def term_frequency_corpus(corpus: list[str]) -> dict:
    """
    Browse the corpus of texts and make as much dictionnary of term_frequency as there are texts.
    :param corpus: list of document as strings
    """
    n_documents = len(corpus)
    word_set = compute_word_set(corpus)

    term_frequency = {i:dict.fromkeys(word_set, 0) for i in range(n_documents)}
    for i in range(n_documents):
        words = corpus[i].split(' ')
        for word in words:
            if word != '':
                term_frequency[i][word] += 1 
    return term_frequency


def inverse_document_frequency(path: str) -> dict:
    """
    For each word within the term_frequency_all
    Find if it appears at least once in each document frequency (list document frequency) then compute the inverse of this proportion
    (count the number of document)
    Finaly compute the logarithm base 10 of this value and associate it with each word.
    Each word should have at least one occurrence across all files. 
    :param path: path of the directory to compute idf
    :return: inverse document frequency of the corpus of files in the given directory
    """
    inv_doc_freq = {}
    all_texts = []
    files = utils.list_files(path, ".txt")
    corpus_size = len(files)

    for file in files:
        with open(file, 'r', encoding="utf-8") as f:
            # put all documents into a single list (its size will then be the number of document)
            all_texts.append(' '.join(map(lambda x: x.removesuffix('\n'),f.readlines())))
    
    word_set = compute_word_set(all_texts)
    for word in word_set:
        counter = 0
        for i in range(corpus_size):
            if word in all_texts[i].split(' '):
                counter += 1
        inv_doc_freq[word] = math.log10(corpus_size / counter)
    return inv_doc_freq        


def tf_idf_final(path: str) -> dict:
    files = utils.list_files(path, '.txt')
    corpus = utils.cat_files(files)
    word_set = compute_word_set(corpus)
    tf = term_frequency_corpus(corpus)
    idf = inverse_document_frequency(path)
    tfidf = tf.copy()

    for word in word_set:
        for i in range(len(corpus)):
            tfidf[i][word] = tf[i][word] * idf[word]
    return tfidf

