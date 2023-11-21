import src.president_names as pres_name
import src.file_cleaner as file_c
import src.tf_idf as tf_idf
import src.utils as utils


"""
    Main program
    Import all files and executes them all along
"""


if __name__ == '__main__':
    # print president names
    presidents: list[str] = pres_name.extract_presidents('./speeches')
    pres_name.display_entire_name(presidents)

    # copy and clear files
    file_c.copy_files(utils.list_files('./speeches', '.txt'))

    # compute tf of each document
    documents_tf = tf_idf.list_document_tf('./cleaned')

    # compute tf with gouped document
    cleaned_tf = tf_idf.term_frequency_all('./cleaned')
    
        

