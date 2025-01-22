"""
Write a function that takes two 
tuples of numbers and returns a 
tuple containing the elements 
common to both tuples.
"""

def find_common_elements(tuple1, tuple2):
    set1 = set(tuple1)
    set2 = set(tuple2)


    common_elements = set1.intersection(set2)


    return tuple(common_elements)
