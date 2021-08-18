# Lab 10-2-1
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz
 
import os
import cmd
CREATE_ACTION = "created"
REMOVE_ACTION = "removed"



def create_dir():
    """Create a directory. Return resulting message."""
    dir_name = get_dir_name(CREATE_ACTION)
    print(dir_name)
    # Let's try to create it
    try:
        os.mkdir(dir_name)
        
    except:
        return ("An error occurred while attempting to create the dir.")

    else:
        return (f"{dir_name} has been created.")


def remove_dir():
    """ Remove a directory.  Return resulting message."""
    dir_name = get_dir_name(REMOVE_ACTION)
    # Let's try to remove it
    print(dir_name)
    try:
        os.rmdir(dir_name)
        
        
    except:
        return ("An error occurred while attempting to delete the dir.")
    
    else:
        return (f"{dir_name} has been removed.")


def get_dir_name(action):
    """ Return the entered directory name. """
    
    return input(f"Please enter the name of the directory to be {action}: ").strip()


import sys
__saved_stdin_readline__ = sys.stdin.readline
def readline():
    s = __saved_stdin_readline__()
    return s

# COMMANDLINE 
class CliShell(cmd.Cmd):
    """Simple command processor example."""
    
    
    def __init__(self):
        """Constructor __init__"""
        cmd.Cmd.__init__(self)
        self.prompt = "Option: "
        self.intro = "Welcome to the directory utility.  Enter help to get started."
        self.stdin.readline = readline

    def default(self, option):
        print("{option} is an unknown option.")
        print("Try ? or help for the options.")

    def precmd(self, option):
        return option.lower()        

    def do_create(self, option):
        """Create a directory"""
        
        print(create_dir())
        
    def do_remove(self, option):
        """Remove a directory"""
        print(remove_dir())

    def do_exit(self, option):
        """Exit from the utility"""
        print("Bye.")
        return True

    #SHORTCUTS
    do_e = do_exit
    do_q = do_exit
    do_c = do_create
    do_r = do_remove


cli = CliShell()
cli.cmdloop()

    
