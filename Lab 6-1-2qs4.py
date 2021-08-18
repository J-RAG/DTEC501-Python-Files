# Lab 6-1-2 question 4
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

REPLY_YES = "y"


def add_item(user_list):
    """
         Asks the user to enter the item to be added.
         If an item was added to the list, add_item returns
         boolean True otherwise it returns boolean False.
    """

    new_item = input("Please enter the item to be added: ").strip().capitalize()
    # Check if item is already in the list
    if user_list.count(new_item) == 0:
        user_list.append(new_item)  
    else:
        # Confirmation if you want to add dupilcate item to the list
        dup_reply = input(f"[{new_item}] is already in the list, please confirm "\
                          "that you want to add another [Y/N]: ").strip().lower()
        if dup_reply[0] == REPLY_YES:
            user_list.append(new_item)
        else:
            # Infrom user of not adding item and return False
            print(f"[{new_item}] was not added.")
            return False
    # Infrom user that item has been added and return True
    print(f"[{new_item}] has been added to the list.")
    # Inform user how many items using the get_total_items function
    print(get_total_items(user_list))
    return True

# Don't Paste get_total_items funct into moodle

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
