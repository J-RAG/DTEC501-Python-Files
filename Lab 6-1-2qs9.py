# Lab 6-1-2 question 9
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

# Main Program Constants
MENU = [
    "Shopping list options.",
     "A) Add an item.",
     "R) Remove an item by its item number.",
     "T) Display the total number of items in the list.",
     "L) List all the items.",
     "S) Sort the list.",
     "E) Empty the list.",
     "C) Count the instances of an item in the list.",
     "Q) Quit."
    ]
ADD_OPTION = 1
REMOVE_OPTION = 2
NUMITEMS_OPTION = 3
DISPLAY_OPTION = 4
SORT_OPTION = 5
CLEAR_OPTION = 6
COUNTITEM_OPTION = 7
EXIT_PROGRAM = -1
END_PROGRAM_MSG = "Shopping time."
# Commented out as it was not specified in this lab to do this
# INVALID_OPTION = "Option does not exit. Please refer to the Shopping List Options." 

# Function Constants
REPLY_YES = "y"
INVALID_NUMBER_MSG = "The item number must be a positive integer."
SUCCESSFUL_SORT = "The list has been sorted."
ONE_ITEM_MSG = "There is only one item in the list, the list does not need to be sorted."
SUCCESSFUL_CLEAR = "All the items have been removed from the list."
EMPTY_LIST_MSG = "Sorry, the list is empty."


# Functions:
def display_list(generic_list, counter_reqd=True):
    """
        Display lists of items
        If required display items in a numbered format
    """
    # Check if list is Empty
    if len(generic_list) == 0:
        print(EMPTY_LIST_MSG)
        return False          

    # Counter Format Check
    elif counter_reqd:
        print()
        for count, item in enumerate(generic_list, start = 1):
            # Checks if the first letter of the item is upper case 
            # to grammitcally print it correctly
            print(f"Item {count}: {item.strip()}" if item[0].isupper() else\
                  f"Item {count}: {item.strip().capitalize()}")
    else:
        print()
        for item in generic_list:
            # Checks if the first letter of the item is upper case 
            # to grammitcally print it correctly
            print(f"{item.strip()}" if item[0].isupper() else\
                  f"{item.strip().capitalize()}")
    return True


def get_option():
    """
        Asks the user to enter an option, removes any extra spaces,
        converts the entered text into lower case and returns it as a string.
    """
    return input("Option: ").strip().lower()


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
    # Display total number of items in list
    print(get_total_items(user_list))
    return True


def remove_item(user_list):
    """
        Ask the user to enter the item number to be removed.
        If the item number is valid, item is deleted, user is
        informed and returns boolean True, else it returns boolean False.
        If the item number is 0 or list is empty, user is infromed
        and returns boolean False.
        
    """
    stay_in_loop = True
    # Check if List is Empty
    if len(user_list) == 0:
        print(EMPTY_LIST_MSG)
    else:
        while stay_in_loop:
            item_num = input("Please enter the item number of the"\
                                " item to remove or 0 to return: ").strip()
                
            # Input Validation Loop
            if not item_num.isdigit():
                print(INVALID_NUMBER_MSG)

            # Exit Program Condition 1 (EPC)
            elif item_num == "0":
                stay_in_loop = False 

            # EPC 2: Item Number validation
            # Note: index range starts at 0 so index must be minused by 1 
            elif int(item_num) - 1 >= len(user_list): 
                print(f"Sorry item {item_num} does not exist in the list.")
                stay_in_loop = False #DRY 
            else:
                # EPC 3: Remove item in list based on item number
                del user_list[int(item_num) - 1]
                print(f"Item {item_num} has been removed from the list.")
                return True
    return False


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


def empty_list(user_list):
    """
        Clears the items from the list and returns boolean True.
        If there are no items in the list, inform the user and
        return boolean False.
        
    """
    # Output Messge to user whether list has been cleared or not
    print(SUCCESSFUL_CLEAR if len(user_list) > 0 else EMPTY_LIST_MSG)
    if len(user_list) != 0:
        # Clear List
        user_list.clear()
        return True
    return False


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


# Main Program :
shopping_list = [] # Initialize Shopping list
option = "" # Initialze loop
# Loop Sequence
while option != MENU[EXIT_PROGRAM][0].lower():
    # Display Options
    display_list(MENU, False)
    # Input an option
    option = get_option()

    # Locate the Option entered
    if option == MENU[ADD_OPTION][0].lower():
        add_item(shopping_list)
    elif option == MENU[REMOVE_OPTION][0].lower():
        remove_item(shopping_list)
    elif option == MENU[NUMITEMS_OPTION][0].lower():
        print(get_total_items(shopping_list))
    elif option == MENU[DISPLAY_OPTION][0].lower():
        display_list(shopping_list)
    elif option == MENU[SORT_OPTION][0].lower():
        sort_list(shopping_list)
    elif option == MENU[CLEAR_OPTION][0].lower():
        empty_list(shopping_list)
    elif option == MENU[COUNTITEM_OPTION][0].lower():
        count_instances(shopping_list)
        
    # Personal Addition to program to notify user if they entered an invalid option
    # As it was not specified in this lab to do this it is commented out
    # elif option != MENU[EXIT_PROGRAM][0].lower():
        # print(INVALID_OPTION) 
print(END_PROGRAM_MSG)

