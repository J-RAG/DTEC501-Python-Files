# Lab 6-1-1 question 2
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz
    
INVALID_NUMBER_MSG = "An invalid item number was entered."
PROGRAM_END_MSG = "Bye."
EXIT_PHRASE = "0"

def display_list(my_list):
    """
        Display list in numbered order format with their respective item
    """
    for count, item in enumerate(my_list, start = 1):
       print(f"Item {count}: {item.strip().capitalize()}")
    print()

# test data of items_list below:
# items_list = ["Apples", "Bananas", "Potatoes", "Rice", "Marmite"]
# items_list = ["Potatoes", "Lentils", "Rice", "Tumeric"]
# items_list = ["Onions", "Coriander", "Potatoes", "Rice", "Marmite"]
# items_list = ["Lentils", "Mushrooms", "Potatoes", "Rice", "Tumeric"]
# items_list = ["Pears", "Rice", "Marmite"]
# items_list = ["Apples", "Rice", "Marmite"]
# items_list = ["Rice", "Cumin seeds", "Cinnamon"]
# ^ ^ ^ ^ ^ 

# Display items
display_list(items_list)
# remove_item items in list
item_num = input(f"Which item would you like to remove? (Enter 0 to exit). ").strip()
if item_num != EXIT_PHRASE: # Exit program if input entered is "0"
    # input validation
    if not item_num.isdigit():
        print(INVALID_NUMBER_MSG)

    # index validation
    elif int(item_num) - 1 >= len(items_list):
        print(f"Item number [{item_num}] is not in the list.")
    
    else:
        # remove_item item from list
        del items_list[int(item_num) - 1]
        display_list(items_list) # Display updated items
print(PROGRAM_END_MSG)






