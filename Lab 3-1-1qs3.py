# Lab 3-1-1 question 3
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

user_name = input("Please enter your first name: ").strip().capitalize()
first_number = int(input(f"Hi {user_name}, please enter the first integer: "))
second_number = int(input(f"Thank you. Please enter the second integer: "))

#True false assignments
is_equal = str(first_number == second_number).lower()
isnot_equal = str(first_number != second_number).lower()
is_less = str(first_number < second_number).lower()
is_more = str(first_number > second_number).lower()
lessor_equal =  str(first_number <= second_number).lower()
moreor_equal =  str(first_number >= second_number).lower()

print()
print(f"It is {is_equal} that {first_number} is equal to {second_number}.")
print(f"It is {isnot_equal} that {first_number} is not equal to {second_number}.")
print()
print(f"It is {is_less} that {first_number} is less than {second_number}.")
print(f"It is {is_more} that {first_number} is greater than {second_number}.")
print()
print(f"It is {lessor_equal} that {first_number} is less than or equal to {second_number}.")
print(f"It is {moreor_equal} that {first_number} is greater than or equal to {second_number}.")
