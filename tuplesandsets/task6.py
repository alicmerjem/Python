"""
Write a function that accepts a 
tuple of characters and returns a 
dictionary with each character 
as a key and its frequency as 
the value.
"""
def frequency_counter(char_tuple):
    frequency = {}
   
    for char in char_tuple:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1


    return frequency
