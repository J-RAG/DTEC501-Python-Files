# Lab 5-1-1 Challenge Lab 
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

NAME_LEN_REQ = 2
PIN_NUMBER_LEN_REQ = 6
SMALL_NAME_MSG = "Your first name is not long enough."
NAME_HASNUMBER_MSG = "Your first name must contain only alphabetic characters."
NON_NUMERICPIN_MSG = "Digits only in the pin number please."
INVALID_PIN_LEN = f"The pin number must be {PIN_NUMBER_LEN_REQ} digits long."
VALID_CHARACTER = "-"

# f"Your pin number has been confirmed {}, thank you."

# Initalize boolean flag loop input validations
invalid_name = True
invalid_pin = True


# Input name loop sequence
while invalid_name:
    user_name = input("Please enter your first name: ").strip().title()
    
    # Bypass "-" and spaces separators for proper validation
    name_validator = user_name.replace(VALID_CHARACTER, "").replace(" ","")
    # Name Validation
    if not(name_validator.isalpha()):
        print(NAME_HASNUMBER_MSG)
    elif len(name_validator) < NAME_LEN_REQ:
        print(SMALL_NAME_MSG)
    else:
        # Name is Valid we can terminate input name loop
        invalid_name = False

        while invalid_pin:
            pin_number = input("Please enter your pin number: ").strip()

            # Pin Validation
            if not(pin_number.isdigit()):
                print(NON_NUMERICPIN_MSG)
            elif len(pin_number) != PIN_NUMBER_LEN_REQ:
                print(INVALID_PIN_LEN)
            else:
                # Pin number is valid we can terminate input pin number loop
                invalid_pin = False
                print(f"Your pin number has been confirmed {user_name}, thank you.")
        
        


