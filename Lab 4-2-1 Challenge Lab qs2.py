# Lab 4-2-1 Challenge Lab question 2
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.

#Alternative to previous question but starts with the input and prints in reverse
ALPHA_INPUT_MSG =  "Integers only please."
END_MESSAGE = "Bye."
END = 0
REVERSE_SEQUENCE = -1

number_of_lines = input("Please enter the number of lines you would like displayed: ").strip()

# input Validation
if number_of_lines.isdigit():
    # print("Input Data is valid!")
    
    # Loop sequence 
    for line in range(int(number_of_lines), END, REVERSE_SEQUENCE):
        print(f"Line {line}")
    print(END_MESSAGE)

else:
    print(ALPHA_INPUT_MSG)

