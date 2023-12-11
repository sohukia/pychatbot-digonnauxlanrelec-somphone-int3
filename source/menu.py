import source.functions as functions
from source.ux import UX


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
        print("\n",
              "\t ██████╗██╗  ██╗ █████╗ ████████╗██████╗  ██████╗ ████████╗\n",
              "\t██╔════╝██║  ██║██╔══██╗╚══██╔══╝██╔══██╗██╔═══██╗╚══██╔══╝\n",
              "\t██║     ███████║███████║   ██║   ██████╔╝██║   ██║   ██║   \n",
              "\t██║     ██╔══██║██╔══██║   ██║   ██╔══██╗██║   ██║   ██║   \n",
              "\t╚██████╗██║  ██║██║  ██║   ██║   ██████╔╝╚██████╔╝   ██║   \n",
              "\t ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═════╝  ╚═════╝    ╚═╝   \n")

    def select_mode(self) -> None:
        mode = 0
        while mode not in [1, 2]:
            mode = int(input("\tPlease select a mode.\t\n\ti.e. Part 1 functionalities (1) or Chatbot (2) : "))
        self.selected_mode = mode

    def menu_part_1(self) -> None:

        text_input = str("\tWhat action do you want to perform ?\n" +
                         "\t (1) Display the name of the presidents.\n" +
                         "\t (2) Display the most repeated word {president}.\n" +
                         "\t (3) Display the word with highest tf_idf score. i.e. the most important word.\n" +
                         "\t (4) Display the list of unimportant words.\n" +
                         "\t (5) Search for {word} and display metadata.\n" +
                         "\t (6) Look for who said {word} first.\n" +
                         "\t >_ ")
        while True:
            action = 0
            while action not in list(range(1, 6)):
                action = int(input(text_input))
                if action == 1:
                    self.display_pres()
                elif action == 2:
                    pass

    def display_pres(self) -> None:
        UX.write(self.functions.president_names)


    def menu_chatbot(self) -> None:
        pass


'''
import src.presidents as pn
import src.tf_idf as tf_idf
import platform
import os


class Menu:
    """
    Menu class: create a CLI with interactive commands
    """

    def __init__(self) -> None:
        self.clear()
        self.tfidf = tf_idf.tf_idf_final('./cleaned')
        self.presidents = pn.extract_presidents('./cleaned')
        self.presidents_with_duplicates = pn.extract_with_duplicates('./cleaned')
        self.message = ""
        self.commands = ["--help", "--president", "--tf_idf"]

        self.mainloop()

    @staticmethod
    def clear() -> None:
        """
        Uses the best command to clear terminal between cls and clear
        """
        os.system('cls') if platform.system() == "Windows" else os.system('clear')


    # HELP DISPLAY
    def help(self, command="") -> None:
        if command == "":
            self.message = """
        L1 international class chatbot project by SOMPHONE Isabelle and DIGONNAUX--LANRELEC Brewen.
        To use command, type any command followed by its parameters.
        Type --help [command] (without the double dash) to have more information on this command.
        Available commands:
        """ + "\n\t".join(self.commands) + """
        """
            return
        if command == "president":
            self.message = f"""
        --president display: will display the list of the president names in the cleaned repository
        --president most_repeated: will ask you to enter a president name and then display its most repeated word
        """
            return

        if command == "tf_idf":
            self.message = f"""
        --tf_idf highest: will display the list of the most important word(s) in the corpus
        --tf_idf lowest: will display the list of the least important words in the corpus (careful, there are a lot of them)
        --tf_idf search: will ask you to enter a word to look for and then display :
            1. who said this word
            2. who repeated it most
        --tf_idf search_first: will ask you to enter a word to look for and then display who said it first.
        """
            return

    def compute_action(self, command: list, param: list) -> None:
        # DEFAULT ERROR HANDLING
        if not command:
            message = ("""
        Please input a command with its params. Type --help for more information.
        List of available commands :""")
            for command in self.commands:
                message += """
        """ + command
            self.message = message
            return

        # PRESIDENT COMMAND
        if "--president" in command:
            index = command.index("--president")

            # LIST PRESIDENTS
            if param[index] == "display":
                self.message = pn.display_entire_name(self.presidents)
                return

            # DISPLAY MOST REPEATED WORD OF SELECTED PRESIDENT
            if param[index] == "most_repeated":
                president = ""
                while president not in self.presidents:
                    president = input(
                        f"\tPlease enter the president you want (must be in this list)\n\t{self.presidents}: ")
                self.message = "Most repeated word by " + president + ": " + tf_idf.most_repeated_word(
                    pn.index_president(self.presidents, president))
                return

            # ERROR MESSAGE
            self.message = "Need to specify a param for the command, type --help president for more information."
            return
        # DISPLAY INFORMATION
        if "--tf_idf" in command:
            index = command.index("--tf_idf")

            # DISPLAY THE WORD(S) WITH MOST IMPORTANCE
            if param[index] == "highest":
                self.message = tf_idf.compute_highest_score(self.tfidf)
                return

            # DISPLAY THE LIST OF LEAST IMPORTANT WORDS
            if param[index] == "lowest":
                self.message = tf_idf.compute_least_important_words(self.tfidf)
                return

            if param[index] == "search":
                word = input('Enter the word you are looking for: ')
                word_appearance = tf_idf.search_word(word)
                message = "These president said \"" + word + "\": "
                pres_who_said_it = []
                for index in word_appearance[0]:
                    if self.presidents_with_duplicates[index] not in pres_who_said_it:
                        pres_who_said_it.append(self.presidents_with_duplicates[index])
                message += ", ".join(pres_who_said_it)
                message += "\n\tAnd " + self.presidents_with_duplicates[word_appearance[1]] + " said it the most."
                self.message = message
                return

            if param[index] == "search_first":
                word = input('Enter the word you are looking for: ')
                self.message = (self.presidents_with_duplicates[tf_idf.first_to_said(word)] + " said \"" + word
                                + "\" first.")
                return
            self.message = "Need to specify a param for this command, type --help tf_idf for more information."
            return
        # HELP COMMAND
        if "--help" in command:
            try:
                index = command.index("--help")
                self.help(param[index])
            except IndexError:
                self.help()
            return

    def mainloop(self) -> None:
        while True:
            self.clear()
            self.help()
            self.greet()
            actions = input("\t>_").split()
            command = actions[::2]
            params = actions[1::2]
            self.compute_action(command, params)

'''
