class UX:
    def __init__(self, text):
        self.write(text)

    @staticmethod
    def write(text) -> None:
        text = str(text)
        print('\t'+'-'*(len(text)+4))
        print('\t|', text, '|')
        print('\t' + '-' * (len(text) + 4))
