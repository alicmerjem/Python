"""
write a function to count number 
of strings where the string len is 2
or more and the first and last char
are the same from a given lst of strs
"""

def count_strings(lst):
    count = 0
    for string in lst:
        if len(lst) >= 2 and string[0] == string[-1]:
            count += 1
    return count