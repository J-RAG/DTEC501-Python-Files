# Lab 5-1-2 Challenge Lab question 4
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

FULLSTOP_CHAR = "."

user_name = input("Please enter your first name: ").strip().title()
word = input(f"Hi {user_name}, please enter a word and I will tell you if it is a palindrome: ").strip().capitalize().replace(FULLSTOP_CHAR,"")

test_word = word.lower()
if test_word == test_word[::-1]:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")

