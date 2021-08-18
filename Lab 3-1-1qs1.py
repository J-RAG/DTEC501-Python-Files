# Lab 3-1-1 question 1
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

user_name = input("Please enter your first name: ").strip().capitalize()
first_number = int(input(f"Hi {user_name}, please enter the first integer: "))
second_number = int(input(f"Thank you. Please enter the second integer.\
 This integer should be less than {first_number}: "))

less_more_flag = second_number < first_number 
print(f"It is {less_more_flag} that {second_number} is less than {first_number}.")
