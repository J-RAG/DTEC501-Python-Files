# Lab 7-1-2 question 5
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz
INVALID_NUMBER_MSG = "Digits only please."
MINIMUM_PHONENUMBER_DIGITS = 3
MSG_INPUT_GETNAME = "Contact: "
MSG_INPUT_PHONENUMBER = "Contact number: "

def get_name(message):
    """
        Returns the Contact name as string
    """
    return input(message).strip().title()


def get_number_as_string(message, min_length):
    """
        Returns the entered number as a string.
    """
    number_text = ""
    while not number_text.isdigit():
        number_text = input(message).strip().replace(" ","")
        # Number Validation
        if not number_text.isdigit():
            print(INVALID_NUMBER_MSG)
        # Length Validation
        elif len(number_text) < min_length:
            print(f"The number must be at least {min_length} digits long.")
            number_text = "" # Re-invalidate number
    return number_text


def add_contact(contacts):
    """
        Obtains the name of a contact by calling the get_name function.
        If not in the contacts dictionary then obtain the phone number
        of the contact by calling the get_number_as_string function.
        returns boolean True if the contact was added,
        otherwise it returns False
    """
    person = get_name(MSG_INPUT_GETNAME)
    if person in contacts:
        print(f"Sorry, {[person]} is already in the phone system.")
        return False
    else:
        phone_number = get_number_string(MSG_INPUT_PHONENUMBER, MINIMUM_PHONENUMBER_DIGITS)
        contacts[person] = phone_number
        print(f"{} has been added with the number: {phone_number}.")
        return True


