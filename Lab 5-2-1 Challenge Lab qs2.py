# Lab 5-1-2 Challenge Lab question 2
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

FULLSTOP_CHAR = "."

user_name = input("Please enter your first name: ").strip().title()
text_line = input(f"{user_name}, please enter a sentence: ").strip()
invalid_input_msg = f"Sorry {user_name}, a sentence must end with a full stop."

if not text_line.endswith(FULLSTOP_CHAR):
    print(invalid_input_msg)
else:
    print(f"The sentence contains {len(text_line) - 1} characters.")
