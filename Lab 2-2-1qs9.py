# Lab 2-2-1 question 9
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz
TRUNK_PREFIX = 0
INTERNATIONAL_TRUNK_PREFIX = "+"
COUNTRY_CODE = "64"


#Names#
first_name = input("Please enter your first name: ").strip().capitalize()
last_name = input(f"{first_name}, please enter your last name: ").strip().capitalize()
fullname = f"{first_name} {last_name}"

#Phone Numbers#
area_code = input("Please enter your 1 digit area code: ").strip()
landline_number = input(f"Lastly {first_name},\
 Please enter your 7 landline number: ").strip().replace(" ", "")
international_number = f"{INTERNATIONAL_TRUNK_PREFIX}{COUNTRY_CODE}\
{TRUNK_PREFIX}{area_code}{landline_number}"

#Output#
print(f"Full_name: {fullname}.  International number: {international_number}")