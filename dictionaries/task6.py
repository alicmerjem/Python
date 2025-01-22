"""
combine values in a list of dicts
"""

def combineValues(list_of_dicts):
    result = {}
    for d in list_of_dicts:
        item = d['item']
        amount = d['amount']

        for item in result:
            result[item] += amount
        else:
            result[item] = amount
    return result