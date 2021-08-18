# Lab 2-2-1 question 7
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

NEWZEALAND_COUNRTYCODE = "NZ"
AUSTRALIA_COUNTRYCODE = "AU"
NEWZEALAND_CURRENCY = "NZD"
AUSTRALIA_CURRENCY = "AUD"

user_name = input("Please enter your first name: ").strip().capitalize()
exchange_rate = float(input(f"Hi {user_name}. Please enter the\
 {NEWZEALAND_COUNRTYCODE}/{AUSTRALIA_COUNTRYCODE} exchange rate: "))
nzd_money = float(input(f"Please enter the amount of {NEWZEALAND_COUNRTYCODE} $'s you want to exchange: "))

aus_money = (exchange_rate) * nzd_money
 
#output 
print(f"{user_name}, I can exchange {nzd_money:.2f} {NEWZEALAND_CURRENCY}\
 into {aus_money:.2f} {AUSTRALIA_CURRENCY} for you.")
