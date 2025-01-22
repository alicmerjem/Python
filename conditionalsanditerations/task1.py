"""
Let the user enter two numbers. 
If the first number is bigger than 
the second, print their sum. 
Otherwise, multiply those numbers. 
"""

a = int(input("Enter the first number: "))
b = int(input("Enter the first number: "))

if a > b:
    print(a+b)

if a < b:
    print(a*b)