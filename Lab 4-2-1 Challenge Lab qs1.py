# Lab 4-2-1 Challenge Lab question 1
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.

ALPHA_INPUT_MSG =  "Integers only please."
END_MESSAGE = "Bye."
INITIAL_START = 1
INCLUSIVE_END = 1

number_of_lines = input("Please enter the number of lines you would like displayed: ").strip()

# input Validation
if number_of_lines.isdigit():
    # print("Input Data is valid!")
    
    # Loop sequence 
    for line in range(INITIAL_START, int(number_of_lines) + INCLUSIVE_END):
        print(f"Line {line}")
    print(END_MESSAGE)

else:
    print(ALPHA_INPUT_MSG)
