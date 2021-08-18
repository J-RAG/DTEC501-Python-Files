# Lab 6-1-2 question 5
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

INVALID_NUMBER_MSG = "The item number must be a positive integer."
EMPTY_LIST_MSG = "Sorry, the list is empty."

def remove_item(user_list):
    """
        Ask the user to enter the item number to be removed.
        If the item number is valid ,item is deleted, user is
        infored and returns boolean True, else it returns boolean False.
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

            # Exit Program Condition 1 (EPC 1)
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
                

