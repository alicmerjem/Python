"""
replacing all values in dictionary
with the leftmost digit
"""
def replaceDigits(d):
    return {key: int(str(value)[0]) for key, value in d.items()}
