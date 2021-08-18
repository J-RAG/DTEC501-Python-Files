# Lab 7-1-2 question 7
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

MSG_INPUT_GETNAME = "Contact: "
CONTACTS_ISEMPTY = "Sorry, there are no contacts."

def get_name(message):
    """
        Returns the Contact name as string
    """
    return input(message).strip().title()


def show_contact(contacts):
    """
        Asks the user to enter the name of a contact by calling the get_name function.
        If the entered contact is in contacts dictionary, displays the phone number of
        the contact, else informs the user that the contact is unknown. If the contacts
        dictionary is empty, inform user that the contacts are empty. Returns boolean
        True if the contact was present, otherwise it returns False.
    """
    contact_displayed = False

    # Check if contacts is empty
    if len(contacts) == 0:
        print(CONTACTS_ISEMPTY)
    else:
        person = get_name(MSG_INPUT_GETNAME)
        # Check if person is in the contacts dictionaty
        if not person in contacts:
            print(f"{person} is unknown.")

        else:
            # Display contact
            print(f"{person}: {contacts.get(person)}")
            contact_displayed = True # Re-update Boolean as contact was displayed
    return contact_displayed
