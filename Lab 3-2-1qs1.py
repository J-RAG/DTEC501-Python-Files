# Lab 3-2-1 question 1
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz
COMPARISSON = "A"

user_name = input("Please enter your first name: ").strip().capitalize()

if user_name.startswith(COMPARISSON):
    print(f"Hi {user_name}, your first name starts with the letter {COMPARISSON}.")
else:
    print(f"Hi {user_name}, your first name does not start with the letter {COMPARISSON}.")
