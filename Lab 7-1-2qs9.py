# Lab 7-1-2 question 9
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

CONTACTS_ISEMPTY = "Sorry, there are no contacts."
CLEAR_SUCCESSFUL = "All the contacts have been removed."

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

# Test for correct parameter name
current_contacts = {"Ms One":101,
                    "Mr Two":102,
                    "Mrs Three":103
                    }
return_status = empty_contacts(current_contacts)
print(f"The contacts dictionary is now: {current_contacts}")
print(return_status)
