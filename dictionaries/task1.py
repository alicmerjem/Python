"""
all values smaller than 9 are doubled
"""

def doubleValues(d):
    return {key: (value*2 if value < 9 else value) for key, value in d.items()}
