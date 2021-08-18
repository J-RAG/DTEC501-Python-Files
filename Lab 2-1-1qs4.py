# Lab 2-1-1 question 4
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

user_name = input("Please enter your first name: ")
exchange_rate = float(input(f"Hi {user_name}. Please enter the NZ/AU exchange rate: "))
nzd_money = float(input("Please enter the amount of NZ $'s you want to exchange: "))

aus_money = (exchange_rate) * nzd_money
 
#output 
print(f"{user_name}, I can exchange NZ ${nzd_money:.2f} into AU ${aus_money:.2f} for you.")

##alternative format method: ##
# print("{}, I can exchange NZ ${:.2f} into AU ${:.2f} for you.".format(user_name, nzd_money, aus_money))
