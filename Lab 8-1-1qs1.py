# Lab 8-1-1 question 1
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

def get_full_name(name_msg="Full name: "):
    """
        If the full name the user enters is valid and contains two or more names
        splits the name based on spaces and returns a tuple in the following format:
        True, name, name, name etc. Else returns a tuple of False and no name.
    """
    # user_names = input(name_msg).strip().title()
    user_names = "EllaMarija Lani-Yelich O'Connor".strip().title()
    # Name Validation: Each name is valid and there is More than one name
    # Replace Dash, Spacea and Apostrophe characters to bypass check validations
    # Split user_names to check if there's is more than one name. 
    if user_names.replace(" ", "").replace("-", "").replace("'", "").isalpha() \
       and len(user_names.split()) > 1:
            return True, user_names.split() # Return Tuple True, with List of names
    return False, # Return Tuple False, with No names

# DAVE SAID TEST CODE IS MISSING SOMETHING HELL EMAIL YOU IF ITS GOOD SKIP THIS QUESTION
# FOR NOW BOSS

FULL_NAME_MSG = "Please enter your full name: "
print(get_full_name(name_msg = FULL_NAME_MSG))
print(get_full_name(FULL_NAME_MSG))
print(get_full_name(FULL_NAME_MSG))
print(get_full_name(FULL_NAME_MSG))
print(get_full_name(FULL_NAME_MSG))
