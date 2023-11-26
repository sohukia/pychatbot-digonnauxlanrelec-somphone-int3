import src.presidents as pn
import src.file_cleaner as fc
import src.tf_idf as tf_idf
import src.utils as utils
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
        self.mainloop()


    def clear(self) -> None:
        """
        Uses the best command to clear terminal between cls and clear
        """
        os.system('cls') if platform.system() == "Windows" else os.system('clear')


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


    def compute_action(self, command:list, param: list) -> None:
        if command == []:
            self.message = "Please input a command with its params. Type --help for more information"
            return
        # PRESIDENT COMMAND
        if "--president" in command:
            index = command.index("--president")
            if param[index] == "display":
                pn.display_entire_name(self.presidents)
                return
            if param[index] == "most_repeated":
                president = ""
                while president not in self.presidents:
                    president = input(f"Please enter the president you want (must be in this list)\n{self.presidents}: ")
                
                print(pn.most_repeated(self.presidents, president))
                return
            self.message = "Need to specify a param for the command"
            return
        # DISPLAY INFORMATIONS





    def mainloop(self) -> None:
        while True:
            self.clear()
            self.greet()
            actions = input(">_ ").split()
            command = actions[::2]
            params = actions[1::2]
            print(command, params)
            self.compute_action(command, params)