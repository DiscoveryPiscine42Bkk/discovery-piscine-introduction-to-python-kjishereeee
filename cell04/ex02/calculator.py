#!/usr/bin/env python3
num1 = float(input("Give me the first number: "))
num2 = float(input("Give me the second number: "))

add = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2

print("Thank you!")

if num1 == int(num1):
    num1 = int(num1)
else:
    num1 = f"{num1}"

if num2 == int(num2):
    num2 = int(num2)
else:
    num2 = f"{num2}"


if add == int(add):
    print(f"{num1} + {num2} = {int(add)}")
else:
    print(f"{num1} + {num2} = {add:.2f}") 

if sub == int(sub):
    print(f"{num1} - {num2} = {int(sub)}")
else:
    print(f"{num1} - {num2} = {sub:.2f}")

if mult == int(mult):
    print(f"{num1} * {num2} = {int(mult)}")
else:
    print(f"{num1} * {num2} = {mult:.2f}")

if div == int(div):
    print(f"{num1} / {num2} = {int(div)}")
else:
    print(f"{num1} / {num2} = {div:.2f}")
