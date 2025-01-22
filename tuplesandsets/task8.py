"""
Write a function replace_with_fizzbuzz() 
that takes a tuple of integers as an 
argument and returns a new tuple where:
Numbers divisible by both 3 and 5 are 
replaced with "FizzBuzz"
Numbers divisible by 5 but not 3 are 
replaced with "Buzz"
Numbers that are not divisible by 5 or 
3 remain unchanged.
"""

def replace_with_fizzbuzz(input_tuple):
    result = ()
    for num in input_tuple:
        if num%3==0 and num%5==0:
            result+=("Fizbuzz",)
        elif num%5 == 0:
            result+=("Buzz",)
        else:
            result+=(num,)
    return result

# or an alternative way
def replace_fizzbuzz(tup):
    result = []
    for num in tuple:
        if num%3==0 and num%5==0:
            result.append("Fizzbuzz")
        elif num%5==0:
            result.append("Buzz")
        else:
            result.append(num)