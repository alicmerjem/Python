"""
filter only even numbers from the dict
values, values are lists
"""

def evenValues(dictionary):
    filtered_dict = {}

    for key, values in dictionary.items():
        filtered_dict[key] = [num for num in values if num%2 == 0]
    
    return filtered_dict