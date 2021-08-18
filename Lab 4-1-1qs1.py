# Lab 4-1-1 question 1
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.

user_name = input("Please enter your first name: ").strip().capitalize()
first_num = int(input(f"Hi {user_name}, please enter the first number: "))
second_num = int(input(f"Thanks {user_name}, please enter the second number: "))

if first_num > second_num:
    print(f"{first_num} is greater than {second_num}")

elif first_num == second_num:
    print(f"{first_num} is equal to {second_num}")

else:
    print(f"{first_num} is less than {second_num}")
