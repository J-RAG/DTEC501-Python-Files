# Lab 5-1-2 Challenge Lab question 1
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

FULLSTOP_CHARACTER = "."
user_name = input("Please enter your first name: ").strip().title()
text_line = input(f"{user_name}, please enter a line of text: ").strip()

# Output
print(f"The first character in the line is {text_line[0]}")
last_char = text_line[-1]
# Check if input contains Fullstop at the end
if last_char == FULLSTOP_CHARACTER:
    # Re-update Last character so it selects the last character before fullstop
    last_char = text_line[-2]
    print(f"The last character before the full stop is {last_char}")
else:
    print(f"The last character in the line is {last_char}")