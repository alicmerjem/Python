"""
double each character in the string
- question bank
"""

def double_char(string):
    result = ''
    for char in string:
        result+=char*2
    return result

print(double_char('hello'))