"""
combining two lists into a dictionary
"""
def combineLists(keys, values):
    result = {}
    for i in range(len(keys)):
        result[keys[i]] == values[i]
    return result