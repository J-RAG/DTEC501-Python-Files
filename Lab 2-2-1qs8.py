# Lab 2-2-1 question 8
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

NEWZEALAND_COUNRTYCODE = "NZ"
UNITEDKINGDOM_COUNTRYCODE = "UK"
NEWZEALAND_CURRENCY = "NZD"
UK_CURRENCY = "UK pounds"

user_name = input("Please enter your first name: ").strip().capitalize()
exchange_rate = float(input(f"Hi {user_name}. Please enter the\
 {NEWZEALAND_COUNRTYCODE}/{UNITEDKINGDOM_COUNTRYCODE} exchange rate: "))
nzd_money = float(input(f"Please enter the amount of {NEWZEALAND_COUNRTYCODE} $'s you want to exchange: "))

uk_money = (exchange_rate) * nzd_money
 
#output 
print(f"{user_name}, I can exchange {nzd_money:.2f} {NEWZEALAND_CURRENCY}\
 into {uk_money:.2f} {UK_CURRENCY} for you.\nEnjoy spending your {UK_CURRENCY}.")
