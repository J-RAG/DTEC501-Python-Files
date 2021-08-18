# Lab 7-1-2 question 6
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

##MSG_INPUT_GETNAME = "Contact: "
CONTACTS_ISEMPTY = "Sorry, there are no contacts."

##def get_name(message):
##    """
##        Returns the Contact name as string
##    """
##    return input(message).strip().title()


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
