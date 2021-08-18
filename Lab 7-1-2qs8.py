# Lab 7-1-2 question 8
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

CONTACTS_ISEMPTY = "Sorry, there are no contacts."

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
