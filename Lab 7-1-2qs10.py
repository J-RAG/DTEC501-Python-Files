# Lab 7-1-2 question 10
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

# MAIN PROGRAM CONSTANTS
MENU = [
 "Telephone contact options.",
 "A) Add a contact.",
 "R) Remove a contact.",
 "S) Show/find a contact.",
 "D) Display all contacts.",
 "E) Empty all contacts.",
 "Q) Quit."
 ]

ADD_OPTION = "a"
REMOVE_OPTION = "r"
SHOW_OPTION = "s"
DISPLAY_OPTION = "d"
EMPTY_OPTION = "e"
EXIT_OPTION = "q"
END_OF_PROGRAM = "Bye."
# Commented out as it was not specified in this lab to do this
# INVALID_OPTION = "Option does not exit. Please refer to the Telephone Contact Options." 


# FUNCTION CONSTANTS
EMPTY_LIST_MSG = "Sorry, the list is empty."
INVALID_NUMBER_MSG = "Digits only please."
MINIMUM_PHONENUMBER_DIGITS = 3
MSG_INPUT_GETNAME = "Contact: "
MSG_INPUT_PHONENUMBER = "Contact number: "
CONTACTS_ISEMPTY = "Sorry, there are no contacts."
CLEAR_SUCCESSFUL = "All the contacts have been removed."


def display_list(generic_list, counter_reqd=True):
    """
        Display lists of items
        If required display items in a numbered format
    """
    # Check if list is Empty
    if len(generic_list) == 0:
        print(EMPTY_LIST_MSG)
        return False 
                
    else:
        # Display List
        print()
        for count, item in enumerate(generic_list, start = 1):
            # Numbered Format Check
            print(f"Item {count}: {item}" if counter_reqd else item)
        return True
    

def get_option():
    """
        Asks the user to enter an option, removes any extra spaces,
        converts the entered text into lower case and returns it as a string.
    """
    return input("Option: ").strip().lower()


def get_name(message):
    """
        Returns the Contact name as string
    """
    return input(message).strip().title()


def get_number_as_string(message, min_length):
    """
        Returns the entered number as a string.
    """
    invalid_number = True
    # Loop Sequence
    while invalid_number:
        # Remove trailing, leading and spaces in-bewteen
        number_text = input(message).strip().replace(" ","")
        # Check if input is a number
        if not number_text.isdigit():
            print(INVALID_NUMBER_MSG)
        # Check if input is a valid length
        elif len(number_text) < min_length:
            print(f"The number must be at least {min_length} digits long.")
        else:
            invalid_number = False
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
    # Check if person is in contacts
    if person in contacts:
        print(f"Sorry, {[person]} is already in the phone system.")
        return False
    else:
        # Input phone number to be added
        phone_number = get_number_as_string(MSG_INPUT_PHONENUMBER, MINIMUM_PHONENUMBER_DIGITS)
        contacts[person] = phone_number # add person's name and number to the contacts
        print(f"{person} has been added with the number: {phone_number}.")
        return True


def remove_contact(contacts):
    """
        Enter the name of a contact by calling the get_name function.
        Removes contact if the entered contact is in the contacts dictionary and
        informs the user contact has been removed, else informs the user that
        the entered contact is not present. If there are no contacts in the contact
        dictionary, user is informed. Returns boolean True if the contact was
        removed, otherwise it returns False.
    """
    contact_removed = False

    # Check if contacts is empty
    if len(contacts) == 0:
        print(CONTACTS_ISEMPTY)
    else:
        person = get_name(MSG_INPUT_GETNAME)
        # Check if contact is not in contacts dictionary
        if not person in contacts:
            print(f"Sorry, {person} is not a contact.")
        else:
            # Remove contact and inform User
            contacts.pop(person)
            print(f"{person} has been removed from the contacts.")
            contact_removed = True # Update Boolean as Contact was removed
    return contact_removed


def show_contact(contacts):
    """
        Asks the user to enter the name of a contact by calling the get_name function.
        If the entered contact is in contacts dictionary, displays the phone number of
        the contact, else informs the user that the contact is unknown. If the contacts
        dictionary is empty, inform user that the contacts are empty. Returns boolean
        True if the contact was present, otherwise it returns False.
    """
    contact_displayed = False
    # Check If contacts is empty
    if len(contacts) == 0:
        print(CONTACTS_ISEMPTY)
    else:
        person = get_name(MSG_INPUT_GETNAME)
        # Check if person is in contacts
        if not person in contacts:
            print(f"{person} is unknown.")

        else :
            # Display person's name and phone number
            print(f"{person}: {contacts.get(person)}")
            contact_displayed = True
    return contact_displayed


def display_contacts(contacts):
    """
        Displays the contacts and associated phone numbers
        If the contacts dictionary is empty then user is informed
        Returns boolean True if the contacts were displayed,
        otherwise it returns False.
    """
    # Check if contacts is empty
    if len(contacts) == 0:
        print(CONTACTS_ISEMPTY)
        return False
    
    # Display every contact and their phone number
    for person in contacts:
        print(f"{person}: {contacts.get(person)}")
    return True


def empty_contacts(contacts):
    """
        If contacts dictionary is empty then informs the user and
        returns False. Else, Removes all the contacts from the dictionary
        and returns True.
    """
    # Infrorm user if contacts have been cleared
    # else infrom them it is already empty
    print(CLEAR_SUCCESSFUL if len(contacts) > 0 else CONTACTS_ISEMPTY)

    # Return False if contacts is empty
    if len(contacts) == 0:
        return False
    # Clear contacts and return True
    contacts.clear()
    return True

# //////////////////////////////////////////
# MAIN PROGRAM
telephone_contacts = {}
option = "" 

# Initialize dictionary of Functions "action"
# to be called by their correspoding letters
action = {
    ADD_OPTION: add_contact,
    REMOVE_OPTION: remove_contact,
    SHOW_OPTION: show_contact,
    DISPLAY_OPTION: display_contacts,
    EMPTY_OPTION: empty_contacts,
    }
# Loop Sequence
while option != EXIT_OPTION:
    # Display Options
    display_list(MENU, False)
    # Input an option
    option = get_option()
    # Retrive Function through option
    if option in action:
        action[option](telephone_contacts)
        
    # Personal Addition to program to notify user if they entered an invalid option
    # As it was not specified in this lab to do this it is commented out
    # else:
        # print(INVALID_OPTION)
    
print(END_OF_PROGRAM)









