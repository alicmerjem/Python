"""
count occurences of a specific digit
in a given number n
"""
def count_digit(n, digit):
    if n==0:
        return 0
    
    last_digit = n % 10

    if last_digit == digit:
        return 1 + count_digit(n//10, digit)
    else:
        return count_digit(n//10, digit)