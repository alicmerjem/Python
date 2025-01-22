"""
reverse a string
"""

def reverse_string(string):
    if len(str) <= 1:
        return string 
    else:
        return reverse_string(string[1:]) + string[0]