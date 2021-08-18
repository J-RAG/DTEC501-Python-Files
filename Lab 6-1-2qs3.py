# Lab 6-1-2 question 3
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

def get_total_items(user_list):
    """
        Returns a string which is a message showing
        the total number of elements there are in the list.
    """
    # Grammar singular/plural output check
    if len(user_list) != 1:
        return f"There are {len(user_list)} items in the list."
    else:
        return f"There is {len(user_list)} item in the list."

