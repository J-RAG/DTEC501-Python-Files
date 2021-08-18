# Lab 4-1-3 Challenge Lab
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.

EQUAL_RESULT = "an equilateral" 
ISO_RESULT = "an isosceles"
SCALENE_RESULT = "a scalene"
INVALID_INPUT_MSG = "One or more of the sides was not valid."
ZERO_INPUT_MSG = "You can't have a triangle with a side of 0."
ZERO_INPUT = 0
VALID_CHAR = "+" #inputs with this char (as a leadingspace) are valid

side_one = input("Enter the length of side 1: ").strip().lstrip(VALID_CHAR)
side_two = input("Enter the length of side 2: ").strip().lstrip(VALID_CHAR)
side_three = input("Enter the length of side 3: ").strip().lstrip(VALID_CHAR)


# input validation check
if not all([side_one.isdigit(),
	side_two.isdigit(),
	side_three.isdigit()]):
	# selfnote: All negative numbers are False when using isdigit() since "-" is 
	# a non-digit char, aswell as "+" char but we lstrip() it so it is valid for 
	# this case since the lab input allows numbers with "+". We do not need to remove
	# "-" char in this case since we cannot have negative inputs on side lengths. 
	
	# print("TestCheck: Input(s) is invalid.")
	print(INVALID_INPUT_MSG)
	
elif any([int(side_one) == ZERO_INPUT,
	int(side_two) == ZERO_INPUT,
	int(side_three) == ZERO_INPUT]):
	# print("TestCheck: Inputs are valid but a Zero input has been made.")
	print(ZERO_INPUT_MSG)
	
else:
	# print("TestCheck: all Inputs are valid!")
	
	# initialize comparisson list for readablitly
	compare_size = [int(side_one) == int(side_two),
		int(side_one) == int(side_three),
		int(side_two) == int(side_three)]
		
	if all(compare_size):
		# print("TestCheck: Result is an Equilateral Triangle.")
		print(f"A triangle with sides {side_one}, {side_two} and {side_three} is {EQUAL_RESULT} triangle.")
	
	elif not any(compare_size):
		# print("TestCheck: Result is a Scalene Triangle.")
		print(f"A triangle with sides {side_one}, {side_two} and {side_three} is {SCALENE_RESULT} triangle.")
		
	else:
		# print("TestCheck: Result is an Isosceles Triangle.")
		print(f"A triangle with sides {side_one}, {side_two} and {side_three} is {ISO_RESULT} triangle.")