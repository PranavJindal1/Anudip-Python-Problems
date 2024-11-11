# 1. Write a program in python to calculate simple interest.
p = float(input())
t = float(input())
r = float(input())
si = (p * t * r) / 100
print(si)


# 2. Write a program to calculate compound interest.
p = float(input())
t = float(input())
r = float(input())
ci = p * (1 + r / 100) ** t - p
print(ci)

# 3. write a program to input cost price of item and apply 20% discount on it and print the total price.
cp = float(input())
discount = 0.2 * cp
total_price = cp - discount
print(total_price)

# 4.write a program to input temperature in celcius and convert it in fahrenhyte.
c = float(input())
f = (c * 9/5) + 32
print(f)


