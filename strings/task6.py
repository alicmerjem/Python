"""
write a function to check if the 
first string is within the second string
"""

def is_substring(s1, s2):
    if s1 not in s2 and s2 not in s1:
        return False
    return True