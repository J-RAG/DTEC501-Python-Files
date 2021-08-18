# Lab 6-1-2 question 8
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

EMPTY_LIST_MSG = "Sorry, the list is empty."

def count_instances(user_list):
    """
        Enter the item to be counted and informs the user how
        many instances were found and returns boolean True.
        If there are no items in the list then inform the user
        and return boolean False.
    """

    # Empty List Condition
    if len(user_list) == 0:
        print(EMPTY_LIST_MSG)
        return False
    # Correct Grammar Output
    item_value = input("Please enter the item to be counted: ").strip().capitalize()
    single_instance = f"There is {user_list.count(item_value)} instance of [{item_value}] in the list."
    multi_instance = f"There are {user_list.count(item_value)} instances of [{item_value}] in the list."
    print(single_instance if user_list.count(item_value) == 1 else multi_instance)
    return True

