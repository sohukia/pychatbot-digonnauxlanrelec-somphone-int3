import src.utils as utils


def clear_content(text: list[str]) -> list[str]:
    """
    Remove punctuation by browsing each word of each line and delete any special char.
    Special treatment over ' and - between words.
    :param text: str
    :return: text without punctuation
    """
    final_text = []
    # browse each line
    for line in text:
        current_line = line.split()
        final_line = []
        # browse each word
        for word in current_line:
            final_word = ''
            # browse each char
            for i in range(len(word)):
                # check if the char is alphanumeric
                if word[i].isalnum():
                    final_word += word[i]
                # if the char is ' or -, check if it is betweens to char or not
                elif word[(i - 1) % len(word)].isalpha() and (word[i] == '-' or word[i] == '\'') and word[
                        (i + 1) % len(word)].isalpha():
                    final_word += ' '
            final_line.append(final_word)
        final_text.append((' '.join(final_line)).strip() + '\n')
    return final_text


def copy_files(filenames: list[str]) -> None:
    """
    Extract file content and format it with lowercase and without special characters
    :param filenames: the list of file names in the directory
    """
    # ensure cleaned directory exists before doing anything
    utils.create_directory("./cleaned")

    for filename in filenames:
        # create new path for the copied files
        new_filename = filename.split(utils.path_separator())
        new_filename[-2] = "cleaned"
        new_filename = utils.path_separator().join(new_filename)
        content = []

        # extract content
        with open(filename, 'r', encoding='utf-8') as input_file:
            for line in input_file.readlines():
                # ensure word are in lowercase
                content += [''.join(word.lower() for word in line)]

        # format content
        content = clear_content(content)

        # save formatted content into cleaned
        with open(new_filename, 'w', encoding='utf-8') as output_file:
            output_file.writelines(content)
