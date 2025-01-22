"""
print even numbers up to an n number
"""
def print_even(n):
    if n<0:
        return
    if n%2==0:
        print_even(n-2)
        print(n)
    else:
        print_even(n-1)
