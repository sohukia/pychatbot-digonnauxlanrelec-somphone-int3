import textwrap

top_left: str = '╔'
top_right: str = '╗'
bot_left: str = '╚'
bot_right: str = '╝'
horizontal: str = '═'
vertical: str = '║'


class UI:
    def __init__(self): pass
    
    @staticmethod
    def write(text: str) -> None:
        size = 70
        print(f"\t{top_left}{horizontal * size}{top_right}")
        if '\n' in text:
            modified_text: list = list(map(lambda x: textwrap.fill(x).split('\n'), text.split('\n')))
            new_text: list = [line for coupleline in modified_text for line in coupleline]
        else:
            new_text: list = textwrap.fill(text).split('\n')
        for i in range(len(new_text)):
            new_text[i] = '\t' + vertical + " " + new_text[i] + " " * (69 - len(new_text[i])) + vertical
        print('\n'.join(new_text))
        print(f"\t{bot_left}{horizontal * size}{bot_right}")
        