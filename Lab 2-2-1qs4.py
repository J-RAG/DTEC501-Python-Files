# Lab 2-2-1 question 4
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

user_name = input("Please enter your first name: ").strip().capitalize()
message = input(f"Hi {user_name.title()}, please enter the message: ").strip()
number_of_duplicates = int(input("Please enter the number of repetitions needed: "))
print(f"{message.upper()}\n"  * number_of_duplicates)
print(f"{message.lower()}\n"  * number_of_duplicates)
print(f"{message.capitalize()}\n"  * number_of_duplicates)
