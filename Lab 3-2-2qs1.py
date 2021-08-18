# Lab 3-2-2 question 1
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz
RESPONSE_YES = "y"
NO_FUNDS = float(0)
TOO_COLD_MESSAGE = "It's not warm enough, stay at home."
FAREWELL_MESSAGE = "Enjoy your time at the beach."
STAY_HOME_MESSAGE = "Ok, enjoy your time at home."
NO_CASH_MESSAGE = "Please remember to bring cash next time."
NOT_ENOUGH_CASH_MESSAGE = "Sorry, no ice cream today."

first_name = input("Please enter your first name: ").strip().capitalize()

beach_response = input(f"Hi {first_name}, do you want to go to the beach? (y/n): ").strip().lower()

#Beach response#
if beach_response.startswith(RESPONSE_YES):
    current_temp = int(input("Please tell me the current temperature: "))
    minimum_temp = int(input("What is the minimum temperature for going to the beach? "))
            
    #Temperature response#
    if current_temp >= minimum_temp:
        print(f"You can go to the beach because it is {current_temp} degrees.")
        ice_cream_response = input("Do you want to buy an ice cream? (y/n): ").strip().lower()

        #Ice-cream response#
        if ice_cream_response.startswith(RESPONSE_YES):
            balance = float(input("How much cash do you have? "))

            #Money Conditions#
            if balance > NO_FUNDS:
                ice_cream_cost = float(input("How much is an ice cream? "))

                if balance >= ice_cream_cost:
                    change = balance - ice_cream_cost
                    print(f"You can buy an ice cream and you will have ${change:.2f} left.")
                else:
                    print(NOT_ENOUGH_CASH_MESSAGE)
            else:
                print(NO_CASH_MESSAGE)
        print(FAREWELL_MESSAGE)               
    else:
        print(TOO_COLD_MESSAGE)
else:
    print(STAY_HOME_MESSAGE)
