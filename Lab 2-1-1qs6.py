# Lab 2-1-1 question 6
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

user_name = input("Please enter your first name: ")
print(f"Hi {user_name}.")
first_integer = int(input("Please enter the first integer: "))
second_integer = int(input("Please enter the second integer: "))

#arithmetic assignment
abosolute_result = abs(first_integer - second_integer)

#output 
print(f"{user_name}, the difference between {first_integer} and {second_integer} is {abosolute_result}.")