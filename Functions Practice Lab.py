# Functions practice lab
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

def double_value(number):
    """ Returns twice the amount of the number """
    return number * 2
    
current_temperature = int(input("What is the temperature? "))
result = double_value(current_temperature )
print(f"{current_temperature} * 2 = {result}")

# Hard coding values
measured_angle = 90
result = double_value(measured_angle )
print(f"{measured_angle} * 2 = {result}")

# Shorter version
age = 45
result = double_value(age)
print(f"{age} * 2 = {result}")

# Even shorter
val = 30
print(f"{val} * 2 = {double_value(val)}")

# A 1 liner
print(f"{30} * 2 = {double_value(30)}")

# Using a string
message = input("Please enter a message: ")
double_val = double_value(message)
print(f"{message } * 2 = {double_val}")

# Strings and ints
message = input("Please enter a message: ")
measured_angle = int(input("What is the angle? "))
repeated_message = double_value(message)
double_angle = double_value(measured_angle)
print(f"{message} * 2 = {repeated_message }")
print(f"{measured_angle} * 2 = {double_angle}")
