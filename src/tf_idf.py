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
    Browse the corpus of texts and make as much dictionary of term_frequency as there are texts.
    :param corpus: list of document as strings
    """
    n_documents = len(corpus)
    word_set = compute_word_set(corpus)

    term_frequency = {i: dict.fromkeys(word_set, 0) for i in range(n_documents)}
    for i in range(n_documents):
        words = corpus[i].split(' ')
        for word in words:
            if word != '':
                term_frequency[i][word] += 1
    return term_frequency


def inverse_document_frequency(path: str) -> dict:
    """
    For each word within the term_frequency_all Find if it appears at least once in each document frequency (list
    document frequency) then compute the inverse of this proportion (count the number of document) Finally compute
    the logarithm base 10 of this value and associate it with each word. Each word should have at least one
    occurrence across all files. :param path: path of the directory to compute idf :return: inverse document
    frequency of the corpus of files in the given directory
    """
    inv_doc_freq = {}
    all_texts = []
    files = utils.list_files(path, ".txt")
    corpus_size = len(files)

    for file in files:
        with open(file, 'r', encoding="utf-8") as f:
            # put all documents into a single list (its size will then be the number of document)
            all_texts.append(' '.join(map(lambda x: x.removesuffix('\n'), f.readlines())))

    word_set = compute_word_set(all_texts)
    for word in word_set:
        counter = 0
        for i in range(corpus_size):
            if word in all_texts[i].split(' '):
                counter += 1
        inv_doc_freq[word] = math.log10(corpus_size / counter)
    return inv_doc_freq


def tf_idf_final(path: str) -> dict:
    """
    Compute the tf_idf score for each word and keep this values in a matrix where each row represent a document and each
    column is a word associated with its score.
    :param path: the path of the directory where the document are located
    :return dict: the tf_idf matrix
    """
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


def compute_least_important_words(corpus_tf_idf: dict) -> list[str]:
    """
    Give a list of unimportant words. That is the tf_idf score of these words are null.
    :param corpus_tf_idf: uses the tf_idf score to find them.
    :return list[str]: of the least important words.
    """
    tolerance: float = 1e-10
    least_important_words = set()
    for doc_id, doc_tf_idf in corpus_tf_idf.items():
        for word, tf_idf_score in doc_tf_idf.items():
            if abs(tf_idf_score) < tolerance:
                least_important_words.add(word)
    return list(least_important_words)


def compute_highest_score(corpus_tf_idf: dict) -> list[str]:
    """
    Look for the most important word of the whole corpus, uses the tf-idf score that emphasizes the importance of
    certain words for that. Allow multiple words to have the same importance.
    :param corpus_tf_idf: the tf_idf score will be used to browse
    :return list[str]: of most important words in the corpus
    """
    highest = []
    highest_scores = []
    for text in corpus_tf_idf.values():
        maxi_score = max(text.values())
        highest_scores.append(maxi_score)
    highest_score = max(highest_scores)
    for i in range(len(corpus_tf_idf)):
        for word, score in corpus_tf_idf[i].items():
            if score == highest_score and word not in highest:
                highest.append(word)
    return highest


def search_word(word_to_search: str) -> tuple[list[int], int]:
    """
    Look for a word into the corpus and find both who said this word and who said it the most.
    Basic maximum searching algorithm.
    :param word_to_search: the word to look for
    :return: first the list of who said it, then who said it the most
    """
    files = utils.list_files("./cleaned", ".txt")
    corpus = utils.cat_files(files)
    tf_corpus = term_frequency_corpus(corpus)

    found_index = []
    maxi_index = 0
    maxi_score = 0
    for i in range(len(tf_corpus)):
        for word, score in tf_corpus[i].items():
            if word == word_to_search and score > 0:
                if score > maxi_score:
                    maxi_score = score
                    maxi_index = i
                found_index.append(i)
                break
    return found_index, maxi_index


def most_repeated_word(president_index: int) -> str:
    """
    Take the president index given by user and return the most repeated word said by him. Use the term frequency and
    search for the maximum score possible, this word is the most repeated.
    :param president_index: document to analyze
    :return: the most repeated word by the given president
    """
    files = utils.list_files("./cleaned", ".txt")
    corpus = utils.cat_files(files)
    tf_corpus = term_frequency_corpus(corpus)
    maxi_word = ""
    maxi_score = 0
    for word, score in tf_corpus[president_index].items():
        if score > maxi_score:
            maxi_score = score
            maxi_word = word
    return maxi_word


def first_to_said(word_to_search: str) -> int:
    """
        Look for a word into the corpus and find who said it first in the corpus.
        :param word_to_search: the word to look for
        :return: the first president to have said the word
        """
    files = utils.list_files("./cleaned", ".txt")
    corpus = utils.cat_files(files)
    tf_corpus = term_frequency_corpus(corpus)

    for i in range(len(tf_corpus)):
        for word, score in tf_corpus[i].items():
            if word == word_to_search and score > 0:
                return i


def common_word(corpus_tf_idf: dict) -> list[str]:
    """
    Look for the word that every president said excepted the unimportant words.
    Search for all words which have a tf score more than 1 in throughout corpus and a tf_df score more than 0.
    Usage of function compute_least_important_words to find the others
    :param corpus_tf_idf: uses the matrix to verify if the word is unimportant or not.
    :return list[str]: the words not unimportant said by all presidents
    """
    files = utils.list_files("./cleaned", ".txt")
    corpus = utils.cat_files(files)
    word_set = compute_word_set(corpus)
    tf_corpus = term_frequency_corpus(corpus)
    least_important = compute_least_important_words(corpus_tf_idf)

    important_words = word_set - set(least_important)
    print(important_words)

    words = []
    for i in range(len(corpus)):
        for word, score in tf_corpus[i].items():
            if score > 0 and word not in least_important:
                words.append(word)
    common_words = []
    for word in words:
        if words.count(word) == len(corpus):
            common_words.append(word)
    return common_words
