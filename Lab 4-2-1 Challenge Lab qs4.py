# Lab 4-2-1 Challenge Lab question 4
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

NO_INPUT_MSG = "You did not enter any characters."
EMPTY_STRING = ""
user_name = input("Please enter your first name: ").strip().capitalize()

# Input Validation:
if user_name == EMPTY_STRING:
    print(NO_INPUT_MSG)

else:
    count = 0
    # Loop Sequence
    for char in user_name:
        count += 1
        print(f"{count} {char}")

    # Grammer Check
    if count == 1:
        print(f"There is {count} character in {user_name}.")
    else:
        print(f"There are {count} characters in {user_name}.")
