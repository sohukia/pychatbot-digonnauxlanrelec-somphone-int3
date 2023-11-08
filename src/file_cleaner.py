import src.utils as utils


def clear_content(text: list[str]) -> list[str]:
    """
    Remove punctuation
    :param text: str
    :return: text without punctuation
    """
    final_text = []
    for line in text:
        current_line = line.split()
        final_line = []
        for word in current_line:
            final_word = ''
            for i in range(len(word)):
                if word[i].isalnum():
                    final_word += word[i]
                elif word[(i - 1) % len(word)].isalpha() and (word[i] == '-' or word[i] == '\'') and word[
                        (i + 1) % len(word)].isalpha():
                    final_word += ' '
            final_line.append(final_word)
        final_text.append((' '.join(final_line)).strip() + '\n')
    return final_text


def copy_files(filenames: list[str]) -> None:
    utils.create_directory("./cleaned")
    for filename in filenames:
        new_filename = filename.split(utils.path_separator())
        new_filename[-2] = "cleaned"
        new_filename = utils.path_separator().join(new_filename)
        content = []
        with open(filename, 'r', encoding='utf-8') as input_file:
            for line in input_file.readlines():
                content += [''.join(word.lower() for word in line)]
        content = clear_content(content)
        with open(new_filename, 'w', encoding='utf-8') as output_file:
            output_file.writelines(content)
