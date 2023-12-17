# Project Chatbot
## Project by DL.Brewen and S.Isabelle

### How to use

- In PyCharm :
Configure usage of `python3.11` with script `chatbot.py`. Ensure the `Emulate terminal in output console` is enabled to avoid error message. To do that, click on the `Current File` in the top left corner of the IDE and select `Edit Configurations...`. Then click on `Create new run configuration` and select `python`. Type `chatbot.py` in the script section. Then click on `Modify options` and add `Emulate terminal in output console`. Finally click `Apply` then `Ok`.
- Within a terminal: type `./chatbot.py`
- In VsCode: with `python` extension installed, open `chatbot.py` and click `run`

#### To start using the chatbot run the command `--help`, it will give the main commands and how to use them.

### Link of the Github repository [here](https://github.com/sohukia/pychatbot-digonnauxlanrelec-somphone-int3.git)


### Project description
This project is about creating a chatbot, a program that can simulate a conversation with a user. The chatbot uses a corpus of text in `./speeches`, a list of sentences that it will use to find the best answer to the user's input. The user can also ask for a specific sentence from the corpus. The chatbot can also be used as a simple search engine, it will return a list of sentences that contains the user's input.


#### How to read the code
1. [utils.py](./source/utils.py) all the functions that are needed across files
2. [functions.py](./source/functions.py) all the functions that deal with tf_idf
3. [vector.py](./source/vector.py) useful to understand the CHATBOT FEATURES part
4. [ui.py](./source/ui.py) just some text formatting
5. [menu.py](./source/menu.py) main menu
6. [chatbat.py](chatbot.py) program to run

#### Eases during the programming process
- Name properly the variables
- Document the code
- `Vector` class was easy to create once we had understand how data were structured
- File manipulation is also pretty easy since Brewen had already worked on such things in other projects.
- Structure the code, even though it could have been better the readability is always an objective while writing.
- Duplicate deletion ! We learn a new method : convert the list into a dictionary so that the keys are unique, keeping the same order (instead of using a set which do not keep order) and convert into a list the keys of this dictionary. 

#### The problems faced during the programming process
- Input function not recognize the character "-" in utf-8, we had to rewrite a new function that encode and decode utf-8 properly
- A word is found in the corpus but shouldn't even exists : "". We had to write a specific instruction to avoid errors with this word.
- Computation of the tf_idf matrix was difficult since there was an error : all the values were the same ! The issue came from a single line `matrix: dict = self.tf.copy()` was the right way to create the empty dictionnary.
- Code and memory usage optimisation were hard to tackle, we had to rewrite the whole codebase to use OOP paradygm which was better and easier to work on.
- Find the right way to display a fency menu.