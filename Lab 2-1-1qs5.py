# Lab 2-1-1 question 5
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

user_name = input("Please enter your first name: ")
print(f"Hi {user_name}.")
first_integer = int(input("Please enter the first integer: "))
second_integer = int(input("Please enter the second integer: "))

#arthmetic assignments
qoutient_result = first_integer // second_integer
remainder_result = first_integer % second_integer

#output results
print(f"{user_name}, the answer to {first_integer} divided by {second_integer} is {qoutient_result} with a remainder of {remainder_result}.")
