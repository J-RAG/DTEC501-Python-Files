# Lab 3-2-1 question 3
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

COMPARISSON_LETTER_A = "A"
COMPARISSON_LETTER_Y = "y"
user_name = input("Please enter your first name: ").strip().capitalize()
print(f"Hi {user_name}.")

#"A" starts with check#
if user_name.startswith(COMPARISSON_LETTER_A):
    print(f"Your first name starts with the letter {COMPARISSON_LETTER_A}.")
else:
    print(f"Your first name does not start with the letter {COMPARISSON_LETTER_A}.")

#"y" ends with check#
if user_name.lower().endswith(COMPARISSON_LETTER_Y):
    print(f"Your first name ends with the letter {COMPARISSON_LETTER_Y}.")
else:
    print(f"Your first name does not end with the letter {COMPARISSON_LETTER_Y}.")
