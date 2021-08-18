# Lab 6-1-2 question 6
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

SUCCESSFUL_SORT = "The list has been sorted."
ONE_ITEM_MSG = "There is only one item in the list, the list does not need to be sorted."
EMPTY_LIST_MSG = "Sorry, the list is empty."
def sort_list(user_list):
    """
        Sorts the items in the list, informs the user and returns boolean True.
        If there is only one item in the list, informs the user and Returns
        boolean False. If there are no items in the list then sort_list informs
        the user and returns boolean False.
    """
    # Check if list needs to be sorted
    if len(user_list) > 1:
        user_list.sort()
        print(SUCCESSFUL_SORT)
        return True
    else:
        # Send appropiate message of why list cannot be sorted
        print(ONE_ITEM_MSG if len(user_list) == 1 else EMPTY_LIST_MSG)
        return False