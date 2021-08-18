# Lab 7-1-1 question 1
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

# initalize dictionary
person_details = dict(
    first_name = input("Please enter your first name: ").strip().capitalize(),
    last_name = input("Please enter your last name: ").strip().capitalize(),
    phone_number = input("Please enter your mobile number: ").strip()
    )
# Display Output
print(f"First name: {person_details['first_name']}")
print(f"Last name: {person_details['last_name']}")
print(f"Mobile number: {person_details['phone_number']}")
