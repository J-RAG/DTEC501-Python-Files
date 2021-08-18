# Lab 3-2-1 question 2
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz
COMPARISSON = 'n'

user_name = input("Please enter your first name: ").strip().capitalize()

if user_name.lower().endswith(COMPARISSON):
    print(f"Hi {user_name}, your first name ends with the letter {COMPARISSON}.")
else:
    print(f"Hi {user_name}, your first name does not end with the letter {COMPARISSON}.")


