# Lab 4-1-1 question 3
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.

PROGRAM_NAME = "Integer comparator."
INVALID_INPUT_MSG = "One or more of the numbers was invalid."
NUMTWO_SAME_MSG = "Two of the numbers are the same."
NUMALL_SAME_MSG = "All of the numbers are the same."
NUMDIFF_MSG = "All of the numbers are different."

print(PROGRAM_NAME)
user_name = input("Please enter your first name: ").strip().title()
first_num = input(f"Hi {user_name}, please enter the first number: ").strip()
second_num = input(f"Please enter the second number: ").strip()
third_num = input(f"Please enter the third number: ").strip()

#Number Validation
if not all ([first_num.isdigit(),
    second_num.isdigit(),
    third_num.isdigit()]):
    print(INVALID_INPUT_MSG)

elif all ([first_num == second_num,
       first_num == third_num,
       third_num == second_num]):
    print(NUMALL_SAME_MSG)

elif any ([first_num == second_num,
       first_num == third_num,
       third_num == second_num]):
    print(NUMTWO_SAME_MSG)

else:
    print(NUMDIFF_MSG)    