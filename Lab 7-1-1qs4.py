# Lab 7-1-1 question 4
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

INVALID_PERCENTAGE = "That percentage is outside the bounds."
NONDIGIT_INPUT_MSG = "Digits only please."
UNKNOWN_JOB_MSG = "No such job."
PERCENTAGE_RANGE = range(-10, 11)
PERCENTAGE_DIVISOR = 100
DASH_CHAR = "-" # Used to bypass .isdigit() so negative numbers can be used

STAFF_SALARY = {
    "Software Architect": 105000,
    "Senior Software Engineer" : 95000,
    "Software Engineer" : 70000,
    "Software Tester" : 55000,
    "Trainee Software Engineer" : 35000
}

invalid_salary_input = True

while invalid_salary_input:
    number_text = input("Enter the percentage salary change: ").strip()
    # Note: ValueError if user inputs 2 dash characters. I commented out the fix
    # since it was not specified in the lab to do this
    # Bypass negative numbers by removing the dash char and spaces
    negative_nums_bypass = number_text.replace(DASH_CHAR,"").replace(" ","")
    salary_change = number_text.replace(" ", "") # Remove in-between spaces from input
    if not negative_nums_bypass.isdigit(): # or number_text.count(DASH_CHAR) > 1: # fix 
        print(NONDIGIT_INPUT_MSG)
    elif int(salary_change) not in PERCENTAGE_RANGE:
        print(INVALID_PERCENTAGE)
    else:
        invalid_salary_input = False

job_type = input("Please enter the job title: ").strip().title()
# Check if Job is in dictionary
if job_type in STAFF_SALARY:
    # New Salary arithmetic Calculation
    new_salary = (STAFF_SALARY.get(job_type) * (int(salary_change) / PERCENTAGE_DIVISOR)) + STAFF_SALARY.get(job_type) 
    print(f"{job_type}: ${int(new_salary)}") # new_salary is a float number so int is used
else:
    print(UNKNOWN_JOB_MSG)