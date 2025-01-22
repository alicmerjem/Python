"""
return even numbers and their sum
"""

def even_and_sum(tup):
    even_numbers = tuple(x for x in tup if x%2==0)
    total = sum(tup)
    return even_numbers, total