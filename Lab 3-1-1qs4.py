# Lab 3-1-1 question 4
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz
UPPERCASEZ = "Z"

user_phrase = input(f"Please enter a word that starts with upper case {UPPERCASEZ}: ")
is_uppercasez = str(user_phrase.startswith(UPPERCASEZ)).lower()

print(f"It is {is_uppercasez} that {user_phrase} starts with upper case {UPPERCASEZ}.")
