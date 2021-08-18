# Lab 5-1-2 Challenge Lab question 3
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

FULLSTOP_CHAR = "."
VOWELS = ["a", "e", "i", "o", "u"]
user_name = input("Please enter your first name: ").strip().title()
sentence = input(f"{user_name}, please enter a sentence: ").strip()
invalid_input_msg = f"Sorry {user_name}, a sentence must end with a full stop."

# Sentence Input validation
if not sentence.endswith(FULLSTOP_CHAR):
    print(invalid_input_msg)
else:
    print(f"The sentence [{sentence}] contains the following vowels.")

    # Assign vowel counts from sentence
    count_a = sentence.lower().count(VOWELS[0])
    count_e = sentence.lower().count(VOWELS[1])
    count_i = sentence.lower().count(VOWELS[2])
    count_o = sentence.lower().count(VOWELS[3])
    count_u = sentence.lower().count(VOWELS[-1])

    # Output
    print(f"A: {count_a}, E: {count_e}, I: {count_i}, O: {count_o}, U: {count_u}")


