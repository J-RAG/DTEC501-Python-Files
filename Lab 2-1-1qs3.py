# Lab 2-1-1 question 3
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz
first_integer = int(input("Please enter the first integer: "))
second_integer = int(input("Please enter the second integer: "))

#assign Arithmetic Values
sum_result = first_integer
difference_result = first_integer
product_result = first_integer
quotient_result = first_integer

#arithmetic calculations
sum_result += second_integer
difference_result -= second_integer
product_result *= second_integer
quotient_result /= second_integer

#output values
print(f"{first_integer} + {second_integer} is {sum_result}")
print(f"{first_integer} - {second_integer} is {difference_result}") 
print(f"{first_integer} * {second_integer} is {product_result}") 
print(f"{first_integer} / {second_integer} is {quotient_result}") 

