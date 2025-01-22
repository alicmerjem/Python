"""
find sum of squares of all even numbers
from 1 to n
"""
def sum_of_squares(n):
    if n==1:
        return 1
    return n*n + sum_of_squares(n-1)