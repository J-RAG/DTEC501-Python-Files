# Lab 2-2-1 question 3
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz
user_name = input("Please enter your first name: ").capitalize().strip() #is it good discipline to add strip()?
name_lower = user_name.lower()
name_upper = user_name.upper()
print(f"{user_name}, your first name in lower case is {name_lower} and in upper case is {name_upper}.")
