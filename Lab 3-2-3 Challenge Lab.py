# Lab 3-2-3 CHALLENGE LAB
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

NAME_LENGTH_REQUIREMENT = 2
PIN_NUMBER_LENGTH_REQUIREMENT = 6
PASSWORD_LENGTH_REQUIREMENT = 8
INVALID_PASSWORD_MESSAGE = "Your password does not meet the standard."
INVALID_PIN_MESSAGE = "Your pin number does not meet the standard."
NO_NAME_INPUT_MESSAGE = "No name was entered."
NO_INPUT = 0
VALID_CHARACTER = "-"

user_name = input("Please enter your first name: ").strip().title()

# Bypass "-" and spaces separators for proper validation
name_validator = user_name.replace(VALID_CHARACTER, "").replace(" ","") 
if len(user_name) == NO_INPUT:
    print(NO_NAME_INPUT_MESSAGE)

else:
    # print("There is something in the name now we need to validate it.")
    
    if name_validator.isalpha() and len(name_validator) >= NAME_LENGTH_REQUIREMENT:
        # print("Name purely alphabetic and contains 2 or more alphabetic characters")
        
        pin_number = input(f"{user_name}, please enter your pin number: ").strip()
        if pin_number.isdigit() and len(pin_number) == PIN_NUMBER_LENGTH_REQUIREMENT:
            # print("Pin is purely numeric exactly and 6 numeric characters")
            
            password = input(f"And lastly {user_name}, please enter the password: ").strip()
            if ((not password.isalpha()) and (not password.isdigit())) and len(password) == PASSWORD_LENGTH_REQUIREMENT:
                # print("Password is valid Alphanumeric and is exactly 8 charaters long")
                print(f"{user_name}, both your pin number and password meet the standard.")
                # print("All tests have passed. YAY!")
            else:
                print(INVALID_PASSWORD_MESSAGE)
        else:
            print(INVALID_PIN_MESSAGE)
    else:
        print(f"{user_name} is not a valid name.")
