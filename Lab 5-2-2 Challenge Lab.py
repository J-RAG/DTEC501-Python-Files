# Lab 5-2-2 Challenge Lab 
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

SENTENCE_LENGTH_REQ = 2
FULLSTOP_CHAR = "."
EXIT_PHRASE = "Stop!"

user_name = input(f"Please enter your first name: ").strip().title()
non_exit_input = True

while non_exit_input:
    text_line = input(f"Please enter a sentence. Enter Stop! to stop running the program: ")
    # Assign a second text_line string with no spaces and Fullstop characters to test length 
    length_test = text_line.replace(" ","").replace(FULLSTOP_CHAR,"")
    if text_line == EXIT_PHRASE:
        non_exit_input = False

    # Sentence Input Validity
    elif all([text_line[0].isupper(),
            len(length_test) >= 2,
            text_line.count(FULLSTOP_CHAR) == 1]):
        space_count = text_line.count(" ")
        # Grammer print check
        if space_count == 1:
            print(f"There is {space_count} space in [{text_line}].")
        else:
            print(f"There are {space_count} spaces in [{text_line}].")
    else:
        print(f"[{text_line}] is not a sentence.")
print(f"Bye {user_name}")
