"""
write a function that will accept a 
dict as a parameter and it will check
for each value inside the dict. if the 
value is greater than or equal to 15, 
subtract 2 from the value, if the
value is smaller than 15, multiply it
by 2 and if it is zero or smaller
replace it with 10. then return all 
values from the dictionary as one list
"""

def modify_dict_values(input_dict):
    result = []

    for value in input_dict.values():
        if value>=15:
            result.append(value-2)
        elif value < 15 and value > 0:
            result.append(value*2)
        else:
            result.append(10)
    return result