"""
counting even digits in a positive int
"""
def count_even(n):
    if n==0:
        return
    
    if (n%10) %2 == 0:
        return 1 + count_even(n//10)
    else:
        return count_even(n//10)