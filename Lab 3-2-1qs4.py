# Lab 3-2-1 question 4
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

COMPARISSON_LETTER_A = "A"
COMPARISSON_LETTER_N = "n"

first_name = input("Please enter your first name: ").strip().capitalize()

#first name criteria#
if first_name.startswith(COMPARISSON_LETTER_A):
    last_name = input(f"Hi {first_name}. Please enter your last name: ").strip().capitalize()

    #last name criteria#
    if last_name.lower().endswith(COMPARISSON_LETTER_N):
        print(f"Your first name starts with the letter {COMPARISSON_LETTER_A} and your last name ends with the letter {COMPARISSON_LETTER_N}.")
        print(f"Your names match the criteria.")
    else:
        print(f"Sorry {first_name}, your last name {last_name} does not match the criteria.")
else:
    print(f"Sorry {first_name}, your first name does not match the criteria.")
    
    



