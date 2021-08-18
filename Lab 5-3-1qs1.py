# Lab 5-3-1 question 1
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

def starts_with_capital(text_string):
    """ Returns True if the first character of the
        parameter is a capital letter else return
        False.
    """
    # Check if string is Empty
    if text_string == "":
        result = False
    else:
        # Final check if first character is uppercase
        result = text_string[0].isupper()
        
    return result


### Starts with capital
##user_sentence = "This is correct."
##correctly_capitalised = starts_with_capital(user_sentence)
##print(correctly_capitalised)
### Starts with space
##starts_with_space = " This is not correct."
##correctly_capitalised = starts_with_capital(starts_with_space)
##print(correctly_capitalised)

### Correct sentence.
##correct_sentence = "This starts with a capital letter."
##correctly_capitalised = starts_with_capital(correct_sentence)
##print(correctly_capitalised)
##print()
### Empty string.
##empty_string = ""
##correctly_capitalised = starts_with_capital(empty_string)
##print(correctly_capitalised)

# Incorrect sentence.
text_line = "this is not correct."
correctly_capitalised = starts_with_capital(text_line)
print(correctly_capitalised)
