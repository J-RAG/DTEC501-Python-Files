# Lab 4-2-1 Challenge Lab question 3
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

ZERO_INPUT_VAL = 0
ZERO_INCREMENT_MSG = "I can't increment in steps of 0."
END_MSG = "Bye."
INVALID_INPUT_MSG = "Positive non zero integers only please."
INITIAL_START = 1
INCLUSIVE_END = 1

input_numbers = input("Please enter how many numbers you would like displayed: ").strip()
increment_val = input("Please enter the increment value: ").strip()

# Input Validation
# note: is.digit() returns False to negative string numbers eg "-7" will return False 
if not(input_numbers.isdigit() and increment_val.isdigit()):
    print(INVALID_INPUT_MSG)
elif int(increment_val) == ZERO_INPUT_VAL:
    print(ZERO_INCREMENT_MSG)

else:
    # print("All inputs are Valid!")

    # Loop Sequence
    value = INITIAL_START # intitalize starting value to be set at 1
    for counter in range(INITIAL_START, int(input_numbers) + INCLUSIVE_END):
        print(f"Counter: {counter} value: {value}")
        value += int(increment_val)
    print(END_MSG)

