# Lab 4-1-1 question 2
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.

EVEN_DIVISOR = 2
EVEN_RESULT = 0
user_name = input("Please enter your first name: ").strip().title()
age = int(input(f"Hi {user_name}, please enter your age in years: "))

if age % EVEN_DIVISOR == EVEN_RESULT:
    print(f"{user_name}, {age} is an even number of years.")
else:
    print(f"{user_name}, {age} is an odd age.")
