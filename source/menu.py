"""
TODO: create header with authors and role of the file
"""


import source.functions as functions
from source.ui import UI


class Menu:
    def __init__(self):
        self.greet()

        self.functions = functions.Functions()
        self.selected_mode = None
        self.select_mode()

        if self.selected_mode == 1:
            self.menu_part_1()
        elif self.selected_mode == 2:
            self.menu_chatbot()
        else:
            return
        

    @staticmethod
    def greet() -> None:
        """Display a fency text at startup
        """
        print(
            "\n",
            "\t ██████╗██╗  ██╗ █████╗ ████████╗██████╗  ██████╗ ████████╗\n",
            "\t██╔════╝██║  ██║██╔══██╗╚══██╔══╝██╔══██╗██╔═══██╗╚══██╔══╝\n",
            "\t██║     ███████║███████║   ██║   ██████╔╝██║   ██║   ██║   \n",
            "\t██║     ██╔══██║██╔══██║   ██║   ██╔══██╗██║   ██║   ██║   \n",
            "\t╚██████╗██║  ██║██║  ██║   ██║   ██████╔╝╚██████╔╝   ██║   \n",
            "\t ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═════╝  ╚═════╝    ╚═╝   \n")

    def select_mode(self) -> None:
        """Select either the chatbot or the firstPart features menu
        """
        mode = 0
        while mode not in [1, 2]:
            mode = int(input("\tPlease select a mode.\t\n\ti.e. Part 1 functionalities (1) or Chatbot (2) : "))
        self.selected_mode = mode

    def menu_part_1(self) -> None:
        """Part 1 features menu
        """
        actions = {
            1: lambda: UI.write(self.convert_names()),
            2: lambda: UI.write(self.most_repeated_display()),
            3: lambda: UI.write(self.most_important()),
            4: lambda: UI.write(self.unimportant()),
            5: lambda: UI.write(self.search_word()),
            6: lambda: UI.write(self.who_said_first()),
        }

        text_input = str(
            "Which action do you want to perform ?\n" +
            " (1) Display the name of the presidents.\n" +
            " (2) Display the most repeated word by {president}.\n" +
            " (3) Display the word with highest tf_idf score. i.e. the most important word.\n" +
            " (4) Display the list of unimportant words.\n" +
            " (5) Search for {word} and display metadata.\n" +
            " (6) Look for who said {word} first.\n"
        )
        
        while True:
            action = 0
            while action not in list(range(1, 7)):
                try:
                    UI.write(text_input)
                    action = int(input("\t>_ "))
                except ValueError:
                    UI.write("Please input a number !")

            actions[action]()

    def convert_names(self) -> str:
        """Convert president name dictionary into a printable string.

        Returns:
            str: name and surname on multiple lines
        """
        return "\n".join([" ".join([name, surname]) for name, surname in self.functions.president_names.items()])
    
    
    def most_repeated_display(self) -> None:
        """Display the most repeated word by a given president
        """

        president = ""
        while president not in self.functions.president_names:
            presidents_list_formatted: str = " - " + "\n\t - ".join(self.functions.president_list)
            president = input(
                f"\tPlease enter the president you want (must be in this list)\n\t{presidents_list_formatted}\n\t>_ ")
        return self.functions.most_repeated_word_by(self.functions.president_list.index(president))

    def search_word(self) -> str:
        """Input to search a word, then convert it into a printable value: who said the word and who said it first.
        Returns:
            str: name of the presidents who said the specific word.
        """
        word: str = ""
        while word not in self.functions.word_set:
            word = input("\tInput the word you are looking for :\n\t>_ ")
        # save the positions of the files where they are located
        poses: list = self.functions.search_word(word)
        # convert these position into president names
        presidents_who_said: str = '\n'.join([self.functions.president_list_with_duplicates[poses[0][i]] for i in range(len(poses[0]))])
        output: str = f"The president who said \"{word}\" are:\n{presidents_who_said}\nAnd {self.functions.president_list_with_duplicates[poses[1]]} said it first in the corpus"
        
        return output
        
    
    def who_said_first(self) -> str:
        """Return the name of the president that firstly said a the word prompted.

        Returns:
            str: string formatted to display with UI
        """
        word: str = ""
        while word not in self.functions.word_set:
            word = input("\tInput the word you are looking for :\n\t>_ ")
        return f"The first president who said \"{word}\" is {self.functions.president_list_with_duplicates[self.functions.first_to_say(word)]}"
        
    def most_important(self) -> str:
        """Return the most important(s) word(s) in the whole corpus as a string.

        Returns:
            str: printable with UI module
        """
        return "The most important(s) word(s) of the corpus is/are :\n" + "\n".join(self.functions.compute_highest_score())
    
    def unimportant(self) -> str:
        """Return the least important words in the whole corpus as a string.

        Returns:
            str: printable with UI module
        """
        return "The least important(s) word(s) of the corpus is/are :\n" + "\n".join(self.functions.compute_least_important_words())
