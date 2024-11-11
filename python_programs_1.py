# 1. Write a program in python to calculate simple interest.
principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time in years: "))
rate = float(input("Enter the rate of interest: "))
simple_interest = (principal * time * rate) / 100
print(f"The simple interest is: {simple_interest}")


# 2. Write a program to calculate compound interest.
principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time in years: "))
rate = float(input("Enter the annual interest rate: "))
compound_interest = principal * (1 + rate / 100) ** time - principal
print(f"The compound interest is: {compound_interest}")


# 3. write a program to input cost price of item and apply 20% discount on it and print the total price.
cost_price = float(input("Enter the cost price of the item: "))
discount_percentage = 20
discount_amount = (discount_percentage / 100) * cost_price
final_price = cost_price - discount_amount
print(f"The final price after {discount_percentage}% discount is: {final_price}")


# 4.write a program to input temperature in celcius and convert it in fahrenhyte.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"The temperature in Fahrenheit is: {fahrenheit}")


