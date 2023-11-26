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
        self.message = ""

        self.commands = ["--help", "--president", "--tf_idf"]
        self.mainloop()

    @staticmethod
    def clear() -> None:
        """
        Uses the best command to clear terminal between cls and clear
        """
        os.system('cls') if platform.system() == "Windows" else os.system('clear')

    # HEADER DISPLAY
    def greet(self) -> None:
        print(
            f"""

         ██████╗██╗  ██╗ █████╗ ████████╗██████╗  ██████╗ ████████╗
        ██╔════╝██║  ██║██╔══██╗╚══██╔══╝██╔══██╗██╔═══██╗╚══██╔══╝
        ██║     ███████║███████║   ██║   ██████╔╝██║   ██║   ██║   
        ██║     ██╔══██║██╔══██║   ██║   ██╔══██╗██║   ██║   ██║   
        ╚██████╗██║  ██║██║  ██║   ██║   ██████╔╝╚██████╔╝   ██║   
         ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═════╝  ╚═════╝    ╚═╝   

        {self.message}
        """)

    # HELP DISPLAY
    def help(self, command="") -> None:
        if command == "":
            self.message = """
        L1 international class chatbot project of SOMPHONE Isabelle and DIGONNAUX--LANRELEC Brewen.
        To use command, type any command followed by its parameters.
        Available commands:""" + "\n\t\t".join(self.commands) + """
        Type --help [command] (without the double dash) to have more information on this command.
        """
            return
        if command == "president":
            self.message = f"""
        --president display: will display the list of the president names in the cleaned repository
        --president most_repeated: will ask you to enter a president name and then display its most repeated word
        """
            return

    def compute_action(self, command: list, param: list) -> None:
        # DEFAULT ERROR HANDLING
        if not command:
            self.message = "Please input a command with its params. Type --help for more information"
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

                self.message = pn.index_president(self.presidents, president)
                return

            # ERROR MESSAGE
            self.message = "Need to specify a param for the command"
            return
        # DISPLAY INFORMATION
        if "--tf_idf" in command:
            index = command.index("--tf_idf")

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
            self.greet()
            actions = input("\t>_").split()
            command = actions[::2]
            params = actions[1::2]
            print(command, params)
            self.compute_action(command, params)
