# Lab 5-1-2 Challenge Lab question 6
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

PASS_LENGTH_REQ = 8

user_name = input(f"Please enter your first name: ").strip().title()
password = input(f"{user_name}, please enter the password: ").strip()

# Password Validation
if any([password[0].lower() == password[-1].lower(), # First and Last character check 
           len(password) < PASS_LENGTH_REQ, # Password length requirement
           password.isalpha() or password.isdigit()]): # Alphanumeric requirement
    print(f"The password [{password}] does not meet the security standard.")
else:
    print(f"The password [{password}] meets the security standard.")

# Alternative Logical Conditional
# if all([password[0].lower() != password[-1].lower(), 
#            len(password) >= PASS_LENGTH_REQ,
#            not(password.isalpha() and password.isdigit())]): 
#     print(f"The password [{password}] meets the security standard.")
# else:
#     print(f"The password [{password}] does not meet the security standard.")

