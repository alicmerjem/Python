"""
Write a function modify_numbers() 
that takes a tuple of integers and 
returns a new tuple where each 
number is doubled if it’s even, 
and halved if it’s odd.
"""

def modify_numbers(input_tuple):
    result = []

    for num in input_tuple:
        if num%2==0:
            result.append(num*2)
        else:
            result.append(num/2)
    return tuple(result)