# Lab 4-1-2 Challenge Lab
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.

CURRENT_YEAR = 2020
ONE_YEAR_OLD = 1
SINGULAR_YEAR = "year"
PLURAL_YEAR = "years"
TIME_TRAVELLER_MSG = "Ah, a time traveller!"
user_name = input("Please enter your first name: ").strip().title()
age = input(f"Hi {user_name}, please enter your age in years: ").strip()


if not age.isdigit():
	print(f"{age} is not a valid age.")
else:
	# print("Age is Valid")
	year_birth = input("Thank you. Please enter the year in which you were born: ").strip()
	
	# Grammatical Result Templates
	resultagree_singular = f"{user_name}, based on you being {age} {SINGULAR_YEAR} old, I agree you were born in {year_birth}."
	resultagree_plural = f"{user_name}, based on you being {age} {PLURAL_YEAR} old, I agree you were born in {year_birth}."
	resultdisagree_singular = f"{user_name}, based on you being {age} {SINGULAR_YEAR} old, you were not born in {year_birth}."
	resultdisdagree_plural = f"{user_name}, based on you being {age} {PLURAL_YEAR} old, you were not born in {year_birth}."
	
	if not year_birth.isdigit():
		# selfnote: isdigit() returns False for inputs with negative numbers due to '-' being non-digit.
		# In this case this works in our favour since age cannot be negative.
		print(f"{year_birth} is not a valid year.")
		
	elif CURRENT_YEAR < int(year_birth): # Top down priority enforces you must check this first
		# print("Year is valid but you must be time traveller.")
		print(TIME_TRAVELLER_MSG)
		
	elif CURRENT_YEAR - int(age) != int(year_birth):
		# print("Year is valid but it's not the right year.")
		year_birth = CURRENT_YEAR - int(age) #Re-update year_birth to actual year
		print(resultdisagree_singular if int(age) == ONE_YEAR_OLD else resultdisdagree_plural)
		print(f"You were actually born in {year_birth}.")
		
	else:
		# print("Year is valid and it's the right year.")
		print(resultagree_singular if int(age) == ONE_YEAR_OLD else resultagree_plural)