# Lab 10-1-1
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz
 
import os

def create_dir():
    """Create a directory. Return resulting message."""
    dir_name = get_dir_name(CREATE_ACTION)
    # Let's try to create it
    try:
        os.mkdir(dir_name)
        
    except:
        return "An error occurred while attempting to create the dir."

    else:
        return f"{dir_name} has been created."


def remove_dir():
    """ Remove a directory.  Return resulting message."""
    dir_name = get_dir_name(REMOVE_ACTION)
    # Let's try to remove it
    try:
        os.rmdir(dir_name)
        
    except:
        return "An error occurred while attempting to delete the dir."
    
    else:
        return f"{dir_name} has been removed."


def display_menu(display_item):
    """Diplay menu.  Return None."""
    
    print(*display_item, sep="\n")
    return None

    
def get_option():
    """ Return entered option. """
    
    return(input("Option: ").strip().lower())


def get_dir_name(action):
    """ Return the entered directory name. """
    
    return input(f"Please enter the name of the directory to be {action}: ").strip()


# Initialise objects
CREATE_DIRECTORY_OPTION = "c"
REMOVE_DIRECTORY_OPTION = "r"
EXIT_OPTION = "e"
CREATE_ACTION = "created"
REMOVE_ACTION = "removed"


option = ""
menu = ["", "Please enter one of the following options:", "C) Create a directory.", "R) Remove a directory.", "E) Exit"]
 
while option != EXIT_OPTION:

    display_menu(menu)
      
    option = get_option() 
 
    if option == CREATE_DIRECTORY_OPTION:
        msg = create_dir()
        print(msg)

    elif option == REMOVE_DIRECTORY_OPTION:
        msg = remove_dir()
        print(msg)
         
print("Bye.")
