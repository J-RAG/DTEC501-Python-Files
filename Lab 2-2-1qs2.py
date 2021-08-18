# Lab 2-2-1 question 2
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz
user_name = input("Please enter your first name: ").strip().capitalize()
first_number = int(input(f"Hi {user_name}, please enter the first integer: "))
second_number = int(input(f"Please enter the second integer: "))
product_number = first_number * second_number
print(f"{user_name}, the answer to {first_number} * {second_number} is {product_number}")
