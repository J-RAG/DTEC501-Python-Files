# Lab 5-3-1 question 2
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

def is_punctuated_correctly(text_string):
    """
        Returns True if  the last character is a
        full stop or an exclamation mark or a question mark.
        return False if the last character is a character
        other than one of the above.
    """
    # intialise a False statement for the result
    result = False
    # Validatoin check
    if any([text_string.strip().endswith("."),
            text_string.strip().endswith("?"),
            text_string.strip().endswith("!")]):
        result = True # Reassign result if condtion is satisfied
    return result

##source_line = "This is a correctly terminated sentence."
##proper_sentence = is_punctuated_correctly(source_line)
##print(proper_sentence)
##
### Correct sentence.
##correct_sentence = "This ends with a full stop. "
##correctly_capitalised = is_punctuated_correctly(correct_sentence)
##print(correctly_capitalised)
##print()
### Empty string.
##empty_string = ""
##correctly_capitalised = is_punctuated_correctly(empty_string)
##print(correctly_capitalised)
##
##text_source = "This is not a proper sentence"
##proper_sentence = is_punctuated_correctly(text_source)
##print(proper_sentence)
##print()
##text_source = " Nor is this is not a proper sentence "
##proper_sentence = is_punctuated_correctly(text_source)
##print(proper_sentence)
##
