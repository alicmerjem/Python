"""
write a program that asks the user to
enter one number and then display the
sum of all numbers from 0 to the number
that user entered
"""

num = int(input("enter some number: "))

total = 0

for i in range(num + 1):
    total += i

print(total)

