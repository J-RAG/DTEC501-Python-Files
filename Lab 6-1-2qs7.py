# Lab 6-1-2 question 7
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

SUCCESSFUL_CLEAR = "All the items have been removed from the list."
EMPTY_LIST_MSG = "Sorry, the list is empty."

def empty_list(user_list):
    """
        Clears the items from the list and returns boolean True.
        If there are no items in the list,inform the user and
        return boolean False.
        
    """
    # Output Messge to user whether list has been cleared or not
    print(SUCCESSFUL_CLEAR if len(user_list) > 0 else EMPTY_LIST_MSG)
    if len(user_list) != 0:
        # Clear List
        user_list.clear()
        return True
    return False
