# Lab 7-1-2 question 4
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

INVALID_NUMBER_MSG = "Digits only please."
def get_number_as_string(message, min_length):
    """
        Returns the entered number as a string.
    """
    invalid_number = True
    # Loop Sequence
    while invalid_number:
        # Remove trailing, leading and spaces in-bewteen
        number_text = input(message).strip().replace(" ","")
        if not number_text.isdigit():
            print(INVALID_NUMBER_MSG)
        # Check if input is a valid length
        elif len(number_text) < min_length:
            print(f"The number must be at least {min_length} digits long.")
        else:
            invalid_number = False
    return number_text
    

