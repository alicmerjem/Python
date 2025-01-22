"""
Write a function that takes a set of 
numbers and an integer n as arguments. 
The function should:
Separate the numbers in the set into 
two new sets: one containing numbers 
greater than n and another containing 
numbers less than or equal to n.
If any number in the set is exactly 
divisible by n, print "Found a 
multiple of n: <number>" for each 
such number.
Return both new sets as a tuple.
"""

def separate_and_check_multiples(numbers, n):
    greater_than_n = set()
    less_or_equal_to_n = set()
   
    for number in numbers:
        if number > n:
            greater_than_n.add(number)
        else:
            less_or_equal_to_n.add(number)
       
        if n != 0 and number % n == 0:
            print("Found a multiple of n: ", number)
   
    return greater_than_n, less_or_equal_to_n
