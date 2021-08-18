# Lab 5-3-1 question 7
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

def welcome_student(first_name, greeting_phrase = "Kia ora"):
    """
        Returns a string containing a welcome message.
    """
    return f"{greeting_phrase} {first_name}."

### Use default
##name = "Jill"
##welcome_phrase = welcome_student(name)
##print(f"Phrase returned: {welcome_phrase}")
##print(f"Phrase length: {len(welcome_phrase)}")
##
### Specify greeting
##given_name = "Joe"
##morning_greeting = "Mōrena"
##welcome_phrase = welcome_student(given_name, morning_greeting)
##print(welcome_phrase)
##
### Test for correct parameter names
##given_name = "Anna"
##afternoon_greeting = "Ata mārie"
##welcome_phrase = welcome_student(first_name = given_name, greeting_phrase = afternoon_greeting)
##print(welcome_phrase)
