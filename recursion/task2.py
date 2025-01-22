"""
find sum of numbers from 1 to n
"""
def one_to_n(n):
    if n == 1:
        return 1
    
    return n + one_to_n(n-1)

