# Lab 7-1-2 question 1
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

EMPTY_LIST_MSG = "Sorry, the list is empty."

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