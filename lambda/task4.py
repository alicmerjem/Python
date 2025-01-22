"""
return the square of a number. use a 
for loop to print the squares of 
numbers from 1 to 5
"""
square = lambda num: num**2

for i in range(1, 6):
    print(square(i))