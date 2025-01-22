"""
printing a string n times
"""

def print_string(s, n):
    if n<=0:
        return
    print(s)
    print_string(s, n-1)
