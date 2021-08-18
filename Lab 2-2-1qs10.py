# Lab 2-2-1 question 10
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

#TESTS#
# NO_SPECIAL_INSTRUCTIONS -> "" 
# MUNGO_LIKES_BINARY -> "5 Sugars in the coffee please"
# MARMITE_CONNOISSEUR -> "real Marmite please."
# NOT_HUNGRY -> "no sugar in either drink Please!"
# NOT_THIRSTY -> "recyclable wrapping only please"

TAX_PERCENTAGE = 15
CONVERT_TO_DECIMAL = 100
MEAL_ONE_PRICE = 7.00
MEAL_TWO_PRICE = 9.00
MEAL_THREE_PRICE = 12.00
COFFEE_PRICE = 5.00


#inputs#
first_name = input("Please enter the first name of the staff member: ").strip().capitalize()
last_name = input("Please enter the first name of the customer: ").strip().capitalize()
meal_one = int(input("How many meal #1's are required: "))
meal_two = int(input("How many meal #2's are required: "))
meal_three = int(input("How many meal #3's are required: "))
coffee = int(input("How many coffee's are required: "))
request = input("Special instructions: ").strip().capitalize()

#Arithmetic assignments#
subtotal = (meal_one * MEAL_ONE_PRICE) + (meal_two* MEAL_TWO_PRICE)\
 + (meal_three * MEAL_THREE_PRICE) + (coffee * COFFEE_PRICE)
total = (subtotal * (TAX_PERCENTAGE / CONVERT_TO_DECIMAL)) + subtotal
 
#Output#
print()
print(f"Your meal was prepared by {first_name}.")
print("You have ordered the following:")
print(f"Meal #1's: {meal_one}")
print(f"Meal #2's: {meal_two}")
print(f"Meal #3's: {meal_three}")
print(f"Drinks: {coffee}")
print()
print(f"Special instructions: {request}".strip())
print(f"Nett subtotal: ${subtotal:.2f}")
print(f"Total including tax at {TAX_PERCENTAGE}% is: ${total:.2f}")
print("Thank you for your order.")
