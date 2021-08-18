# Lab 6-1-1 question 1
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz
    
INVALID_NUMBER_MSG = "Digits only please."
PROGRAM_END_MSG = "Bye."
EXIT_PHRASE = "STOP!"

def display_list(my_list):
    """
        Display list in numbered order format with their respective item
    """
    print()
    for count, item in enumerate(my_list, start = 1):
       print(f"Item {count}: {item.strip().capitalize()}")
    print()
    print(PROGRAM_END_MSG)


my_listed_items = []
num_ofitems = ""
# Request number of items in list
while not num_ofitems.isdigit():
    num_ofitems = input("Please enter the number of items you would like to enter: ").strip()
    if not num_ofitems.isdigit():
        print(INVALID_NUMBER_MSG)

# Add items to list
add_item = "" # intialise empty string to start loop
count = 1 # intialise counter to track where the item will be addded
while add_item != EXIT_PHRASE and len(my_listed_items) != int(num_ofitems):
    add_item = input(f"Please enter item #{count} or STOP! if you want to finish early: ")

    if add_item != EXIT_PHRASE:
        # Add item to list
        my_listed_items.append(add_item)
        count += 1 

display_list(my_listed_items)



