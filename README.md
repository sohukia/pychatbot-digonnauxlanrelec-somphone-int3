# Project Chatbot
## Project by DL.Brewen and S.Isabelle

### How to use

- In PyCharm :
Configure usage of `python3.11` with script `main.py`. Ensure the `Emulate terminal in output console` is enabled to avoid error message.
- Within a terminal: type `python3 main.py`
- In VsCode: with `python` extension installed, open `main.py` and click `run`

#### To start using the chatbot run the command `--help`, it will give the main commands and how to use them.

### Link of the Github repository [here](https://github.com/sohukia/pychatbot-digonnauxlanrelec-somphone-int3.git)


### Project description
This project is about text analysis. This project will allow you to understand some basic concepts used in text 
processing and help you understand one of the methods used in developing chatbots and/or generative 
artificial intelligences such as ChatGPT. 
Obviously, we're not talking here about manipulating neural networks, but in this project we're going to focus 
on a method based on words occurrences to generate intelligent answers from a corpus of texts. The aim is to 
design a system that can answer questions based on the frequency of words in the corpus. 
This application is based on the following algorithm: 
Data pre-processing: your program begins by collecting and pre-processing a set of documents in order to 
understand the nature of their contents, before using them to prepare answers. This phase cleans up the text 
by removing punctuation, converting letters to lower case, and dividing the text into words (or "tokens").
Creating a TF-IDF matrix: For each unique word in the documents, you'll need to calculate a TF-IDF vector 
using the TF-IDF method. Each word is associated with a vector whose dimension is equal to the number of 
documents in the corpus. This creates a TF-IDF matrix where each row represents a word and each column 
represents a document.
Question representation: When a question is asked, the chatbot performs the same pre-processing on the 
question. It then calculates a TF-IDF vector for this question, using the same vocabulary as the documents. The 
question vector has the same dimension as the vectors associated with the words in the corpus.
Similarity calculation: The chatbot calculates the similarity between the question vector and the word vectors 
in the corpus, using cosine similarity or another similarity measure. This enables it to determine which words 
in the corpus are most similar to the question.
Selecting the best answer: The chatbot identifies the words in the corpus most similar to the question, based 
on their TF-IDF similarity score. It then selects the answer that contains the greatest number of these similar 
words.
Provide answer: The chatbot returns the selected answer as the answer to the question asked.
