# Lab 5-1-2 Challenge Lab question 5
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

ODD_EVEN_MODULAR = 2
HALF_INDEX = 2
IS_EVEN_NUMBER = 0
FULLSTOP_CHAR = "."

user_name = input("Please enter your first name: ").strip().title()
text_line = input(f"{user_name}, please enter a sentence: ").strip()

# Sentence Input requirements Validation
if text_line[0].isupper() and text_line.endswith(FULLSTOP_CHAR):
    text_line = text_line.strip(FULLSTOP_CHAR) #remove the Fullstop Character in the sentence 
    size_of_text = len(text_line) 
    mid_index = size_of_text // HALF_INDEX
    
    # Middle character(s) odd / even length checks
    if (size_of_text % ODD_EVEN_MODULAR) == IS_EVEN_NUMBER:
        
        # Index slicing must be spread out by 2 to obtain the middle characters
        # Start slice position will be at: mid_index - 1
        # End position must be inclusive: mid_index + 1
        print(f"The characters [{text_line[mid_index - 1:mid_index + 1]}] are in the middle of the sentence.")
    else:
        print(f"The character [{text_line[mid_index]}] is in the middle of the sentence.")
else:
    print(f"Sorry {user_name}, a sentence must start with a capital letter and end with a full stop.")

