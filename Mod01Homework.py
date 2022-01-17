#Jonathan Mai Mod 01 Homework

import random

#Variable declarations
total_payment = 0
BASEPRICE = 100
price_variance = random.randint(-3,3) * 5
soda_price = BASEPRICE + price_variance

#Welcome screen
print("Welcome! What soda would you like to purchase today?")
soda_name = input()
print("The current price of " + soda_name + " is " + str(int(soda_price)) + " cents.")

#Vending Machine Logic
while True:
    print("Please enter a payment.")
    user_payment = input()
    total_payment = total_payment + int(user_payment)
    balance = soda_price - total_payment

    if balance > 0:
        print("You still owe " + str(int(balance)) + " cents.")
    elif balance < 0:
        print("You have been refunded " + str(int(abs(balance))) + " cents.")
        break
    else:
        break

print("Enjoy your " + soda_name + "!")
    
    

